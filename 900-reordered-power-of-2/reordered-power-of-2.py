class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = {''.join(sorted(str(1 << i))) for i in range(31)}
        return ''.join(sorted(str(n))) in powers