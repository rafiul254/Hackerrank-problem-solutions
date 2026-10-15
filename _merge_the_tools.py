def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        substring = string[i:i+k]
        seen = []
        for char in substring:
            if char not in seen:
                seen.append(char)
        print(''.join(seen))

if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)
