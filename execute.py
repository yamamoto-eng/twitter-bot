import sys

sys.dont_write_bytecode = True

import schedule
from time import sleep
import os
import datetime
from services.like.addLike import addLike
from services.like.deleteLike import deleteLike
from services.retweet.deleteRetweet import deleteRetweet


print("\n--------------------------------------------------")
print(
    "start",
    datetime.datetime.now().strftime("%H時%M分"),
    os.path.basename(__file__),
)
print("--------------------------------------------------\n")


def execute():
    addLike()
    deleteLike()
    deleteRetweet()


schedule.every(60).minutes.do(execute)


while True:
    schedule.run_pending()
    sleep(1)
