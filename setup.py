#!/usr/bin/env python

from distutils.core import setup

setup(name='a10ctl',
    version='0.1',
    description='Command line tool managing servers on A10 lb',
    install_requires=[
        'acos-client',
    ],
    scripts=['a10ctl']
)

