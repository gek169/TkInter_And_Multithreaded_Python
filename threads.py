#!/usr/bin/python
import thread
import time
def worker( threadName, delay):
    i = 0
    while i < 500:
        i+=1
        time.sleep(delay)
        print "%s : %s" % ( threadName, time.ctime(time.time()) )

try:
    thread.start_new_thread(worker, ("T1",2,))
    thread.start_new_thread(worker, ("T2",5,))
except:
    print "Can't start threads?"
while 1:
    pass