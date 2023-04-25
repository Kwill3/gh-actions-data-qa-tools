"""
    Description: Checks for duplicate key and start-end pairs

    Author: William Lee

"""

import os
import sys

BASE_PATH = os.path.abspath('.')
sys.path.insert(0, os.path.abspath('./src'))
print (sys.path)

from dupe_key_check import scan_file


def test_scenario1():
    test1 = {}
    count = scan_file(BASE_PATH + '/src/tests/test_scenario1.csv', test1)
    assert (count == 1)

