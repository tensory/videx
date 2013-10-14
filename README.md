videx
=====

Videx is for Android developers who need to render animations in the app from video files.

It converts video files (*.avi, etc) into AnimationDrawable batches that you can drop into your /res/drawable directory.

Requirements
------------
Videx is based on [http://linuxers.org/tutorial/how-extract-images-video-using-ffmpeg](ffmpeg). If you don't have that, install it by your favorite means. I used Homebrew: `brew install ffmpeg`

It is limited to processing the media file types that ffmpeg understands.

Installation
------------
1. Download this repository .tar.gz and extract it
2.
```
cd videx
python setup.py
```

Usage
-----
`videx /Full/path/to/your/source/video/directory`

Videx does not destroy original files, but the script must have write permissions in the video source directory. It will create a directory called `videx_output` with XML files and subfolders containing animation frames.

License
-------
Videx is released under the [WTFPL](http://en.wikipedia.org/wiki/WTFPL).