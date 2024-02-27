# thread: flow of execution. Separate order of instructions.
# cpu bound: task spends most of it's time waiting for internal events: cpu intensive, use multiprocessing.
# io bound: task spends most of it's time waiting for external events: user input/web scraping. use multithreading.
import threading
import time


def eat_breakfast():
    start_time = time.time()
    time.sleep(2)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"You finish breakfast. Time taken: {time_taken:.2f} seconds")


def drink_water():
    start_time = time.time()
    time.sleep(5)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"You are more hydrated. Time taken: {time_taken:.2f} seconds")


def study():
    start_time = time.time()
    time.sleep(8)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"You finish studying. Time taken: {time_taken:.2f} seconds")


def morning_ritual():
    x = threading.Thread(target=eat_breakfast, args=())
    y = threading.Thread(target=drink_water, args=())
    z = threading.Thread(target=study, args=())

    x.start()
    y.start()
    z.start()

    print(threading.active_count())  # 4 threads
    print(threading.enumerate())  # which threads

    x.join()
    y.join()
    z.join()
    # the joins ensure the program waits for all the threads to finish before continuing.

    print("You are prepared to leave.")
    print(time.perf_counter())  # time taken for all: >8 s as the main thread is not instant.


morning_ritual()
