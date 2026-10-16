from collections import Counter

s = input()
counts = Counter(s)
sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
for char, count in sorted_counts[:3]:
    print(char, count)
