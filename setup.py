# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='excon',
    version='0.1.1',
    description='Extract and convert data from PDFs',
    long_description=readme,
    author='Ryan Trigg',
    author_email='rbutustree@gmail.com',
    url='https://github.com/rbutus/excon.git',
    license=license,
    packages=find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
    ],
)

