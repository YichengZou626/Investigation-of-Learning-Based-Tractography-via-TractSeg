import os

subjects = ['134627', '135124', '137128', '144226', '145834', ' 146432', '146735', '146937', '148133', '155938', '156334', '158136']
for subject in subjects:
    func_1 = 'calc_FA -i '+subject+'/data.nii.gz -o '+subject+'/FA.nii.gz --bvals '+subject+'/bvals --bvecs '+subject+'/bvecs --brain_mask '+subject+'/nodif_brain_mask.nii.gz'
    os.system(func_1)
    func_2 = 'TractSeg -i '+subject+'/mrtrix_peaks.nii.gz -o '+subject+'/tractseg_output --output_type tract_segmentation'
    os.system(func_2)
    func_3 = 'TractSeg -i '+subject+'/mrtrix_peaks.nii.gz -o '+subject+'/tractseg_output --output_type endings_segmentation'
    os.system(func_3)
    func_4 = 'TractSeg -i '+subject+'/mrtrix_peaks.nii.gz -o '+subject+'/tractseg_output --output_type TOM'
    os.system(func_4)
    func_5 = 'Tracking -i '+subject+'/mrtrix_peaks.nii.gz -o '+subject+'/tractseg_output --nr_fibers 5000'
    os.system(func_5)
    func_6 = 'Tractometry -i '+subject+'/tractseg_output/TOM_trackings/ -o '+subject+'/tractseg_output/Tractometry_subject1.csv -e '+subject+'/tractseg_output/endings_segmentations/ -s '+subject+'/FA.nii.gz'
    os.system(func_6)
    
    print(subject + ' is finished!')
