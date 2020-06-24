#!/usr/bin/python
from PIL import Image
import os, sys

import os

path ="."
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))
dirs= filelist
print(dirs[3])
def resize():
    for item in dirs:
        if item.endswith("JPG") or item.endswith("jpg") or item.endswith("png") or item.endswith("jpeg") or item.endswith("JPEG"):
            
            if os.path.isfile(item):
                im = Image.open(item)
                f, e = os.path.splitext(item)
                imResize = im.resize((530,420), Image.ANTIALIAS)
                imResize.save(f + '_resized.jpg', 'JPEG', quality=90)

resize()

