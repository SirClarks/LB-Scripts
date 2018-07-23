import hou
import glob
import os

fileList = glob.glob('/tmp/houdini_temp/crash*')
latestFile = max(fileList, key=os.path.getctime)

try:
    hou.hipFile.load(latestFile)
except hou.LoadWarning, e:
    print e
