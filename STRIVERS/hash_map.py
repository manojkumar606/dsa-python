from collections import defaultdict
#freq_map = defaultdict(int)
#incoming_cargo = [10, 5, 10, 15, 10, 5]
#for i in incoming_cargo:
#    freq_map[i]+=1
#for key,value in freq_map.items():
#    print(key,value)

class solution:
    def frequency(self,arr,n):
        freq_map = defaultdict(int)
        for i in range(n):
            freq_map[arr[i]]+=1
        for key,value in freq_map.items():
            print(key,value)
    def highest_lowest_frequency(self,arr,n):
        freq_map = defaultdict(int)
        for i in range(n):
            freq_map[arr[i]]+=1
        min_freq = float('inf')
        max_freq = float(0)
        min_element,max_element = 0,0
        for key,value in freq_map.items():
            if value > max_freq:
                max_freq = value
                max_element = key
            if value < min_freq:
                min_freq = value
                min_element = key
        return min_element,min_freq,max_element,max_freq

obj = solution()
arr = [10, 5, 10, 15, 10, 5]
n = len(arr)
#obj.frequency(arr,n)
min_element,min_freq,max_element,max_freq = obj.highest_lowest_frequency(arr,n)
print(min_element,min_freq,max_element,max_freq)   