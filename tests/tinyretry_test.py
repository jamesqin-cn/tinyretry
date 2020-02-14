# -*- coding: utf-8 -*-
__author__ = 'james'

import unittest
import logging
import random
from tinyretry import *

@UntilRetryForJson(retry_code_key='errno', expected_err_code='0', max_retry_num = 10, retry_interval_sec = 0.1)
def DoHttpRequest():
    errno = random.randint(0,1)
    errmsg_arr = ['ok', 'err']
    return {
        "errno": errno,
        "errmsg": errmsg_arr[errno]
    }

class Test_TinyRetry(unittest.TestCase):
    def test_WithCache(self):
        for i in range(10):
            res = DoHttpRequest()
            self.assertEqual(res["errno"], 0)

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    unittest.main()
