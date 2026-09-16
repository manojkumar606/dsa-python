class Solution:
    def reverse(self, arr: list, n: int) -> None:
        left = 0
        right = n-1
        while left < right:
            arr[left],arr[right] = arr [right],arr[left]
            left+=1 
            right-=1 
            
sol_Inst = Solution()
my_list = [1,2,3]
list_length = len(my_list)
sol_Inst.reverse(my_list,list_length)
print(my_list)