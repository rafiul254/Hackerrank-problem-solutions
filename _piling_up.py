from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    blocks = deque(map(int, input().split()))
    possible = True
    prev = float('inf')
    while blocks:
        left = blocks[0]
        right = blocks[-1]
        if left >= right:
            if left <= prev:
                prev = left
                blocks.popleft()
            else:
                possible = False
                break
        else:
            if right <= prev:
                prev = right
                blocks.pop()
            else:
                possible = False
                break
    print("Yes" if possible else "No")
