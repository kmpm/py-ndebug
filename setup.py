#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# convert markdown to rst
try:
    import pypandoc
    desc = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    desc = ''

with open('ndebug/__init__.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(),
        re.MULTILINE
    ).group(1)

with open('requirements/base.txt', 'r') as fd:
    requirements = fd.read().strip().split('\n')

setup(
    name='ndebug',
    version=version,
    description=("Tiny python debugging utility modeled after visionmedia's ",
                 "node.js debug module"),
    long_description=desc,
    author='Peter Magnusson',
    author_email='peter@birchroad.se',
    url='https://github.com/kmpm/py-ndebug',
    license='MIT',
    packages=['ndebug'],
    install_requires=requirements,
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
