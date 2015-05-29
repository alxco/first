#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='MyFirstPkg',
    version='0.1.1',
    packages=find_packages(exclude=['docs', 'testspec']),
    install_requires=['mockito==0.5.2']
)
