#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of hellopyworld.
# https://github.com/scorphus/hellopyworld

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Pablo S Blum <scorphus@gmail.com>

from setuptools import setup, find_packages
from hellopyworld import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='hellopyworld',
    version=__version__,
    description='Hello, Python World! This is a Python package example.',
    long_description='''
Hello, Python World! This is a Python package example.
''',
    keywords='python package hello world',
    author='Pablo S Blum',
    author_email='scorphus@gmail.com',
    url='https://github.com/scorphus/hellopyworld',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            'hellopyworld=hellopyworld.main:main',
        ],
    },
)
