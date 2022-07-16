import os
import time

from multiprocessing import Process

def long_time_task(i):

    print("son process:{}- task{}".format(os.getpid(),i))
    time.sleep(2)

    print("result: {}".format(8 ** 20))


if __name__ == "__main__":

    print("mother process: {}".format(os.getpid()))
    start = time.time()
    p1 = Process(target=long_time_task,args=(1,))
    p2 = Process(target=long_time_task,args=(2,))
    print("wait all of the son process complted")
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end = time.time()
    print("the time {}".format(end-start))