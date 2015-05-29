#!/usr/bin/env python
from setuptools import setup, find_packages

pkgs = find_packages(exclude=['docs', 'testspec'])
print ('pkgs', pkgs)
setup(
    name='MyFirstPkg',
    version='0.1.1',
    packages=pkgs,
    install_requires=['mockito==0.5.2']
)
