#!/usr/bin/env python

import threading
import time

## time.sleep(1)  --> to sleep the program for 1 secs

def myfunction():
    print "Start a thread"
    time.sleep(3)
    print "End a thread"

threads = []

# We want 5 instances of the function to be executed at the same time

for i in range(5):
    th = threading.Thread(target = myfunction)  ### Creating a thread object
    th.start()  ## To start the thread  
    threads.append(th)

for th in threads:
    th.join()   ## join method for threading class Waits for thread to terminate


### Now normal function calling
for i in range(5):
    myfunction()  ## This will take 15 secs to run
        


    