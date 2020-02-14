# -*- coding: utf-8 -*-
__author__ = 'james'

import unittest
import logging
import random
from tinyretry import RetryUntilForJson,RetryWhileForJson

@RetryUntilForJson(retry_code_key='errno', expected_err_code=0, max_retry_num = 10, retry_interval_sec = 0.1)
def DoHttpRequest1():
    errno = random.randint(0,2)
    errmsg_arr = ['ok', 'err-timeout', 'err-req-limit']
    return {
        "errno": errno,
        "errmsg": errmsg_arr[errno]
    }

@RetryWhileForJson(retry_code_key='errno', not_expected_err_code=2, max_retry_num = 10, retry_interval_sec = 0.1)
def DoHttpRequest2():
    errno = random.randint(0,2)
    errmsg_arr = ['ok', 'err-timeout', 'err-req-limit']
    return {
        "errno": errno,
        "errmsg": errmsg_arr[errno]
    }

class Test_TinyRetry(unittest.TestCase):
    def test_RetryUntilForJson(self):
        for i in range(5):
            res = DoHttpRequest1()
            self.assertEqual(res["errno"], 0)

    def test_RetryWhileForJson(self):
        for i in range(5):
            res = DoHttpRequest2()
            self.assertNotEqual(res["errno"], 2)

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    unittest.main()
