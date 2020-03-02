import os

fpath = str(input('Enter file path(include "/" at end of path): '))     # directory that contains files to be renamed
i = 0
for fname in os.listdir(fpath):
    dest = fpath + str(i) + '.jpg'  # destination ~ renames the files to numbers starting from '0.jpg'
    srce =  fpath + fname   # source

    print('Renaming from ', srce, 'to', dest)
    os.rename(srce, dest)
    i += 1