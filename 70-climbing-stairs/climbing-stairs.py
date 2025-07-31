class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a, b = 1, 2  # base cases: 1 way to reach step 1, 2 ways for step 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b