#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from loggable import __version__, __doc__

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='loggable',
    version=__version__,
    packages=find_packages(exclude=('tests.*', 'tests',)),
    url='https://github.com/nick-allen/python-loggable',
    license='MIT',
    author='Nick Allen',
    author_email='nick.allen.cse@gmail.com',
    description=__doc__,
    long_description=long_description,
    include_package_data=True,
    zip_safe=True
)
