# directly taken from a sidefx and odforce forum. Can't seem to find the forum though.
import hou
mode = hou.updateModeSetting().name()

if mode == 'AutoUpdate':
	hou.setUpdateMode(hou.updateMode.Manual)
if mode == 'Manual':
	hou.setUpdateMode(hou.updateMode.AutoUpdate)

