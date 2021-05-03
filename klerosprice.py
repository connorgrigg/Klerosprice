#!/bin/python
import requests
import json
import os
# counts lines in file
def count_lines(file):
    line_count = 0
    for i in file:
        if i != '\n':
            line_count += 1
    return line_count

# accesses data from coingecko API
url = 'https://api.coingecko.com/api/v3/simple/price?ids=kleros&vs_currencies=usd'
data = requests.get(url).json()
# writes old lookups to file for comparison
w = open("pricehistory.txt", "a+")
w.write(str(data['kleros']['usd']))
w.write('\n')
w.close()
w = open("pricehistory.txt", "r")
contents = w.readlines()
w.close()
# if price history gets too long, deletes
line_count = count_lines(contents)
if line_count > 100:
    os.remove("pricehistory.txt")
# arranges data for printing
previousdata = float(contents[line_count - 2])
current = data['kleros']['usd']
change = current - float(previousdata)
change = round(change, 5)
percent_change = round(((change/current) * 100), 6)
# prints 
print("Current Kleros price:", current, "USD")
print("Previous Kleros price:", previousdata, "USD")
print("Difference: ", change, "USD")
print("Percent difference:", percent_change, "%")
