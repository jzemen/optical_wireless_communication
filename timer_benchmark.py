#REMEMBER TO CHANGE PICKLE FILE NAME BETWEEN SETS.

import time
import datetime
import numpy as np
import matplotlib.pyplot as plot
import pickle

"""
I'm tired of hearing different sources give different figures for the precision
of a given timer function. This is an empirical attempt to benchmark 4 different
functions for our particular hardware setup and determine to what extent the 
communication speed is throttled by the timer function.

I'm also going to change the sleep length (10s, 1s, 0.1s, 0.01s and 0.001s)
to see whether these uncertainties
scale with time.

Note that by changing sleep length instead of range() we can simulate the effect
of having two sources of uncertainty (transmitter and receiver).
"""
snooze = 10

def timezzzz(snooze):
    t0 = time.perf_counter()
    for i in range(200):
        time.sleep(snooze)
    return(time.perf_counter()-t0) #recommended newest function. Python 3.3 onwards
    
def timezzz(snooze):
    t0 = datetime.datetime.now()
    for i in range(200):
        time.sleep(snooze)
    return(datetime.datetime.now()-t0) #returns a weird 'timedelta' object.
    
def timezz(snooze):
    t0 = time.clock()
    for i in range(200):
        time.sleep(snooze)
    return(time.clock()-t0) # A sensible choice normally, difficult to use with laser. 
    
 
def timez(snooze):
    t0 = time.time()
    for i in range(200):
        time.sleep(snooze)
    return(time.time()-t0) #The function we are currently using in receiverversion 4.0

a = np.array([timezzzz(snooze) for i in range(1000)])
print('method a is finished.')
bb = np.array([timezzz(snooze) for i in range(1000)])
b = np.array([time_x / datetime.timedelta(seconds=1) for time_x in xx])
print('method b is finished.')
c = np.array([timezz(snooze) for i in range(1000)])
print('method c is finished.')
d = np.array([timez(snooze) for i in range(1000)])
print('method d is finished.')

#and we're going to use pickle to save this data and make graphs etc.
# simply unpickle, then use plot.hist() for each dataset.

fid = open('comparing_time2e3.pkl','wb') #CHANGE PICKLE FILE NAME BETWEEN SETS = range*snooze!
pickle.dump(a, fid)
pickle.dump(b, fid)
pickle.dump(c, fid)
pickle.dump(d, fid)

fid.close()
