n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
for row in sorted(data, key=lambda x: x[k]):
    print(*row)
