# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="distributed-logging",
    version="0.0.2",
    description='This is my distributed logging package',
    long_description='This is my distributed logging package',
    author='ckf10000',
    author_email='ckf10000@sina.com',
    url='https://github.com/ckf10000/distributed-logging',
    packages=find_packages(),
    install_requires=[
        "pywin32>=303; sys_platform != 'linux'",
        "PyYAML>=6.0.1"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
