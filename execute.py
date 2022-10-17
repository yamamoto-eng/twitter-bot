import sys

sys.dont_write_bytecode = True

import schedule
from time import sleep
from services.likes.addLike import addLike
from services.likes.deleteLike import deleteLike


def execute():
    addLike()
    deleteLike()


schedule.every(2).seconds.do(execute)


while True:
    schedule.run_pending()
    sleep(1)
