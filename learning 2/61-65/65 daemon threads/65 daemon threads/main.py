# daemon thread: thread that runs in the background, not important for program to run.
# program will wait for daemon threads to finish before exiting.
# non-daemon threads cannot normally be killed: stay alive until task done. EG: waiting for input, garbage collection.
import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for : " + str(count) + " seconds.")


x = threading.Thread(target=timer, daemon=True)
x.start()
# print(x.isDaemon())  # deprecated...?
answer = input("Exit? yes/no").strip().lower()

# x.setDaemon(True)


