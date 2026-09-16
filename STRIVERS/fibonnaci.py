class Solution:
    def fibonnaci(self,n):
        last=1 
        second_last=0
        print(second_last, last, end=" ")
        for i in range(2,n+1):
            cur = last + second_last
            second_last = last
            last = cur
            print(cur,end=" ")
            
        
            
sol_Inst = Solution()
sol_Inst.fibonnaci(10)


