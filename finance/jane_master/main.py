#!/usr/bin/python

# ~~~~~==============   HOW TO RUN   ==============~~~~~
# 1) Configure things in CONFIGURATION section
# 2) Change permissions: chmod +x bot.py
# 3) Run in loop: while true; do ./bot.py; sleep 1; done

from __future__ import print_function

import sys
import socket
import json

import time
from Queue import Queue

import adr
from bond import b_trade
import liquidity
import etf

# ~~~~~============== CONFIGURATION  ==============~~~~~
# replace REPLACEME with your team name!
team_name = "thetraders"
# This variable dictates whether or not the bot is connecting to the prod
# or test exchange. Be careful with this switch!
test_mode = True

# This setting changes which test exchange is connected to.
# 0 is prod-like
# 1 is slower
# 2 is empty
test_exchange_index = 0
prod_exchange_hostname = "production"

port = 25000 + (test_exchange_index if test_mode else 0)
exchange_hostname = "test-exch-" + team_name if test_mode else prod_exchange_hostname

# ~~~~~============== NETWORKING CODE ==============~~~~~


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((exchange_hostname, port))
    return s.makefile('rw', 1)


def write_to_exchange(exchange, obj):
    json.dump(obj, exchange)
    exchange.write("\n")


def read_from_exchange(exchange):
    return json.loads(exchange.readline())


# ~~~~~============== MAIN LOOP ==============~~~~~

def main():
    count = 0

    def connect_exchange():
        exchange = connect()
        write_to_exchange(exchange, {"type": "hello", "team": team_name.upper()})
        hello_from_exchange = read_from_exchange(exchange)
        # A common mistake people make is to call write_to_exchange() > 1
        # time for every read_from_exchange() response.
        # Since many write messages generate marketdata, this will cause an
        # exponential explosion in pending messages. Please, don't do that!
        print("The exchange replied:", hello_from_exchange)
        count = 0
        return exchange
    exchange = connect_exchange()
    bz_current = None
    goldman = None
    morgan = None
    wells = None
    net_bz, net_ez, order_id, bz = 0, 0, None, None
    while True:
        data = read_from_exchange(exchange)
        if data['type'] == 'close':
            sys.exit()
        # if data['type'] == 'book' and data['symbol'] == "VALE":
        #    liquidity.makeQueue(vale_e_queue, data, "VALE")
        if data['type'] == 'book' and data['symbol'] == 'BOND':
            trades = b_trade(data, count)
            count += len(trades)
            for t in trades:
                write_to_exchange(exchange, t)
                print(t)
        if data['type'] == 'book' and data['symbol'] == 'VALBZ' and data["sell"] and data["buy"]:
            bz_current = adr.bz_price(data)
#        if data['type'] == 'book' and data['symbol'] == 'MS' and data["sell"] and data["buy"]:
#            morgan = etf.etf_price(data, "MS")
#        if data['type'] == 'book' and data['symbol'] == 'WFC' and data["sell"] and data["buy"]:
#            wells = etf.etf_price(data, "WFC")
#        if data['type'] == 'book' and data['symbol'] == 'GS' and data["sell"] and data["buy"]:
#            goldman = etf.etf_price(data, "GS")
        if data['type'] == 'book' and data['symbol'] == 'VALE' and bz_current:
            trades = adr.adr_trade(data, bz_current, count)
            count += len(trades)
            for t in trades:
                write_to_exchange(exchange, t)
                print(t)
#        if data['type'] == 'book' and data['symbol'] == 'XLF' and goldman and wells and morgan:
#            trades = etf.etf_trade(data, goldman, wells, morgan, count)
#            count += len(trades)
#            for t in trades:
#                write_to_exchange(exchange, t)
#                print(t)
        if data['type'] == 'fill' and data["order_id"]:
            if data["dir"] == "BUY":
                if data["symbol"] == "VALE":
                    net_ez += data["size"]
                elif data["symbol"] == "VALBZ":
                    net_bz += data["size"]
            elif data["dir"] == "SELL":
                if data["symbol"] == "VALE":
                    net_ez -= data["size"]
                elif data["symbol"] == "VALBZ":
                    net_bz -= data["size"]
            print(data["dir"], data["symbol"], data["size"], net_bz, net_ez)
        if data["type"] == "ack" and data["order_id"] == order_id:
            print(data["type"])
            if bz:
                net_bz -= 10
                net_ez += 10
            else:
                net_bz += 10
                net_ez -= 10
        if net_ez == -net_bz and abs(net_ez) == 10:
            if net_ez < 0:
                convert_trade = {"type": "convert", "order_id": count,
                                 "symbol": "VALBZ", "dir": "SELL", "size": 10}
                bz = True
            elif net_ez > 0:
                convert_trade = {"type": "convert", "order_id": count,
                                 "symbol": "VALE", "dir": "SELL", "size": 10}
                bz = False
            order_id = count
            count += 1
            write_to_exchange(exchange, convert_trade)
            print(convert_trade)
        # if vale_e_queue.size() >= 5:
        #     average = liquidity.returnAverage5(queue)


if __name__ == "__main__":
    main()
