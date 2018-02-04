import os
from setuptools import setup, find_packages

with open('README.rst') as f:
	long_description = f.read()

setup(
  name = 'pyprog',
  version = '1.0.1',
  packages = find_packages(),
  description = ('A library for creating customizable progress indicators.'),
  long_description = long_description,
  author = 'Bill Kudo',
  author_email = 'bluesky42624@gmail.com',
  license = 'GNU AGPLv3',
  url = 'https://github.com/Bill13579/pyprog',
  keywords = 'progress bar indicator pyprog',
)