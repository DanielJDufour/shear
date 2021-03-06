from setuptools import setup
from os import path
from re import sub

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

# remove emojiis
long_description = sub(":[a-z]+:", "- ", long_description)

# replace html top
long_description = "# Shear\nTrim Excess Quotes from your Strings\n" + long_description[long_description.index("#"):]

setup(
  name = 'shear',
  packages = ['shear'],
  entry_points={
      'console_scripts': ['shear=shear.__init__:main'],
  },
  version = "0.0.4",
  description = '🐑 Shear: Trim Excess Quotes from your Strings in Python and on the Command Line',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'Daniel J. Dufour',
  author_email = 'daniel.j.dufour@gmail.com',
  url = 'https://github.com/DanielJDufour/shear',
  download_url = 'https://github.com/DanielJDufour/shear/tarball/download',
  keywords = ['python', 'string', 'unquote'],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    'Operating System :: OS Independent',
  ],
  install_requires=[]
)
