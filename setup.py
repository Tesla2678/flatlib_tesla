"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)

"""

from setuptools import setup
from setuptools import find_packages

setup(
    # Project
    name='flatlib_tesla',
    version='0.0.6',

    # Sources
    packages=find_packages(),
    package_data={
        'flatlib': [
            'resources/README.md',
            'resources/swefiles/*'
        ],
    },

    # Dependencies
    install_requires=['pyswisseph==2.08.00-1'],

    # Metadata
    description='Python library for Traditional Astrology',
    url='https://github.com/Tesla2678/flatlib_tesla',
    keywords=['Astrology', 'Traditional Astrology'],
    license='MIT',

    # Authoring
    author='Tesla',
    author_email='Tesla2678@gmail.com',

    # Classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
