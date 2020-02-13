# TinyRetry

## What is tiny_retry?
tinyretry is a python module that provides failure retry encapsulation for the target function

## Example
use python decorators syntax to wrap the call target
```
from tinyretry.tinyretry import UntilRetryForJson

@UntilRetryForJson(retry_code_key='errno', expected_err_code='0', max_retry_num = 10, retry_interval_sec = 0.1)
def DoHttpRequest():
    errno = random.randint(0,1)
    errmsg_arr = ['ok', 'err']
    return {
        "errno": errno,
        "errmsg": errmsg_arr[errno]
    }
```

## Retry type
- for json response
    - UntilRetryForJson
    - WhileRetryForJson
- for bool response
    - UntilRetryForBool
    - WhileRetryForBool