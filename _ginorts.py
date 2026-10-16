s = input()
print(''.join(sorted(s, key=lambda x: (
    0 if x.islower() else
    1 if x.isupper() else
    2 if x.isdigit() and int(x) % 2 != 0 else
    3,
    x
))))
