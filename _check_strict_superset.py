a = set(map(int, input().split()))
n = int(input())
print(all(a > set(map(int, input().split())) for _ in range(n)))
