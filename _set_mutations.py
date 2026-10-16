n = int(input())
s = set(map(int, input().split()))
t = int(input())
for _ in range(t):
    op, k = input().split()
    other = set(map(int, input().split()))
    if op == 'update':
        s.update(other)
    elif op == 'intersection_update':
        s.intersection_update(other)
    elif op == 'difference_update':
        s.difference_update(other)
    elif op == 'symmetric_difference_update':
        s.symmetric_difference_update(other)
print(sum(s))
