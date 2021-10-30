import os
path = "/media/anim/D@7@570R@G3/Anime/Haikyuu!!/Haikyuu!!"
removeString = '日向翔哉'
fileList = os.listdir(path)
for file in fileList:
    if removeString in file:
        os.rename(os.path.join(path, file), os.path.join(path, file.replace(removeString, "")))