import cv2

import os, glob

from os import listdir, makedirs

from os.path import isfile, join
origpath = 'images'  # Source Folder
dstpath = 'grayscaleImages'  # Destination Folder
try:
    makedirs(dstpath)
except:
    print("Directory already exist, images will be written in same folder")
# Folder won't used
folders = [f for f in listdir(origpath) if not isfile(join(origpath, f))]
for folder in folders:
    path = origpath + "/" + folder
    try:
        makedirs(dstpath + "/" + folder)
    except:
        print("Directory already exist, images will be written in same folder")
    files = [f for f in listdir(path) if isfile(join(path, f))]
    print(files)
    for image in files:
        try:
            src = cv2.imread(os.path.join(path, image), cv2.IMREAD_UNCHANGED)
            # Save the transparency channel alpha
            *_, alpha = cv2.split(src)
            gray_layer = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            # Duplicate the grayscale image to mimic the BGR image and finally add the transparency
            dst = cv2.merge((gray_layer, gray_layer, gray_layer, alpha))
            newdstPath = join(dstpath + "/" + folder, image)
            cv2.imwrite(newdstPath, dst)
        except:
            print("{} is not converted".format(image))
    for fil in glob.glob("*.png"):
        try:
            image = cv2.imread(fil)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert to greyscale
            cv2.imwrite(os.path.join(dstpath, fil), gray_image)
        except:
            print('{} is not converted')
