n, x = map(int, input().split())
scores = [list(map(float, input().split())) for _ in range(x)]
for student in zip(*scores):
    print(sum(student) / x)
