#!/usr/bin/env python

import threading
import time

## time.sleep(1)  --> to sleep the program for 1 secs

def myfunction(n):
    print "Start a thread:", n
    time.sleep(3)
    print "End a thread:", n

threads = []

# We want 5 instances of the function to be executed at the same time
th1 = threading.Thread(target = myfunction,args="1")  ### Creating a thread object
th2 = threading.Thread(target = myfunction,args="2")
th3 = threading.Thread(target = myfunction,args="3")
th4 = threading.Thread(target = myfunction,args="4")
th5 = threading.Thread(target = myfunction,args="5")
th1.start();th2.start();th3.start();th4.start();th5.start()  ## To start the thread  
th1.join();th2.join();th3.join();th4.join();th5.join()

# for th in threads:
#     th.join()   ## join method for threading class Waits for thread to terminate


# ### Now normal function calling
# for i in range(5):
#     myfunction(i)  ## This will take 15 secs to run
        


    