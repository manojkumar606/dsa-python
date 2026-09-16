n = int(input()) # number of elements
arr = list(map(int,input().split())) # array of elements
hash_arr = [0]*13 # hash array
for i in range(n): 
    hash_arr[arr[i]] += 1 # incrementing the hash array at the index of the element
q = int(input()) # number of queries
for _ in range(q):
    query = int(input())
    print(hash_arr[query])