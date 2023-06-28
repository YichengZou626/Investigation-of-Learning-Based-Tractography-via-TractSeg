import os

file_list = os.listdir('/work/users/z/y/zyc626/dti')
files = []
for f in file_list:
    if f != '.DS_Store':
        files.append(f)



for file in files:
    os.system('rm -rf /work/users/z/y/zyc626/dti/' + file+ '/bundles')
    os.system('rm -rf /work/users/z/y/zyc626/dti/' + file+ '/tdi')
    os.system('rm -rf /work/users/z/y/zyc626/dti/' + file+ '/masks')
    os.system('rm -rf /work/users/z/y/zyc626/dti/' + file+ '/weights')

