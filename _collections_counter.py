from collections import Counter

n = int(input())
shoes = Counter(map(int, input().split()))
customers = int(input())
earnings = 0
for _ in range(customers):
    size, price = map(int, input().split())
    if shoes[size] > 0:
        earnings += price
        shoes[size] -= 1
print(earnings)
