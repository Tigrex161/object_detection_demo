from PIL import Image
import os
import argparse

def rescale_images(directory):
    for img in os.listdir(directory):
        im = Image.open(directory+img)
        im_resized = im.resize((800,600), Image.ANTIALIAS)
        im_resized.save(directory+img)

rescale_images("test/")