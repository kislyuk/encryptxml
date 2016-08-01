#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='encryptxml',
    version='0.0.1',
    url='https://github.com/kislyuk/encryptxml',
    license='Apache Software License',
    author='Andrey Kislyuk',
    author_email='kislyuk@gmail.com',
    description='Python XML Encryption library',
    long_description=open('README.rst').read(),
    install_requires=[
        'signxml >= 1.0.1'
    ],
    packages=find_packages(exclude=['test']),
    platforms=['MacOS X', 'Posix'],
    package_data={'encryptxml': ['schemas/*.xsd']},
    zip_safe=False,
    include_package_data=True,
    test_suite='test',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
