from collections import OrderedDict

n = int(input())
d = OrderedDict()
for _ in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(len(d))
print(*d.values())
