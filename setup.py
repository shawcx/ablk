#!/usr/bin/env python3

import sys
import os

from setuptools import setup

setup(
    name             = 'ablk',
    version          = '0.3',
    author           = 'Matthew Shaw',
    author_email     = 'mshaw.cx@gmail.com',
    license          = 'MIT',
    description      = 'Terminal image viewer',
    long_description = open('README.rst').read(),
    url              = 'https://github.com/shawcx/ablk',
    entry_points = {
        'console_scripts': [
            'ablk    = ablk:main',
            ]
        },
    py_modules = ['ablk'],
    install_requires = [
        'pillow',
        ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Viewers',
        ],
    zip_safe = True
    )
