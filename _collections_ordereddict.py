from collections import OrderedDict

n = int(input())
d = OrderedDict()
for _ in range(n):
    line = input().rsplit(' ', 1)
    item = line[0]
    price = int(line[1])
    if item in d:
        d[item] += price
    else:
        d[item] = price
for item, price in d.items():
    print(item, price)
