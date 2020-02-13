#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name = "tinyretry",
    version = "0.1.0",
    author = "jamesqin",
    author_email = "jamesqin@vip.qq.com",
    description = "tinyretry is a python module that provides failure retry encapsulation for the target function",
    long_description = "tinyretry is a python module that provides failure retry encapsulation for the target function",
    license = "MIT",
    url = "https://github.com/jamesqin-cn/tinyretry",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
)
