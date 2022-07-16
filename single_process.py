import time
import os


def long_time_task():

    print("current process: {}".format(os.getpid()))
    time.sleep(2)

    print("result: {}".format(8 ** 20))

if __name__ == "__main__":

    print("mother process: {}".format(os.getpid()))

    start = time.time()

    for i in range(2):

        long_time_task()

    end = time.time()

    print("duration{}s".format(end - start))

