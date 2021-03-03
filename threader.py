import threading
import multiprocessing

threads = multiprocessing.cpu_count() * 2

def run_threads(target, arg_list):
    thread_list = [threading.Thread(target=target, args=(x,)) for x in arg_list]
    for x in thread_list: x.start()
    for x in thread_list: x.join()