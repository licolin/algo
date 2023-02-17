# -*- encoding: utf-8 -*-
# Author: li_colin

import unittest
from BeautifulReport import BeautifulReport
from parameterized import parameterized
import sys

params_info = [(1, "xxxxxyyyy", True, True), (3, "aaaaabbbbbb", True, False)]


class TestDemo(unittest.TestCase):
    params = params_info

    @parameterized.expand(params)
    def test_a(self, case_id, details, a, b):
        '''case details'''
        sys.stdout.write(str(case_id) + str(details))
        sys.stderr.write("error info is ")
        self.assertTrue(a)
        self.assertTrue(a)


def suite():
    st = unittest.TestSuite()
    loader = unittest.TestLoader()
    st.addTest(loader.loadTestsFromTestCase(TestDemo))
    print("st ", st.__dict__)
    return st


if __name__ == '__main__':
    br = BeautifulReport(suite())
    print("br ", br)
    br.report(filename="re.html", log_path='.', report_dir='.', description="test")
