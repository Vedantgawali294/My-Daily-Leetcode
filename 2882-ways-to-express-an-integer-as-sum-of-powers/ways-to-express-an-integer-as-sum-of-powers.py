class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        powers = []
        num = 1
        while num ** x <= n:
            powers.append(num ** x)
            num += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for p in powers:
            for i in range(n, p - 1, -1):
                dp[i] = (dp[i] + dp[i - p]) % mod

        return dp[n]