with open('100610/streamline_weights.txt') as f:
    weights = f.readlines()

cnm = set()
count = 99999

weight1 = []
for w in weights:
    value = float(w)
    if value > 0 and value < count:
        count = value
 
for w in weights:
    if float(w) >= count:
        weight1.append(w)

print(len(weight1))

import os
os.system('tckedit 100610/demo01_fibers_connecting.tck 100610.tck -tck_weights_in 100610/streamline_weights.txt -minweight ' +str(count))
###############################################
with open('102311/streamline_weights.txt') as f:
    weights = f.readlines()

cnm = set()
count = 99999

weight2 = []
for w in weights:
    value = float(w)
    if value > 0 and value < count:
        count = value
 
for w in weights:
    if float(w) >= count:
        weight2.append(w)

print(len(weight2))

os.system('tckedit 102311/demo01_fibers_connecting.tck 102311.tck -tck_weights_in 102311/streamline_weights.txt -minweight ' +str(count))
###############################################
with open('102816/streamline_weights.txt') as f:
    weights = f.readlines()

cnm = set()
count = 99999

weight3 = []
for w in weights:
    value = float(w)
    if value > 0 and value < count:
        count = value
 
for w in weights:
    if float(w) >= count:
        weight3.append(w)

print(len(weight3))

os.system('tckedit 102816/demo01_fibers_connecting.tck 102816.tck -tck_weights_in 102816/streamline_weights.txt -minweight ' +str(count))
###############################################
with open('104416/streamline_weights.txt') as f:
    weights = f.readlines()

cnm = set()
count = 99999

weight4 = []
for w in weights:
    value = float(w)
    if value > 0 and value < count:
        count = value
 
for w in weights:
    if float(w) >= count:
        weight4.append(w)

print(len(weight4))

os.system('tckedit 104416/demo01_fibers_connecting.tck 104416.tck -tck_weights_in 104416/streamline_weights.txt -minweight ' +str(count))
###############################################
with open('105923/streamline_weights.txt') as f:
    weights = f.readlines()

cnm = set()
count = 99999

weight5 = []
for w in weights:
    value = float(w)
    if value > 0 and value < count:
        count = value
 
for w in weights:
    if float(w) >= count:
        weight5.append(w)

print(len(weight5))

os.system('tckedit 105923/demo01_fibers_connecting.tck 105923.tck -tck_weights_in 105923/streamline_weights.txt -minweight ' +str(count))
###############################################
with open('108323/streamline_weights.txt') as f:
    weights = f.readlines()

cnm = set()
count = 99999

weight6 = []
for w in weights:
    value = float(w)
    if value > 0 and value < count:
        count = value
 
for w in weights:
    if float(w) >= count:
        weight6.append(w)

print(len(weight6))

os.system('tckedit 108323/demo01_fibers_connecting.tck 108323.tck -tck_weights_in 108323/streamline_weights.txt -minweight ' +str(count))
###############################################
with open('109123/streamline_weights.txt') as f:
    weights = f.readlines()

cnm = set()
count = 99999

weight7 = []
for w in weights:
    value = float(w)
    if value > 0 and value < count:
        count = value
 
for w in weights:
    if float(w) >= count:
        weight7.append(w)

print(len(weight7))

os.system('tckedit 109123/demo01_fibers_connecting.tck 109123.tck -tck_weights_in 109123/streamline_weights.txt -minweight ' +str(count))
###############################################
with open('111312/streamline_weights.txt') as f:
    weights = f.readlines()

cnm = set()
count = 99999

weight8 = []
for w in weights:
    value = float(w)
    if value > 0 and value < count:
        count = value
 
for w in weights:
    if float(w) >= count:
        weight8.append(w)

print(len(weight8))

os.system('tckedit 111312/demo01_fibers_connecting.tck 111312.tck -tck_weights_in 111312/streamline_weights.txt -minweight ' +str(count))
###############################################
with open('111514/streamline_weights.txt') as f:
    weights = f.readlines()

cnm = set()
count = 99999

weight9 = []
for w in weights:
    value = float(w)
    if value > 0 and value < count:
        count = value
 
for w in weights:
    if float(w) >= count:
        weight9.append(w)

print(len(weight9))

os.system('tckedit 111514/demo01_fibers_connecting.tck 111514.tck -tck_weights_in 111514/streamline_weights.txt -minweight ' +str(count))
###############################################
with open('115017/streamline_weights.txt') as f:
    weights = f.readlines()

cnm = set()
count = 99999

weight10 = []
for w in weights:
    value = float(w)
    if value > 0 and value < count:
        count = value
 
for w in weights:
    if float(w) >= count:
        weight10.append(w)

print(len(weight10))

os.system('tckedit 115017/demo01_fibers_connecting.tck 115017.tck -tck_weights_in 115017/streamline_weights.txt -minweight ' +str(count))
###############################################

os.system('tckedit 100610.tck 102311.tck 102816.tck 104416.tck 105923.tck 108323.tck 109123.tck 111312.tck 111514.tck 115017.tck cnm.tck')

from dipy.data import get_fnames
from dipy.io.streamline import load_tractogram
from dipy.segment.clustering import QuickBundles
from dipy.segment.metric import Metric
from dipy.segment.featurespeed import ArcLengthFeature
from dipy.segment.metric import EuclideanMetric
import numpy as np


fornix = load_tractogram('cnm.tck', 'avg.nii.gz', bbox_valid_check=False)
streamlines = fornix.streamlines
print(len(streamlines))

t1 = len(weight1)
t2 = t1+len(weight2)
t3 = t2+len(weight3)
t4 = t3+len(weight4)
t5 = t4+len(weight5)
t6 = t5+len(weight6)
t7 = t6+len(weight7)
t8 = t7+len(weight8)
t9 = t8+len(weight9)
t10 = t9+len(weight10)

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


os.mkdir('100610/bundles')
os.mkdir('100610/tdi')
os.mkdir('100610/masks')
os.mkdir('100610/weights')

os.mkdir('102311/bundles')
os.mkdir('102311/tdi')
os.mkdir('102311/masks')
os.mkdir('102311/weights')

os.mkdir('102816/bundles')
os.mkdir('102816/tdi')
os.mkdir('102816/masks')
os.mkdir('102816/weights')

os.mkdir('104416/bundles')
os.mkdir('104416/tdi')
os.mkdir('104416/masks')
os.mkdir('104416/weights')

os.mkdir('105923/bundles')
os.mkdir('105923/tdi')
os.mkdir('105923/masks')
os.mkdir('105923/weights')

os.mkdir('108323/bundles')
os.mkdir('108323/tdi')
os.mkdir('108323/masks')
os.mkdir('108323/weights')

os.mkdir('109123/bundles')
os.mkdir('109123/tdi')
os.mkdir('109123/masks')
os.mkdir('109123/weights')

os.mkdir('111312/bundles')
os.mkdir('111312/tdi')
os.mkdir('111312/masks')
os.mkdir('111312/weights')

os.mkdir('111514/bundles')
os.mkdir('111514/tdi')
os.mkdir('111514/masks')
os.mkdir('111514/weights')

os.mkdir('115017/bundles')
os.mkdir('115017/tdi')
os.mkdir('115017/masks')
os.mkdir('115017/weights')


func1 = 'fslmerge -tr 100610/bundle_masks.nii.gz '
func2 = 'fslmerge -tr 102311/bundle_masks.nii.gz '
func3 = 'fslmerge -tr 102816/bundle_masks.nii.gz '
func4 = 'fslmerge -tr 104416/bundle_masks.nii.gz '
func5 = 'fslmerge -tr 105923/bundle_masks.nii.gz '
func6 = 'fslmerge -tr 108323/bundle_masks.nii.gz '
func7 = 'fslmerge -tr 109123/bundle_masks.nii.gz '
func8 = 'fslmerge -tr 111312/bundle_masks.nii.gz '
func9 = 'fslmerge -tr 111514/bundle_masks.nii.gz '
func10 = 'fslmerge -tr 115017/bundle_masks.nii.gz '

###############################################
for number in range(cluster_number):
    maxl = 0
    for cluster in clusters:
        if len(cluster)>maxl and len(cluster)<pre_max:
            maxl = len(cluster)
            largest_cluster = cluster
    pre_max = maxl
    print(pre_max)
    index = largest_cluster.indices
    
    weight1_rep = ['0.0']*len(weight1)
    weight2_rep = ['0.0']*len(weight2)
    weight3_rep = ['0.0']*len(weight3)
    weight4_rep = ['0.0']*len(weight4)
    weight5_rep = ['0.0']*len(weight5)
    weight6_rep = ['0.0']*len(weight6)
    weight7_rep = ['0.0']*len(weight7)
    weight8_rep = ['0.0']*len(weight8)
    weight9_rep = ['0.0']*len(weight9)
    weight10_rep = ['0.0']*len(weight10)
    
    for i in index:
        if i < t1:
            weight1_rep[i] = '1.0'
        elif i >= t1 and i < t2:
            i = i-t1
            weight2_rep[i] = '1.0'
        elif i >= t2 and i < t3:
            i = i-t2
            weight3_rep[i] = '1.0'
        elif i >= t3 and i < t4:
            i = i-t3
            weight4_rep[i] = '1.0'
        elif i >= t4 and i < t5:
            i = i-t4
            weight5_rep[i] = '1.0'
        elif i >= t5 and i < t6:
            i = i-t5
            weight6_rep[i] = '1.0'
        elif i >= t6 and i < t7:
            i = i-t6
            weight7_rep[i] = '1.0'
        elif i >= t7 and i < t8:
            i = i-t7
            weight8_rep[i] = '1.0'
        elif i >= t8 and i < t9:
            i = i-t8
            weight9_rep[i] = '1.0'
        elif i >= t9 and i < t10:
            i = i-t9
            weight10_rep[i] = '1.0'
    
###############################################
    file = '100610/weights/' + str(number) + '.txt'
    with open(file, 'w') as f:
        f.write('\n'.join(weight1_rep))
    CMD = 'tckedit 100610.tck 100610/bundles/cluster' + str(number) +'.tck -tck_weights_in ' + file + ' -minweight 1.0'
    os.system(CMD)

    CMD = 'tckmap 100610/bundles/cluster' + str(number) + '.tck -contrast tdi 100610/tdi/t' + str(number) + '.nii.gz -template 100610/b0.nii.gz'
    os.system(CMD)

    CMD = 'fslmaths 100610/tdi/t' + str(number) + '.nii.gz -bin 100610/masks/mask' + str(number) + '.nii.gz'
    os.system(CMD)

    mask = '100610/masks/mask' + str(number) + '.nii.gz '
    func1 += mask
###############################################
    file = '102311/weights/' + str(number) + '.txt'
    with open(file, 'w') as f:
        f.write('\n'.join(weight2_rep))
    CMD = 'tckedit 102311.tck 102311/bundles/cluster' + str(number) +'.tck -tck_weights_in ' + file + ' -minweight 1.0'
    os.system(CMD)

    CMD = 'tckmap 102311/bundles/cluster' + str(number) + '.tck -contrast tdi 102311/tdi/t' + str(number) + '.nii.gz -template 102311/b0.nii.gz'
    os.system(CMD)

    CMD = 'fslmaths 102311/tdi/t' + str(number) + '.nii.gz -bin 102311/masks/mask' + str(number) + '.nii.gz'
    os.system(CMD)

    mask = '102311/masks/mask' + str(number) + '.nii.gz '
    func2 += mask
###############################################
    file = '102816/weights/' + str(number) + '.txt'
    with open(file, 'w') as f:
        f.write('\n'.join(weight3_rep))
    CMD = 'tckedit 102816.tck 102816/bundles/cluster' + str(number) +'.tck -tck_weights_in ' + file + ' -minweight 1.0'
    os.system(CMD)

    CMD = 'tckmap 102816/bundles/cluster' + str(number) + '.tck -contrast tdi 102816/tdi/t' + str(number) + '.nii.gz -template 102816/b0.nii.gz'
    os.system(CMD)

    CMD = 'fslmaths 102816/tdi/t' + str(number) + '.nii.gz -bin 102816/masks/mask' + str(number) + '.nii.gz'
    os.system(CMD)
###############################################
    mask = '102816/masks/mask' + str(number) + '.nii.gz '
    func3 += mask
    
    file = '104416/weights/' + str(number) + '.txt'
    with open(file, 'w') as f:
        f.write('\n'.join(weight4_rep))
    CMD = 'tckedit 104416.tck 104416/bundles/cluster' + str(number) +'.tck -tck_weights_in ' + file + ' -minweight 1.0'
    os.system(CMD)

    CMD = 'tckmap 104416/bundles/cluster' + str(number) + '.tck -contrast tdi 104416/tdi/t' + str(number) + '.nii.gz -template 104416/b0.nii.gz'
    os.system(CMD)

    CMD = 'fslmaths 104416/tdi/t' + str(number) + '.nii.gz -bin 104416/masks/mask' + str(number) + '.nii.gz'
    os.system(CMD)

    mask = '104416/masks/mask' + str(number) + '.nii.gz '
    func4 += mask
###############################################
    file = '105923/weights/' + str(number) + '.txt'
    with open(file, 'w') as f:
        f.write('\n'.join(weight5_rep))
    CMD = 'tckedit 105923.tck 105923/bundles/cluster' + str(number) +'.tck -tck_weights_in ' + file + ' -minweight 1.0'
    os.system(CMD)

    CMD = 'tckmap 105923/bundles/cluster' + str(number) + '.tck -contrast tdi 105923/tdi/t' + str(number) + '.nii.gz -template 105923/b0.nii.gz'
    os.system(CMD)

    CMD = 'fslmaths 105923/tdi/t' + str(number) + '.nii.gz -bin 105923/masks/mask' + str(number) + '.nii.gz'
    os.system(CMD)

    mask = '105923/masks/mask' + str(number) + '.nii.gz '
    func5 += mask
###############################################
    file = '108323/weights/' + str(number) + '.txt'
    with open(file, 'w') as f:
        f.write('\n'.join(weight6_rep))
    CMD = 'tckedit 108323.tck 108323/bundles/cluster' + str(number) +'.tck -tck_weights_in ' + file + ' -minweight 1.0'
    os.system(CMD)

    CMD = 'tckmap 108323/bundles/cluster' + str(number) + '.tck -contrast tdi 108323/tdi/t' + str(number) + '.nii.gz -template 108323/b0.nii.gz'
    os.system(CMD)

    CMD = 'fslmaths 108323/tdi/t' + str(number) + '.nii.gz -bin 108323/masks/mask' + str(number) + '.nii.gz'
    os.system(CMD)

    mask = '108323/masks/mask' + str(number) + '.nii.gz '
    func6 += mask
###############################################
    file = '109123/weights/' + str(number) + '.txt'
    with open(file, 'w') as f:
        f.write('\n'.join(weight7_rep))
    CMD = 'tckedit 109123.tck 109123/bundles/cluster' + str(number) +'.tck -tck_weights_in ' + file + ' -minweight 1.0'
    os.system(CMD)

    CMD = 'tckmap 109123/bundles/cluster' + str(number) + '.tck -contrast tdi 109123/tdi/t' + str(number) + '.nii.gz -template 109123/b0.nii.gz'
    os.system(CMD)

    CMD = 'fslmaths 109123/tdi/t' + str(number) + '.nii.gz -bin 109123/masks/mask' + str(number) + '.nii.gz'
    os.system(CMD)

    mask = '109123/masks/mask' + str(number) + '.nii.gz '
    func7 += mask
###############################################
    file = '111312/weights/' + str(number) + '.txt'
    with open(file, 'w') as f:
        f.write('\n'.join(weight8_rep))
    CMD = 'tckedit 111312.tck 111312/bundles/cluster' + str(number) +'.tck -tck_weights_in ' + file + ' -minweight 1.0'
    os.system(CMD)

    CMD = 'tckmap 111312/bundles/cluster' + str(number) + '.tck -contrast tdi 111312/tdi/t' + str(number) + '.nii.gz -template 111312/b0.nii.gz'
    os.system(CMD)

    CMD = 'fslmaths 111312/tdi/t' + str(number) + '.nii.gz -bin 111312/masks/mask' + str(number) + '.nii.gz'
    os.system(CMD)

    mask = '111312/masks/mask' + str(number) + '.nii.gz '
    func8 += mask
###############################################
    file = '111514/weights/' + str(number) + '.txt'
    with open(file, 'w') as f:
        f.write('\n'.join(weight9_rep))
    CMD = 'tckedit 111514.tck 111514/bundles/cluster' + str(number) +'.tck -tck_weights_in ' + file + ' -minweight 1.0'
    os.system(CMD)

    CMD = 'tckmap 111514/bundles/cluster' + str(number) + '.tck -contrast tdi 111514/tdi/t' + str(number) + '.nii.gz -template 111514/b0.nii.gz'
    os.system(CMD)

    CMD = 'fslmaths 111514/tdi/t' + str(number) + '.nii.gz -bin 111514/masks/mask' + str(number) + '.nii.gz'
    os.system(CMD)

    mask = '111514/masks/mask' + str(number) + '.nii.gz '
    func9 += mask
###############################################
    file = '115017/weights/' + str(number) + '.txt'
    with open(file, 'w') as f:
        f.write('\n'.join(weight10_rep))
    CMD = 'tckedit 115017.tck 115017/bundles/cluster' + str(number) +'.tck -tck_weights_in ' + file + ' -minweight 1.0'
    os.system(CMD)

    CMD = 'tckmap 115017/bundles/cluster' + str(number) + '.tck -contrast tdi 115017/tdi/t' + str(number) + '.nii.gz -template 115017/b0.nii.gz'
    os.system(CMD)

    CMD = 'fslmaths 115017/tdi/t' + str(number) + '.nii.gz -bin 115017/masks/mask' + str(number) + '.nii.gz'
    os.system(CMD)

    mask = '115017/masks/mask' + str(number) + '.nii.gz '
    func10 += mask
###############################################
func1 += '1'
func2 += '1'
func3 += '1'
func4 += '1'
func5 += '1'
func6 += '1'
func7 += '1'
func8 += '1'
func9 += '1'
func10 += '1'
os.system(func1)
os.system(func2)
os.system(func3)
os.system(func4)
os.system(func5)
os.system(func6)
os.system(func7)
os.system(func8)
os.system(func9)
os.system(func10)
