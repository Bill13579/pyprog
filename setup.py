import os
from setuptools import setup, find_packages

with open('README.rst') as f:
	long_description = f.read()

setup(
  name = 'pyprog',
  version = '1.1.0-0',
  packages = find_packages(),
  description = ('A library for creating super customizable progress indicators.'),
  long_description = long_description,
  author = 'BillK',
  author_email = 'bluesky42624@gmail.com',
  license = 'GNU AGPLv3',
  url = 'https://github.com/Bill13579/pyprog',
  keywords = 'progress bar indicator pyprog',
)
