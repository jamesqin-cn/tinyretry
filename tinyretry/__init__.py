# -*- coding:utf-8 -*-
__author__ = 'james'

import logging
import functools
import time

# retry为了得到期望状态码
def UntilRetryForJson(retry_code_key, expected_err_code, max_retry_num = 3, retry_interval_sec = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for i in range(max_retry_num):
                logging.info("call UntilRetry(%s)(...)", func.__name__)
                res = func(*args, **kw)
                if retry_code_key in res and str(res[retry_code_key]) == str(expected_err_code):
                    break
                logging.info("Error code %s was found, retry %d", expected_err_code, i+1)
                time.sleep(retry_interval_sec)
            return res
        return wrapper
    return decorator

# retry为了不要返回指定错误码
def WhileRetryForJson(retry_code_key, not_expected_err_code, max_retry_num = 3, retry_interval_sec = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for i in range(max_retry_num):
                logging.info("call UntilRetry(%s)(...)", func.__name__)
                res = func(*args, **kw)
                if retry_code_key in res and str(res[retry_code_key]) != str(not_expected_err_code):
                    break
                logging.info("Error code %s was found, retry %d", not_expected_err_code, i+1)
                time.sleep(retry_interval_sec)
            return res
        return wrapper
    return decorator    

# retry为了得到期望状态码
def UntilRetryForBool(expected_bool, max_retry_num = 3, retry_interval_sec = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for i in range(max_retry_num):
                logging.info("call UntilRetry(%s)(...)", func.__name__)
                res = func(*args, **kw)
                if res == expected_bool:
                    break
                logging.info("Error code %d was found, retry %d", expected_bool, i+1)
                time.sleep(retry_interval_sec)
            return res
        return wrapper
    return decorator

# retry为了不要返回指定错误码
def WhileRetryForBool(not_expected_bool, max_retry_num = 3, retry_interval_sec = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for i in range(max_retry_num):
                logging.info("call UntilRetry(%s)(...)", func.__name__)
                res = func(*args, **kw)
                if res != not_expected_bool:
                    break
                logging.info("Error code %d was found, retry %d", not_expected_bool, i+1)
                time.sleep(retry_interval_sec)
            return res
        return wrapper
    return decorator

