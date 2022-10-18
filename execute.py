import sys

sys.dont_write_bytecode = True

import schedule
from time import sleep
from services.like.addLike import addLike
from services.like.deleteLike import deleteLike
from services.retweet.deleteRetweet import deleteRetweet


def execute():
    addLike()
    deleteLike()
    deleteRetweet()


schedule.every(1800).seconds.do(execute)


while True:
    schedule.run_pending()
    sleep(1)
