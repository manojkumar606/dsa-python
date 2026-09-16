s = input().strip()
print(s)
hash_arr = [0] *256

for char in s:
    hash_arr[ord(char)] += 1

q = int(input())

for _ in range(q):
    char = input()
    print(hash_arr[ord(char)])