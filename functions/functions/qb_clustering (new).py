import os

CMD = 'tckedit '

file_list = os.listdir('/work/users/z/y/zyc626/dti')
files = []
for f in file_list:
    if f != '.DS_Store':
        files.append(f)
        
os.chdir('/work/users/z/y/zyc626/dti')
os.mkdir('tck')

weight_list = []
for file in files:
    text = file+'/streamline_weights.txt'
    with open(text) as f:
        weights = f.readlines()

    cnm = set()
    count = 99999

    weight = []
    for w in weights:
        value = float(w)
        if value > 0 and value < count:
            count = value
 
    for w in weights:
        if float(w) >= count:
            weight.append(w)

    weight_list.append(len(weight))

    os.system('tckedit '+file+'/demo01_fibers_connecting.tck '+ 'tck/'+file+'.tck -tck_weights_in '+file+'/streamline_weights.txt -minweight '+str(count))
    
    CMD = CMD +'tck/'+ file +'.tck '
CMD += 'cnm.tck'
os.system(CMD)

############################################################################
from dipy.data import get_fnames
from dipy.io.streamline import load_tractogram
from dipy.segment.clustering import QuickBundles
from dipy.segment.metric import Metric
from dipy.segment.featurespeed import ArcLengthFeature
from dipy.segment.metric import EuclideanMetric
import numpy as np

fornix = load_tractogram('/work/users/z/y/zyc626/dti/cnm.tck', '/work/users/z/y/zyc626/dti/100610/avg.nii.gz', bbox_valid_check=False)
streamlines = fornix.streamlines

w_list = []
for i in range(len(weight_list)):
    if i == 0:
        w_list.append(weight_list[i])
    else:
        w = w_list[i-1] + weight_list[i]
        w_list.append(w)

#print(weight_list)
#print(w_list)

from dipy.segment.clustering import QuickBundles
from dipy.segment.metric import AveragePointwiseEuclideanMetric
from dipy.tracking.streamline import set_number_of_points

streamlines = set_number_of_points(streamlines, nb_points=12)

metric = AveragePointwiseEuclideanMetric()
qb = QuickBundles(threshold=30., metric=metric)
clusters = qb.cluster(streamlines)

print("Nb. clusters:", len(clusters))
print("Cluster sizes:", map(len, clusters))

large_cluster_list = []
cluster_number = 100
pre_max = 999999999
largest_cluster = clusters[0]

func_list = []
for file in files:
    os.system('fslroi /work/users/z/y/zyc626/dti/'+file+'/data.nii.gz /work/users/z/y/zyc626/dti/'+file+'/b0.nii.gz 0 1')
    os.mkdir('/work/users/z/y/zyc626/dti/'+file+'/bundles')
    os.mkdir('/work/users/z/y/zyc626/dti/'+file+'/tdi')
    os.mkdir('/work/users/z/y/zyc626/dti/'+file+'/masks')
    os.mkdir('/work/users/z/y/zyc626/dti/'+file+'/weights')
    #os.system('fslroi '+file+'/data.nii.gz '+file+'/b0.nii.gz 0 1 ')
    func = 'fslmerge -tr /work/users/z/y/zyc626/dti/'+file+'/bundle_masks.nii.gz '
    func_list.append(func)
    
############################################################################
for number in range(cluster_number):
    maxl = 0
    for cluster in clusters:
        if len(cluster)>maxl and len(cluster)<pre_max:
            maxl = len(cluster)
            largest_cluster = cluster
    pre_max = maxl
    #print(pre_max)
    index = largest_cluster.indices
    
    wr_list = []
    for i in range(len(w_list)):
        if i == 0:
            wr = ['0.0']*weight_list[i]
            for idx in index:
                if idx < w_list[i]:
                    wr[idx] = '1.0'
            wr_list.append(wr)
        else:
            wr = ['0.0']*weight_list[i]
            for idx in index:
                if idx >= w_list[i-1] and idx < w_list[i]:
                    wr[idx-w_list[i-1]] = '1.0'
            wr_list.append(wr)
        
    for i in range(len(wr_list)):
        file = files[i]
        text = file+'/weights/'+str(number)+'.txt'
        with open(text, 'w') as f:
            f.write('\n'.join(wr_list[i]))
        CMD = 'tckedit /work/users/z/y/zyc626/dti/tck/'+file+'.tck /work/users/z/y/zyc626/dti/'+file+'/bundles/cluster'+str(number)+'.tck -tck_weights_in '+text+' -minweight 1.0'
        os.system(CMD)

        CMD = 'tckmap /work/users/z/y/zyc626/dti/'+file+'/bundles/cluster'+str(number)+'.tck -contrast tdi /work/users/z/y/zyc626/dti/'+file+'/tdi/t'+str(number)+'.nii.gz -template /work/users/z/y/zyc626/dti/'+file+'/b0.nii.gz'
        os.system(CMD)

        CMD = 'fslmaths /work/users/z/y/zyc626/dti/'+file+'/tdi/t'+str(number)+'.nii.gz -bin /work/users/z/y/zyc626/dti/'+file+'/masks/mask'+str(number)+'.nii.gz'
        os.system(CMD)

        mask = '/work/users/z/y/zyc626/dti/'+file+'/masks/mask'+ str(number)+'.nii.gz '
        func_list[i] += mask

for i in range(len(func_list)):
    func_list[i] += '1'
    os.system(func_list[i])
    
