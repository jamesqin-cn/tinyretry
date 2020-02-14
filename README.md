# Tiny Retry

## What is TinyRetry?
tinyretry is a python module that provides failure retry encapsulation for the target function

## Programming Language
- python 2.7
- python 3.7

## Install
```
pip install tinyretry 
```

## Quick Start
use python decorators syntax to wrap the call target

### Case 1: retry until the return code equals to the special value
When we call the function and hope to get the special return code, then we can use `RetryUntilForJson` or `RetryUntilForBool`
```
from tinyretry import RetryUntilForJson

@RetryUntilForJson(retry_code_key='errno', expected_err_code=0, max_retry_num = 10, retry_interval_sec = 0.1)
def DoHttpRequest1():
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
```

Then you can get the return value from the function `DoHttpRequest1()` which must be successful, the call log like this:
```
bogon:tinyretry jamesqin$ python tinyretry_test.py
2020-02-14 14:03:14,754 - root - INFO - call RetryUntilForJson(DoHttpRequest)(...)
2020-02-14 14:03:14,754 - root - INFO -     Get expected error code 0
2020-02-14 14:03:14,754 - root - INFO - call RetryUntilForJson(DoHttpRequest)(...)
2020-02-14 14:03:14,754 - root - INFO -     Error code 2 was found, retry 1
2020-02-14 14:03:14,859 - root - INFO -     Get expected error code 0
2020-02-14 14:03:14,860 - root - INFO - call RetryUntilForJson(DoHttpRequest)(...)
2020-02-14 14:03:14,860 - root - INFO -     Error code 1 was found, retry 1
2020-02-14 14:03:14,964 - root - INFO -     Error code 1 was found, retry 2
2020-02-14 14:03:15,070 - root - INFO -     Error code 1 was found, retry 3
2020-02-14 14:03:15,172 - root - INFO -     Error code 2 was found, retry 4
2020-02-14 14:03:15,278 - root - INFO -     Get expected error code 0
2020-02-14 14:03:15,278 - root - INFO - call RetryUntilForJson(DoHttpRequest)(...)
2020-02-14 14:03:15,278 - root - INFO -     Error code 2 was found, retry 1
2020-02-14 14:03:15,381 - root - INFO -     Error code 1 was found, retry 2
2020-02-14 14:03:15,482 - root - INFO -     Error code 1 was found, retry 3
2020-02-14 14:03:15,586 - root - INFO -     Error code 1 was found, retry 4
2020-02-14 14:03:15,692 - root - INFO -     Error code 2 was found, retry 5
2020-02-14 14:03:15,794 - root - INFO -     Get expected error code 0
2020-02-14 14:03:15,794 - root - INFO - call RetryUntilForJson(DoHttpRequest)(...)
2020-02-14 14:03:15,794 - root - INFO -     Get expected error code 0
.
----------------------------------------------------------------------
Ran 1 test in 1.040s

OK
```

### Case 2: while the return code equals to the special value, we will retry
When we call the function and hope to skip the special return code, then we can use `RetryWhileForJson` or `RetryWhileForBool`
```
from tinyretry import RetryWhileForJson

@RetryWhileForJson(retry_code_key='errno', not_expected_err_code=2, max_retry_num = 10, retry_interval_sec = 0.1)
def DoHttpRequest2():
    errno = random.randint(0,2)
    errmsg_arr = ['ok', 'err-timeout', 'err-req-limit']
    return {
        "errno": errno,
        "errmsg": errmsg_arr[errno]
    }

class Test_TinyRetry(unittest.TestCase):
    def test_RetryWhileForJson(self):
        for i in range(5):
            res = DoHttpRequest2()
            self.assertNotEqual(res["errno"], 2)
```

then call log look like this:
```
2020-02-14 14:13:30,708 - root - INFO - call RetryWhileForJson(DoHttpRequest2)(...)
2020-02-14 14:13:30,708 - root - INFO -     Error code 2 was found, retry 1
2020-02-14 14:13:30,810 - root - INFO -     Error code 2 was found, retry 2
2020-02-14 14:13:30,912 - root - INFO -     Error code 2 was found, retry 3
2020-02-14 14:13:31,013 - root - INFO -     Error code 2 was found, retry 4
2020-02-14 14:13:31,117 - root - INFO -     Error code 2 was found, retry 5
2020-02-14 14:13:31,222 - root - INFO -     Get not expected error code 1
2020-02-14 14:13:31,222 - root - INFO - call RetryWhileForJson(DoHttpRequest2)(...)
2020-02-14 14:13:31,222 - root - INFO -     Get not expected error code 0
2020-02-14 14:13:31,222 - root - INFO - call RetryWhileForJson(DoHttpRequest2)(...)
2020-02-14 14:13:31,222 - root - INFO -     Error code 2 was found, retry 1
2020-02-14 14:13:31,324 - root - INFO -     Get not expected error code 0
2020-02-14 14:13:31,324 - root - INFO - call RetryWhileForJson(DoHttpRequest2)(...)
2020-02-14 14:13:31,324 - root - INFO -     Error code 2 was found, retry 1
2020-02-14 14:13:31,426 - root - INFO -     Error code 2 was found, retry 2
2020-02-14 14:13:31,529 - root - INFO -     Get not expected error code 1
2020-02-14 14:13:31,529 - root - INFO - call RetryWhileForJson(DoHttpRequest2)(...)
2020-02-14 14:13:31,529 - root - INFO -     Get not expected error code 1
```


## Other useful retry functions:
This package provide two scenarios of failure retries
- Until scene
    - RetryUntilForJson()
    - RetryUntilForBool()
- while scene
    - RetryWhileForJson()
    - RetryWhileForBool()