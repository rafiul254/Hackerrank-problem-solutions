m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
result = sorted(a.symmetric_difference(b))
for x in result:
    print(x)
