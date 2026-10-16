# Run with Python 2
import re
n = int(raw_input())
for _ in range(n):
    try:
        re.compile(raw_input())
        print(True)
    except re.error:
        print(False)
