import numpy as np
import os
import commit
from commit import trk2dictionary
commit.setup()

os.system('tckgen WM_FODs.mif 100M.tck -act 5TT.mif -backtrack -crop_at_gmwmi -seed_dynamic WM_FODs.mif -maxlength 250 -select 100M -cutoff 0.06')

os.system('tcksift 100M.tck WM_FODs.mif 10M_SIFT.tck -act 5TT.mif -term_number 10M')

os.system('sh2peaks WM_FODs.mif Peaks.nii.gz')
os.system('mrconvert nodes_fixSGM.mif GM_1x1x1.nii.gz')

os.system( 'tck2connectome -force -nthreads 0 -assignment_radial_search 2 -out_assignments fibers_assignment.txt 10M_SIFT.tck GM_1x1x1.nii.gz connectome.csv' )

if not os.path.isdir( 'bundles' ) :
    os.mkdir( 'bundles' )
os.system( 'connectome2tck -force -nthreads 0 -exclusive -files per_edge -keep_self 10M_SIFT.tck fibers_assignment.txt bundles/bundle_' )

C = np.loadtxt( 'connectome.csv', delimiter=',' ) # NB: change 'delimiter' to suits your needs
CMD = 'tckedit -force -nthreads 0'
for i in range(C.shape[0]):
    CMD_i = 'tckedit -force -nthreads 0'
    for j in range(i,C.shape[0]):
        if C[i,j] > 0 :
            CMD_i += ' bundles/bundle_%d-%d.tck' %(i+1,j+1)
    os.system( CMD_i + ' bundles/demo01_fibers_connecting_%d.tck' % (i+1) )
    CMD += ' bundles/demo01_fibers_connecting_%d.tck' %(i+1)
os.system( CMD + ' demo01_fibers_connecting.tck' )


trk2dictionary.run(
    filename_tractogram = 'demo01_fibers_connecting.tck',
    filename_mask       = 'nodif_brain_mask.nii.gz',
    fiber_shift         = 0.5
)



# convert the bvals/bvecs pair to a single scheme file
import amico
amico.util.fsl2scheme( 'bvals', 'bvecs', 'DWI.scheme' )

# load the data
mit = commit.Evaluation( '.', '.' )
mit.load_data( 'data.nii.gz', 'DWI.scheme' )

# use a forward-model with 1 Stick for the streamlines and 2 Balls for all the rest
mit.set_model( 'StickZeppelinBall' )
d_par       = 1.7E-3             # Parallel diffusivity [mm^2/s]
d_perps_zep = []                 # Perpendicular diffusivity(s) [mm^2/s]
d_isos      = [ 1.7E-3, 3.0E-3 ] # Isotropic diffusivity(s) [mm^2/s]
mit.model.set( d_par, d_perps_zep, d_isos )

mit.generate_kernels( regenerate=True )
mit.load_kernels()

# create the sparse data structures to handle the matrix A
mit.load_dictionary( 'COMMIT' )
mit.set_threads()
mit.build_operator()

# perform the fit
mit.fit( tol_fun=1e-3, max_iter=1000, verbose=False )
mit.save_results( path_suffix="_COMMIT1" )

x_nnls, _, _ = mit.get_coeffs( get_normalized=False )



C = np.loadtxt( 'connectome.csv', delimiter=',' )
C = np.triu( C ) # be sure to get only the upper-triangular part of the matrix
group_size = C[C>0].astype(np.int32)

tmp = np.insert( np.cumsum(group_size), 0 , 0)
group_idx = np.array( [np.arange(tmp[i],tmp[i+1]) for i in range(len(tmp)-1)] )

group_w = np.empty_like( group_size, dtype=np.float64 )
for k in range(group_size.size) :
    group_w[k] = np.sqrt(group_size[k]) / ( np.linalg.norm(x_nnls[group_idx[k]]) + 1e-12 )


reg_lambda = 5e-4 # change to suit your needs

prior_on_bundles = commit.solvers.init_regularisation(
    mit,
    regnorms    = [commit.solvers.group_sparsity, commit.solvers.non_negative, commit.solvers.non_negative],
    structureIC = group_idx,
    weightsIC   = group_w,
    lambdas     = [reg_lambda, 0.0, 0.0]
)



mit.fit( tol_fun=1e-3, max_iter=1000, regularisation=prior_on_bundles, verbose=False )
mit.save_results( path_suffix="_COMMIT2" )
