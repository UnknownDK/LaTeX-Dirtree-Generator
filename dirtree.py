import os

# Place this in the preamble of your Latex project
# \usepackage{dirtree}

# E.g. C:/Users/user/Desktop/Folder/ on windows or /home/user/Desktop/Folder/ on linux.
dir = '/home/greven/Desktop/LarsVRKlo/'

# Link to the Github e.g. https://github.com/UnknownDK/LaTeX-Dirtree-Generator/
gitlink = "https://github.com/simo389b/LarsVRKlo/"

# Name of branch
branch = "master"

# Ignore list. This can be specific files/folders or even file extensions e.g. script.py, secretfolder, .git.
ignore = [".git", ".mat", "Image", "ISM", "Reverb", "AllpassFilter_class", "HeadphoneFilter", "FDN", "Absorption", ".pdf", ".png", ".txt", "Data", "Responses", "roomGeneratorSpas", "Parameters"]


def list_files(startpath):
    print("\dirtree{%")
    for root, dirs, files in os.walk(startpath):
        if not any(ele in root for ele in ignore):
            level = root.replace(startpath, '').count(os.sep) + 1
            if os.path.basename(root) != "":
                level += 1
            folders = root.replace('\\', '/').split('/')
            for fold in reversed(folders):
                if fold in dir:
                    del(folders[folders.index(fold)])
            folderpath = ""
            for folder in folders:
                folderpath += folder + "/"
            print('.' + str(level) + ' \href{' + gitlink + 'tree/master/' + folderpath + '}{' + os.path.basename(root).replace("_", "\_") + '/}.' )
            for f in files:
                if not any(ele in f for ele in ignore):
                    filename = f.replace("_", "\_")
                    print('.' + str(level + 1) + ' \href{' + gitlink + 'blob/master/' + folderpath + f + '}{' + filename + '}.' )
    print("}")

list_files(dir)