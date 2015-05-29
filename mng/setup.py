#!/usr/bin/env python
from setuptools import setup, find_packages
import mng

pkgs = find_packages(exclude=['docs'])
print ('pkgs', pkgs)
setup(
    name='MyFirstPkg',
    version=mng.__version__,
    packages=pkgs,
    install_requires=['mockito==0.5.2']
)
