#!/usr/bin/python

try:
    from setuptools import setup, Extension
    has_setuptools = True
except ImportError:
    from distutils.core import setup, Extension
    has_setuptools = False

version_string = '0.1.0'


setup_kwargs = {}

# Requirements
install_requires = [
    # PyPi

    # Non PyPi
]
dependency_links = [
]

setup(name='giturlparse',
    description='A Git URL parsing module (supports parsing and rewriting)',
    keywords='git url parse ssh github bitbucket',
    version=version_string,
    url='https://github.com/FriendCode/giturlparse.py',
    license='Apache v2',
    author="Aaron O'Mullan",
    author_email='aaron@friendco.de',
    long_description="""
    """,
    packages=['giturlparse', 'giturlparse.platforms'],
    install_requires=install_requires,
    dependency_links=dependency_links,
    **setup_kwargs
)
