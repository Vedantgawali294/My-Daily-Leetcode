class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        i=n
        sum=0
        prod=1
        rev=0
        while i>0:
            prod=prod*(rev*10+i%10)
            sum=sum+(rev*10+i%10)
            i=i//10
            
        return prod-sum    

            