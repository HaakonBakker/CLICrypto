#!/usr/local/bin/python
# This is the script that will show the Crypto Markets.
import requests
import time
import os
from prettytable import PrettyTable
from CryptoGetter import CryptoGetter

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

UPDATEINTERVAL = 1
BASEURL = "https://min-api.cryptocompare.com/data/pricemultifull"

COINLIST = ["BTC", "ETH", "DASH", "XRP", "GNT", "LTC", "BAT"]
TOLIST = ["USD", "NOK", "BTC"]


def printCryptoTable():
    getter = CryptoGetter(COINLIST, BASEURL, TOLIST)

    coinInfo = getter.getCoinInfo()
    coinInfoen = dict(coinInfo)

    coinDisplay = coinInfo["DISPLAY"]
    coinRaw = coinInfo["RAW"]

    #t = PrettyTable(["Pair", "Price", "High 24H", "Low 24H", "Change 24H", "24H %", "Volume", "Mkt. Cap"])
    t = PrettyTable(["Pair", "Price", "High 24H", "Low 24H", "Change 24H", "Δ 24H %"])
    t.align["Price"] = "r"
    t.align["High 24H"] = "r"
    t.align["Low 24H"] = "r"
    t.align["Change 24H"] = "r"
    t.align["Δ 24H %"] = "r"
    t.align["Volume"] = "l"
    t.align["Mkt. Cap"] = "l"
    for coin in coinDisplay:
        # Get pair

        pair = coin + "/" + TOLIST[0]
        price = coinDisplay[coin][TOLIST[0]]["PRICE"]
        price24HHigh = coinDisplay[coin][TOLIST[0]]["HIGH24HOUR"]
        price24HLow = coinDisplay[coin][TOLIST[0]]["LOW24HOUR"]
        change24H = coinDisplay[coin][TOLIST[0]]["CHANGE24HOUR"]


        # Check if the change was positive or negative
        change24HPCT = "0 %"

        if coinRaw[coin][TOLIST[0]]["CHANGEPCT24HOUR"] > 0:
            change24HPCT = bcolors.OKGREEN + coinDisplay[coin][TOLIST[0]]["CHANGEPCT24HOUR"] + " %" + bcolors.ENDC
        else:
            change24HPCT = bcolors.FAIL + coinDisplay[coin][TOLIST[0]]["CHANGEPCT24HOUR"] + " %" + bcolors.ENDC
        volume = coinDisplay[coin][TOLIST[0]]["VOLUMEDAY"]
        mktCap = coinDisplay[coin][TOLIST[0]]["MKTCAP"]

        t.add_row([pair, price, price24HHigh, price24HLow, change24H, change24HPCT])
        #t.add_row([pair, price, price24HHigh, price24HLow, change24H, change24HPCT, volume, mktCap])

    os.system('clear')
    print(t)
    print("Last updated", time.strftime("%H:%M:%S"))

wantToCont = True
while wantToCont:
    printCryptoTable()
    time.sleep(1)
