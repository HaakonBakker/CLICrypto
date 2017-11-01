# CLI Crypto
A Simple Python script that will show the price and the changes for defined cryptocurrencies.

# I want to change which coins to follow!
Change coinlist.txt (one coin/token for each line).

# Command Line Arguments
```sh
Usage: CryptoMarkets.py [options]

Options:
  -h, --help            show this help message and exit
  -c CUR, --cur=CUR     Choose which currency you want to convert to
  -u UPD, --upd=UPD     Choose the update interval (seconds)
  -v VERBOSE, --verbose=VERBOSE
                        Will print more info in the table
```

# How to run
```sh
python3 CryptoMarkets.py
```

# Volumes show 0 on some coins
This is a limitation in the API, not every coin will have a volume connected in each currency.
