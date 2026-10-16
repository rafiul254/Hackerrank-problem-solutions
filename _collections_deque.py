from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'append':
        d.append(int(cmd[1]))
    elif cmd[0] == 'appendleft':
        d.appendleft(int(cmd[1]))
    elif cmd[0] == 'pop':
        d.pop()
    elif cmd[0] == 'popleft':
        d.popleft()
print(*d)
