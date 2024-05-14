import os

# Place this in the preamble of your Latex project
# \usepackage{dirtree}

# E.g. C:/Users/user/Desktop/Folder/ on windows or /home/user/Desktop/Folder/ on linux.
dir = '/home/greven/repos/ES10-Drowning/'

# Link to the Github e.g. https://github.com/UnknownDK/LaTeX-Dirtree-Generator/
gitlink = "https://github.com/UnknownDK/ES10-Drowning/"

# Name of branch
branch = "master"

# Ignore list. This can be specific files/folders or even file extensions e.g. script.py, secretfolder, .git.
# Everything in every .gitignore is automatically added
ignore = [".git",]


def list_files(startpath):
    ignore_list = []
    # Walk the directory tree to find .gitignore files and extract their rules
    for root, dirs, files in os.walk(startpath):
        if '.gitignore' in files:
            with open(os.path.join(root, '.gitignore'), 'r') as ignore_file:
                ignore_list.extend(
                    [os.path.join(root, line.strip()) for line in ignore_file.readlines() if not line.startswith('#')]
                )

    print("\dirtree{%")
    for root, dirs, files in os.walk(startpath):
        if not any(ele in root for ele in ignore) and not any(ele in root for ele in ignore_list):
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
                if not any(ele in f for ele in ignore) and not any(ele in os.path.join(root, f) for ele in ignore_list):
                    filename = f.replace("_", "\_")
                    print('.' + str(level + 1) + ' \href{' + gitlink + 'blob/master/' + folderpath + f + '}{' + filename + '}.' )
    print("}")

list_files(dir)
