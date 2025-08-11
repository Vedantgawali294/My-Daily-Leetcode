from typing import List
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = []
        power = 1
        while n > 0:
            if n & 1:
                powers.append(power)
            power <<= 1
            n >>= 1
        
        prefix = [1]
        for p in powers:
            prefix.append((prefix[-1] * p) % MOD)
        
        result = []
        for left, right in queries:
            val = prefix[right + 1] * pow(prefix[left], MOD - 2, MOD) % MOD
            result.append(val)
        
        return result