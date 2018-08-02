import hou
import glob
import sys, os

node = hou.pwd()
geo = node.geometry()

filedir = hou.evalParm('filedir')
parmname = hou.evalParm('newFileName')
path = filedir+'*'

# rename all the files in specified directory
i=0;
fileList = glob.glob(path)
for fname in fileList:
    i+=1
    num = ('{:04d}'.format(i))
    basename = os.path.basename(fname)
    filename, file_ext = os.path.splitext(basename)
    newname = parmname+num+file_ext
    os.rename(fname, os.path.join(os.path.dirname(fname), newname))

# convert to bgeo
fileList = glob.glob(path)
for fname in fileList:
    if fname.endswith('.obj'):
        geo = fname.replace('.obj', '.bgeo')
        cmd = 'gconvert %s %s' % (fname, geo)
        if os.system(cmd):
             print 'Error running command'
             break

