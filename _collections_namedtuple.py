from collections import namedtuple

n = int(input())
fields = input().split()
Student = namedtuple('Student', fields)
total = 0
for _ in range(n):
    s = Student(*input().split())
    total += int(s.MARKS)
print("{:.2f}".format(total/n))
