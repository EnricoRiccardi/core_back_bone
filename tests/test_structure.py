# -*- coding: utf-8 -*-
# Copyright (c) 2022, Enrico Development Team.
# Distributed under the LGPLv2.1+ License.
"""
Test program structure.

"""
import unittest
from io import StringIO
from unittest.mock import patch
from pyeli.core.runner import Geni
from pyeli.core.main import pyeli_main
from pyeli.bin.pyelirun import hello_world, bye_world


class StructureTesting(unittest.TestCase):
    """
    Class for testing program structure.

    """
    def test_main(self):
        """
        Test main runner function.

        """
        general = Geni()
        general.settings['Main'] = {'tasks': ['gnegne']}
        with self.assertRaises(ValueError) as smess:
            general.check_settings()
        self.assertIn('Task', str(smess.exception))

        general = Geni()
        general.settings['Main'] = {'tasks': [],
                                    'cross_tasks': ['nanna']}
        with self.assertRaises(ValueError) as smess:
            general.check_settings()
        self.assertIn('Cross-Task', str(smess.exception))

        with patch('sys.stdout', new=StringIO()) as stdout:
            general.cheers()
        self.assertIn('D-O-N-E', stdout.getvalue().strip())

    def test_pyeli_main(self):
        """
        Test main function.

        """
        with patch('sys.stdout', new=StringIO()) as stdout:
            pyeli_main(input_file='test.json')
        self.assertIn('D-O-N-E', stdout.getvalue().strip())

    def test_polite_functions(self):
        """
        Test greeting function.

        """
        with patch('sys.stdout', new=StringIO()) as stdout:
            hello_world()
        self.assertIn('xir', stdout.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as stdout:
            bye_world()
        self.assertIn('execution', stdout.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
