#!/usr/bin/env python
# -*- coding: utf-8 -*-
import giturlparse

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = giturlparse.__version__


readme = open('README.rst').read()


setup(
    name='giturlparse',
    version=version,
    description='A Git URL parsing module (supports parsing and rewriting)',
    long_description=readme,
    license='Apache v2',
    author="Aaron O'Mullan",
    author_email='aaron@friendco.de',
    url='https://github.com/nephila/giturlparse',
    maintainer='Iacopo Spalletti',
    maintainer_email='i.spalletti@nephila.it',
    packages=['giturlparse', 'giturlparse.platforms'],
    include_package_data=True,
    install_requires=[],
    keywords='git url parse ssh github bitbucket',
    test_suite='giturlparse.tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
