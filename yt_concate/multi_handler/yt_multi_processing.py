import os

from multiprocessing import Process


class YTMultiprocessing:
    def run_process(self, target, *args, **kwargs):
        processes = []
        tuple_data = ()

        if not args:
            print("args: tuple is empty")
        else:
            tuple_data = self.data_equal_parts_by_num(os.cpu_count(), args[0])
        if not kwargs:
            print('kwargs: dictionary is empty')

        for core in range(os.cpu_count()):
            # print('total thread num:', os.cpu_count(), 'thread:', core, 'create')
            if not tuple_data:
                processes.append(Process(target=target))
            else:
                processes.append(Process(target=target, args=tuple_data[core]))

        for process in processes:
            process.start()

        for process in processes:
            process.join()

    def data_equal_parts_by_num(self, threads_num, iterable_data):
        item_num = len(iterable_data) / threads_num
        if len(iterable_data) % threads_num != 0:
            item_num += 1
        item_num = int(item_num)
        print('item_num:', item_num)
        return [iterable_data[i:i + item_num] for i in range(0, len(iterable_data), item_num)]
