#!/usr/bin/env python3

from PIL import Image
import os
# Image module from the Pillow Library

download_folder = "download_mapp/"
output_folder = "/bilder/fixade/"

# Adjusts all images in the folder and saves the finished images in the output_folder
for bild in os.listdir(download_folder):
    if bild != ".DS_Store":
        im = Image.open(os.path.join(download_mapp, bild))
        im = im.rotate(-90)
        im = im.resize((128,128))
        im = im.convert("RGB")
        im.save(os.path.join(output_folder, bild+".jpeg"))
