# -*- encoding: utf-8 -*-
# Author: li_colin

import multiprocessing
from loguru import logger

process_cnt = multiprocessing.cpu_count() - 1


def f(q, s):
    logger.info("xxxx " + str(s))
    q.put(s * 10)


if __name__ == '__main__':

    processes = []
    queue = multiprocessing.Queue()
    for n in range(process_cnt):
        logger.add(
            "info.log",
            colorize=True,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> {process} [{level}] {name} - <level>{message}</level>",
            level='INFO', enqueue=False)
        p = multiprocessing.Process(target=f, args=(queue, str(n),))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    while not queue.empty():
        obj = queue.get()
        print(obj)
    print("end")
