n = int(input())
nums = list(map(int, input().split()))
print(all(x > 0 for x in nums) and any(str(x) == str(x)[::-1] for x in nums))
