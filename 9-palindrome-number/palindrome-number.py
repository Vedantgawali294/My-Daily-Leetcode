class Solution:
    def isPalindrome(self, x: int) -> bool:
        i=x
        rev=0
        while i>0:
            rev=(rev*10)+(i%10)
            i=i//10
        
        return x==rev
            
