import os

# Place this in the preamble of your Latex project
# \usepackage{dirtree}

# E.g. C:/Users/user/Desktop/Folder/ on windows or /home/user/Desktop/Folder/ on linux.
dir = '/home/greven/Projects/LaTeX-Dirtree-Generator/'

# Link to the Github e.g. https://github.com/UnknownDK/LaTeX-Dirtree-Generator/
gitlink = "https://github.com/UnknownDK/LaTeX-Dirtree-Generator/"

# Ignore list. This can be specific files/folders or even file extensions e.g. script.py, secretfolder, .git.
ignore = [".git"]
# Whitelist. This will triumph over ignore. So if a folder e.g. /Data/ is ignored, but .txt is whitelisted,
#  .txts will be included, but the rest of the folder will be ignored.
whitelist = []


def list_files(startpath):
    print("\dirtree{%")
    for root, dirs, files in os.walk(startpath):
        dirPrinted = False
        level = root.replace(startpath, '').count(os.sep) + 1
        if os.path.basename(root) != "":
            level += 1
        folders = root.replace('\\', '/').split('/')
        for fold in reversed(folders):
            if fold in dir:
                del(folders[folders.index(fold)])
        folderpath = ""
        folders.append("")
        for folder in folders:
            if folder != "":
                folderpath += folder + "/"
            for f in files:
                #print(f)
                if not any(ele in (folderpath + f) for ele in ignore) or any(ele in (folderpath + f) for ele in whitelist):
                    if dirPrinted == False:
                        print('.' + str(level) + ' \href{' + gitlink + 'tree/master/' + folderpath + '}{' + os.path.basename(root).replace("_", "\_") + '/}.' )
                        dirPrinted = True
                    filename = f.replace("_", "\_")
                    print('.' + str(level + 1) + ' \href{' + gitlink + 'blob/master/' + folderpath + f + '}{' + filename + '}.' )
    print("}")

list_files(dir)