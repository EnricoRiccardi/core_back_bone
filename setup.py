# -*- coding: utf-8 -*-
# Copyright (c) 2022, Enrico Development Team.
# Distributed under the LGPLv2.1+ License.
from codecs import open as openc
import pathlib
from setuptools import setup, find_namespace_packages


def get_requirements():
    """Read requirements.txt and return a list of requirements."""
    here = pathlib.Path(__file__).absolute().parent
    requirements = []
    filename = here.joinpath('requirements.txt')
    with openc(filename, encoding='utf-8') as fileh:
        for lines in fileh:
            package = lines.split('>=')[1].strip()
            requirements.append(lines.strip())
    return requirements


setup(
    name='pyeli',
    version='0.0.9.dev0',
    description='A simulation package for getting hired at Elixir',
    author='Enrico Riccardi',
    author_email='enricori@uio.no',
    license='LGPLv2.1+',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        ('License :: OSI Approved :: '
         'GNU Lesser General Public License v2 or later (LGPLv2+)'),
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Bioinformatics',
    ],
    keywords='elixir interview uio',
    packages=find_namespace_packages(),
    install_requires=get_requirements(),
    entry_points={
        'console_scripts': [
            'pyeli = pyeli.bin.pyelirun:entry_point',
        ]
    },
)
