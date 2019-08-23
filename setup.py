#!/usr/bin/env python

'''
Setup script for zenmoney API
'''

from setuptools import setup, find_packages
from zenmoney import VERSION


with open('README.md') as f:
    long_description = f.read()

setup(
    name='zenmoney',
    version='.'.join(str(d) for d in VERSION),
    description='Library for zenmoney.ru API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Felixoid/python-zenmoney',
    license='MIT',
    author='Mikhail f. Shiryaev',
    author_email='mr.felixoid@gmail.com',
    install_requires=['requests'],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
)
