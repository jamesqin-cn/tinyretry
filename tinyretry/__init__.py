# -*- coding:utf-8 -*-
__author__ = 'james'

import logging
import functools
import time

# we will retry until the return code equals to the special value
def RetryUntilForJson(retry_code_key, expected_err_code, max_retry_num = 3, retry_interval_sec = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            logging.info("call RetryUntilForJson(%s)(...)", func.__name__)
            for i in range(max_retry_num):
                res = func(*args, **kw)
                if retry_code_key in res and str(res[retry_code_key]) == str(expected_err_code):
                    logging.info("    Get expected error code %s", str(res[retry_code_key]))
                    break
                logging.info("    Error code %s was found, retry %d", str(res[retry_code_key]), i+1)
                time.sleep(retry_interval_sec)
            return res
        return wrapper
    return decorator

# while the return code equals to the special value, we will retry
def RetryWhileForJson(retry_code_key, not_expected_err_code, max_retry_num = 3, retry_interval_sec = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            logging.info("call RetryWhileForJson(%s)(...)", func.__name__)
            for i in range(max_retry_num):
                res = func(*args, **kw)
                if retry_code_key in res and str(res[retry_code_key]) != str(not_expected_err_code):
                    logging.info("    Get not expected error code %s", str(res[retry_code_key]))
                    break
                logging.info("    Error code %s was found, retry %d", str(res[retry_code_key]), i+1)
                time.sleep(retry_interval_sec)
            return res
        return wrapper
    return decorator    

# we will retry until the return code equals to the special value
def RetryUntilForBool(expected_bool, max_retry_num = 3, retry_interval_sec = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            logging.info("call RetryUntilForBool(%s)(...)", func.__name__)
            for i in range(max_retry_num):
                res = func(*args, **kw)
                if res == expected_bool:
                    logging.info("    Get expected return value %s", res)
                    break
                logging.info("    Return value %d was found, retry %d", res, i+1)
                time.sleep(retry_interval_sec)
            return res
        return wrapper
    return decorator

# while the return code equals to the special value, we will retry
def RetryWhileForBool(not_expected_bool, max_retry_num = 3, retry_interval_sec = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            logging.info("call RetryWhileForBool(%s)(...)", func.__name__)
            for i in range(max_retry_num):
                res = func(*args, **kw)
                if res != not_expected_bool:
                    logging.info("    Get not expected return value %s", res)
                    break
                logging.info("    Return value %d was found, retry %d", res, i+1)
                time.sleep(retry_interval_sec)
            return res
        return wrapper
    return decorator
