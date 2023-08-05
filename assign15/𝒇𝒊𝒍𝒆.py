import os
import shutil

cwd = os.getcwd()
img = os.listdir()
a = cwd+"/folder_images"
os.mkdir(a) 
list_images = ["jpeg", "heic", "png", "tiff", "gif", "jpeg", "raw"]

for i in img:
    if len(i.split(".")) > 1:
        for j in list_images:
            if i.split(".")[1] == j:
                shutil.copy(i, a)
