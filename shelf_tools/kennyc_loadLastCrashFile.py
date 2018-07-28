import hou
import glob
import os

fileList = glob.glob('/home/kennyc/houdini_temp/crash*.hip*')
latestFile = max(fileList, key=os.path.getctime)

try:
    hou.hipFile.load(latestFile)
except hou.LoadWarning, errormsg:
    print errormsg

