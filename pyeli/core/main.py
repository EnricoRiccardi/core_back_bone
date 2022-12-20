# -*- coding: utf-8 -*-
# Copyright (c) 2022, Enrico Development Team.
# Distributed under the LGPLv2.1+ License.
"""
Main function.

"""
from pyeli.core.runner import Geni
from pyeli.inout.inout import save_results


def pyeli_main(input_file=None):
    """
    Run the computations.

    """
    run = Geni(input_file)
    run.read_settings()
    run.check_settings()
    run.read_data_files()
    run.check_data()
    results = run.execute()
    run.cheers()
    save_results('results.pyeli', results)
