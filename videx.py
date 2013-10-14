#!/usr/bin/env python

import os
import sys
import xml.etree.ElementTree as ET
from subprocess import call, check_call

# visit directory with video files
# for each video file,
# if extracted directory doesn't already exist for file,
# do extraction on it
# then visit extracted directory to build up xml


OUTPUT_ROOT_DIR = "videx_output"
FRAME_RATE = 30

def process_files(in_dir, out_dir):
    for filename in os.listdir(in_dir):
        if filename == '.DS_Store':
            continue
        shortname = os.path.splitext(filename)[0]
        file_path = os.path.abspath(os.path.join(in_dir, filename))

        new_target_dir = os.path.abspath(setup_output_dir(os.path.join(out_dir, shortname)))
        extract_frames(file_path, shortname, new_target_dir)
        # Build up XML file conforming to Drawable Animation
        #print filename


def setup_output_dir(output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    return output_path

def extract_frames(file_path, shortname, output_directory):
    ffmpeg_args = "ffmpeg -i %s -r %d -f image2 %s-" % (file_path, FRAME_RATE, os.path.join(output_directory, "img"))
    ffmpeg_args = ffmpeg_args + "%3d.png"
    if (os.path.exists(output_directory)):
        check_call(ffmpeg_args, shell=True)


path = sys.argv[1]
if not path:
    path = '/Users/ari/Documents/Consulting/2013/Erogear/video_files'


if __name__ == '__main__':
    # Get output directory
    parent = os.path.join(path, os.path.pardir)
    output_directory = setup_output_dir(os.path.join(parent, OUTPUT_ROOT_DIR))

    # Start putting extracted files into directory
    process_files(in_dir=path, out_dir=output_directory)


root = ET.Element("animation-list", {
    "xmlns:android": "http://schemas.android.com/apk/res/android"
})

tree = ET.ElementTree()

