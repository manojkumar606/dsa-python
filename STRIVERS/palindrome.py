class Solution:
    def palindrome(self,i,s):
        if i>=len(s)//2:
            return True
        if s[i]!=s[len(s)-i-1]:
            return False
        return self.palindrome(i+1,s)
            
sol_Inst = Solution()
word = "madam"
print(sol_Inst.palindrome(0,word))
