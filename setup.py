import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="videx",
      version="0.1",
      description="Convert movie media files into XML files and source images for Android AnimationDrawable resources",
      long_description=read('README.md'),
      author="Ari Lacenski",
      author_email="alacenski@gmail.com",
      license="WTFPL",
      packages=['videx'],
      zip_safe=False
      )
