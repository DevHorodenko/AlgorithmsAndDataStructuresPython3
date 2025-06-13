from threading import Thread
import time

def myFunc(i):
    print('Starting thread %d' %i)
    time.sleep(5)
    print('Thread %d finished' %i)

for i in range(10):
    t = Thread(target=myFunc, args=(i,))
    t.start()