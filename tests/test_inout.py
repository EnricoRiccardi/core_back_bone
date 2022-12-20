# -*- coding: utf-8 -*-
# Copyright (c) 2022, Enrico Development Team.
# Distributed under the LGPLv2.1+ License.
"""
Test in and output functions.

"""
import os
import unittest
from io import StringIO
from unittest.mock import patch
import numpy as np
from pyeli.inout.inout import save_results, parse_settings_file, read_data_file


class InoutTesting(unittest.TestCase):
    """
    Unit tests to check PyEli inout effectiveness.

    """
    def test_inout(self):
        """
        Write and read a json.

        """
        dummy_dict = {'ducati': 999,
                      'ferrari': 'F40'}

        with patch('sys.stdout', new=StringIO()) as stdout:
            save_results('test.file', dummy_dict)
        self.assertIn('Results saved', stdout.getvalue().strip())

        read_data = parse_settings_file('test.file')
        os.remove('test.file')
        self.assertEqual(dummy_dict, read_data)

    def test_segment_file_reader(self):
        """
        Read a segment file.

        """
        expected_read_not_ok = np.array([[100, 200], [150, 250]])
        source_file_not_ok = 'segment_not_ok.s'
        read_not_ok = read_data_file(source_file_not_ok)

        self.assertEqual(read_not_ok.tolist(), expected_read_not_ok.tolist())

        expected_read_ok = np.array([[100, 200], [200, 300]])
        source_file_ok = 'segment_ok.s'
        read_ok = read_data_file(source_file_ok)

        self.assertEqual(read_ok.tolist(), expected_read_ok.tolist())

        not_existing_file = 'graal.s'
        with self.assertRaises(ValueError) as cmess:
            read_data_file(not_existing_file)
        self.assertEqual(str(cmess.exception),
                         'Input file "graal.s" not existing!')

        not_supported_file = 'file.unicorn'
        with self.assertRaises(ValueError) as cmess:
            read_data_file(not_supported_file)
        self.assertEqual(str(cmess.exception),
                         'Input file "file.unicorn" NOT supported!')

    def test_function_file_reader(self):
        """
        Read a function file.

        """
        source_file = 'function.f'
        expected_read = np.array([25.0, 26.0, 10.0, 11.0])
        read_ok = read_data_file(source_file)

        self.assertEqual(read_ok.tolist(), expected_read.tolist())


if __name__ == '__main__':
    unittest.main()
