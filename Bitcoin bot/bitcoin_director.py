"""
Created on Mon Jan 30 20:20:47 2017

@author: Jarrod
"""
import time
import analysiskraken
import Kraken
import numpy
between_time = 30

# for x in range(10):
#     now = time.time()
#     next_time = now + between_time
#     Kraken.price_getter()
#     time.sleep(next_time - time.time())
while True:
    now = time.time()
    next_time = now + between_time
    Kraken.price_getter()
    time.sleep(5)
    analysiskraken.decision_maker()
    time.sleep(next_time - time.time())



