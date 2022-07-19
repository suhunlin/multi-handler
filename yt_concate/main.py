import math
import time

from multi_handler.yt_multi_threading import YTMultithreading
from multi_handler.yt_multi_processing import YTMultiprocessing


def no_arguments_func():
    for num in range(1, 10000):
        print(num, 'sqrt:', math.sqrt(num))


def one_arguments_func(*args):
    print('one_arguments_func')
    for item in args:
        print(item, 'sqrt:', math.sqrt(item))


def main():
    iterable_data = [num for num in range(1, 10000)]
    start_time = time.time()
    # yt_thread.run_thread(target=no_arguments_func)
    # yt_thread.run_thread(target=one_arguments_func, iterable_data)

    # yt_thread = YTMultithreading()
    # yt_thread.run_thread(one_arguments_func, iterable_data)
    yt_process = YTMultiprocessing()
    yt_process.run_process(one_arguments_func, iterable_data)
    end_time = time.time()
    print('Total cost time: ', end_time - start_time)

if __name__ == '__main__':
    main()
