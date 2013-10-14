#!/usr/bin/env python

import os
import sys
import xml.etree.ElementTree as ET
from subprocess import call

# visit directory with video files
# for each video file,
# if extracted directory doesn't already exist for file,
# do extraction on it
# then visit extracted directory to build up xml

# Build up XML file conforming to Drawable Animation

def process_files(path):
    for filename in os.listdir(path):
        print filename

path = sys.argv[1]
if not path:
    path = '/Users/ari/Documents/Consulting/2013/Erogear/video_files'

if __name__ == '__main__':
    process_files(path)

root = ET.Element("animation-list", {
    "xmlns:android": "http://schemas.android.com/apk/res/android"
})

tree = ET.ElementTree()

