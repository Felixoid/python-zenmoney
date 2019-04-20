#!/usr/bin/env python

'''
Setup script for zenmoney API
'''

from setuptools import setup
from zenmoney import VERSION


setup(
    name='zenmoney',
    version='.'.join(str(d) for d in VERSION),
    description='Library for zenmoney.ru API',
    url='https://github.com/Felixoid/python-zenmoney',
    license='MIT',
    author='Mikhail f. Shiryaev',
    author_email='mr.felixoid@gmail.com',
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3',
)
