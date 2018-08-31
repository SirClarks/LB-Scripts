from os.path import join, isfile
from shutil import copytree

# change these to match where you would like to save files
dest_dir = 'destination/'
src_dir = 'source/'

# ignore any files but files with '.hipnc' extension
ignore_func = lambda d, files: [f for f in files if isfile(join(d, f)) and f[-6:] != '.hipnc']
copytree(src_dir, dest_dir, ignore=ignore_func)

# all code based on stackoverflow answer found here: https://stackoverflow.com/questions/25643454/copy-all-files-with-certain-extension-while-maintaining-directory-tree
# better solutions exist, especially when dealing with the -6 characters for file name, but this script does the job nice and dirty
