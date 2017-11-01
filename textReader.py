def linesToList(filename):
    with open(filename) as file:
        coinList = []
        for line in file:
            coinList.append(line.strip())
        return coinList
    return []
