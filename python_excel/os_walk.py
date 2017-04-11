import os


spath = 'H:/Project_Munich_Technology/New_name_ MIs/'

# list everything in thr directory. Files directories etc
#print(os.listdir(spath))

# Split everything
#for roots, dirs, files in os.walk(spath):
#    for directory in dirs:
#        print('Directory = {}'.format(directory))
#        for file in files:
#            print('...File = {}'.format(os.path.join(spath, file)))


# # only the roots
##  next itterator function [] donates level 0 = roots, 1 = dirs etc
# roots = next(os.walk(spath))[0]
# print('Roots = {}'.format(roots))
#
# # only the dirs
# dirs =next(os.walk(spath))[1]
# print('Dirs = {}'.format(dirs))
#
# # only the files
# files = next(os.walk(spath))[2]
# print('Files = {}'.format(files))

for root, dirs, files in os.walk(spath):

    #print(root)
    for file in files:
        pathname = os.path.join(root,file)
        filesize = os.path.getsize(pathname)
        # Replace \ with /
        pathname = '/'.join(pathname.split('\\'))
        print(pathname)
        print(filesize)
    print()
