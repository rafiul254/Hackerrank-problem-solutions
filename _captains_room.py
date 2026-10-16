from collections import Counter

k = int(input())
rooms = list(map(int, input().split()))
counts = Counter(rooms)
for room, count in counts.items():
    if count % k != 0:
        print(room)
