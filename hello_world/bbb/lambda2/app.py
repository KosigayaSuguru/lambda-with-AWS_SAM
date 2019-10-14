import json

import hoge
from . import main


def lambda_handler(event, context):
    print("aaaaa")
    main.main2()
    a = 0
    while a <= 10:
        print("looping")
        hoge.hoge()
        import time
        time.sleep(4)
        a += 4
        print(a, a, a)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
