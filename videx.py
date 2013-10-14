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
DURATION = 50

def process_files(in_dir, out_dir):
    for filename in os.listdir(in_dir):
        if filename == '.DS_Store':
            continue
        shortname = os.path.splitext(filename)[0]
        file_path = os.path.abspath(os.path.join(in_dir, filename))

        file_target_dir = os.path.abspath(setup_output_dir(os.path.join(out_dir, shortname)))
        extract_frames(file_path, shortname, file_target_dir)
        # Build up XML file conforming to Drawable Animation
        make_xml_file(shortname=shortname, img_path=file_target_dir, write_to_path=out_dir)
    print "Done.\r"


def setup_output_dir(output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    return output_path


def extract_frames(file_path, shortname, output_directory):
    # Android requires drawable filenames to be lowercase
    ffmpeg_args = "ffmpeg -i %s -r %d -f image2 %s_" % (file_path, FRAME_RATE, os.path.join(output_directory, shortname.lower()))
    ffmpeg_args = ffmpeg_args + "%3d.png"
    if (os.path.exists(output_directory)):
        call(ffmpeg_args, shell=True)


def make_xml_file(shortname, img_path, write_to_path):
    root = ET.Element("animation-list", {
        "xmlns:android": "http://schemas.android.com/apk/res/android"
    })
    for filename in os.listdir(img_path):
        # Android requires drawable filenames to be lowercase
        item = ET.SubElement(root, "item", {
            "android:drawable": "@drawable/%s" % os.path.splitext(filename)[0].lower(),
            "android:duration": str(DURATION)
        })

    indent(root)
    tree = ET.ElementTree(root)
    outfile = os.path.abspath(os.path.join(write_to_path, shortname + ".xml"))
    tree.write(outfile)


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

# Pass in path to video files on command line
# e.g. /Users/ari/Documents/video_files
path = sys.argv[1]

if __name__ == '__main__':
    # Get output directory
    parent = os.path.join(path, os.path.pardir)
    output_directory = setup_output_dir(os.path.join(parent, OUTPUT_ROOT_DIR))

    # Start putting extracted files into directory
    process_files(in_dir=path, out_dir=output_directory)


tree = ET.ElementTree()

