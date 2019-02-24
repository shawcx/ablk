#!/usr/bin/env python3

import sys
import os

from setuptools import setup

setup(
    name         = 'ablk',
    version      = '0.1',
    author       = 'Matthew Oertle',
    author_email = 'moertle@gmail.com',
    description  = 'Terminal image viewer',
    url          = 'https://github.com/moertle/ablk',
    license      = 'TBD',
    entry_points = {
        'console_scripts': [
            'ablk    = ablk:main',
            ]
        },
    py_modules = ['ablk'],
    install_requires = [
        'pillow',
        ],
    zip_safe = True
    )
