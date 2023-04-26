# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

REQUIREMENTS = [
    'grpcio',
    'google-api-core'
]


CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.7',
    'Topic :: Communications',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]

setup(
    name='chirpstack-api',
    version = "4.0.5",
    url='https://github.com/SAP529/chirpstack-api',
    author='Sagar Patel',
    author_email='sagu25patel@hotmail.com',
    license='MIT',
    description='Chirpstack Python API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
)
