# -*- coding: utf-8 -*-
# Copyright (c) 2022, Enrico Development Team.
# Distributed under the LGPLv2.1+ License.
"""
Main program test run in a Pythonic way.

It decompress the data (from .zip) and run direclty the main function.

"""
import os
import zipfile
from pyeli.core.main import pyeli_main
# pylint: disable=C0103

source_zip = 'testfiles.zip'
with zipfile.ZipFile(source_zip) as zipped:
    zipped.extractall(path=os.path.dirname(os.path.abspath(source_zip)))

pyeli_main('test.json')
