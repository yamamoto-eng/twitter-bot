import sys

sys.dont_write_bytecode = True

import schedule
from time import sleep
from services.likes.addLike import addLike
from services.likes.deleteLike import deleteLike


def execute():
    addLike()
    deleteLike()


schedule.every(600).seconds.do(execute)


# 03 イベント実行
while True:
    schedule.run_pending()
    sleep(1)
