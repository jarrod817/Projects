# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:28:27 2017

@author: Jarrod
"""
import krakenex
import time
import datetime
import sqlite3
conn = sqlite3.connect("bitcoinprices.db")
cur = conn.cursor()
k = krakenex.API()
k.load_key('krakenkey.txt')


def price_getter():
    ind = 0
    try:
        cur.execute('''SELECT strftime('%s')''')
        timestamp = cur.fetchone()
        price = k.query_public('Ticker', {"pair": "XXBTZUSD"})
        ask = price["result"]["XXBTZUSD"]["a"][0]
        bid = price["result"]["XXBTZUSD"]["b"][0]
        # balance=k.query_private('Balance')
        cur.execute('INSERT INTO btcprices (bid, ask, time, ind) VALUES (?,?,?,?)',
                    (bid, ask, timestamp[0], ind))
        conn.commit()
        ind += 1
        print("received at:", timestamp[0], ask)
        #print (balance["result"])
        # time.sleep(next_time-time.time())
    except:
        print("failed to get price at", timestamp[0])
        price_getter()

# Selling get bid price, buying get ask price
#<pair_name> = pair name
#    a = ask array(<price>, <whole lot volume>, <lot volume>),
#    b = bid array(<price>, <whole lot volume>, <lot volume>),
#    c = last trade closed array(<price>, <lot volume>),
#    v = volume array(<today>, <last 24 hours>),
#    p = volume weighted average price array(<today>, <last 24 hours>),
#    t = number of trades array(<today>, <last 24 hours>),
#    l = low array(<today>, <last 24 hours>),
#    h = high array(<today>, <last 24 hours>),
#    o = today's opening price
