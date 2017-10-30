#!/usr/local/bin/python
# This class will make requests to the API and get all the prices in a nice dict format
import requests
class CryptoGetter:
    def __init__(self, coinlist, baseurl, tolist):
        self.coinlist = coinlist
        self.baseurl = baseurl
        self.tolist = tolist
        pass

    def _makeRequest(self, url):
        """ Will return the json object (dict) of the URL """
        # Perform get Requests
        r = requests.get(url)
        tickerInfo = r.json()
        return tickerInfo


    def getCoinInfo(self):
        return self._makeRequest(self._getRequestURL())


    def _getRequestURL(self):
        requestUrl = self.baseurl
        # Defining the from symbols
        requestUrl = requestUrl + "?fsyms="
        for coin in self.coinlist:
            requestUrl = requestUrl + coin + ","

        # Defining the to symbols
        requestUrl = requestUrl + "&tsyms="
        for toCoin in self.tolist:
            requestUrl = requestUrl + toCoin + ","

        return requestUrl
