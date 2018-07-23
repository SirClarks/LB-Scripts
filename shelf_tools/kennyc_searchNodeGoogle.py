import hou
import webbrowser
import string

def getSelectedNode():
    selected = hou.selectedNodes()
    node = selected[-1]
    return node

# get and convert the node type to a string for search term
n = getSelectedNode()
foo = str(hou.Node.type(n))
foo_list = foo.split()
n = foo_list[-1]
n = n[:-1]

# search string combine houdini with node name
search = 'http://www.google.com/search?q=sidefx+houdini+'+n

# perform websearch
webbrowser.open(search)
