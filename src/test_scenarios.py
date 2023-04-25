"""
    Description: Tests for version_overlap_check Python file

    Author: William Lee

"""

import os
import sys
from version_overlap_check import scan_file

BASE_PATH = os.path.abspath('.')
sys.path.insert(0, os.path.abspath('./src'))
print (sys.path)

def test_scenario1():
    test1 = {}
    count = scan_file(BASE_PATH + '/src/tests/test_scenario1.csv', test1)
    print(test1)
    assert count == 6
