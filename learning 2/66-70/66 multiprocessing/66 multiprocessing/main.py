# multiprocessing: running tasks in parallel on different cores. bypasses GIL(global interpreter lock)
# multithreading: better for io bound tasks(waiting)
# multiprocessing: better for CPU bound tasks(heavy cpu usage)
from multiprocessing import cpu_count, Process
import time


def main():
    print(cpu_count())

    start_time = time.perf_counter()

    a = Process(target=counter, args=(500000000 / 6,))
    b = Process(target=counter, args=(500000000 / 6,))
    c = Process(target=counter, args=(500000000 / 6,))
    d = Process(target=counter, args=(500000000 / 6,))
    e = Process(target=counter, args=(500000000 / 6,))
    f = Process(target=counter, args=(500000000 / 6,))
    g = Process(target=counter, args=(500000000 / 6,))
    h = Process(target=counter, args=(500000000 / 6,))
    i = Process(target=counter, args=(500000000 / 6,))
    j = Process(target=counter, args=(500000000 / 6,))
    k = Process(target=counter, args=(500000000 / 6,))
    l = Process(target=counter, args=(500000000 / 6,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    k.start()
    l.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    i.join()
    j.join()
    k.join()
    l.join()

    end_time = time.perf_counter()
    print("Finished in : ", end_time - start_time, " seconds")  # is not directly proportional to threads... hmm.


def counter(num):
    count = 0
    while count < num:
        count += 1


if __name__ == "__main__":
    main()
