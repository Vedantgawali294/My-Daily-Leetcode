class Solution:
    def mySqrt(self, x: int) -> int:
        lp = 0
        rp = x
        while lp <= rp:
            mid = (lp + rp) // 2
            if mid ** 2 <= x < ((mid+1)**2):
                return mid
            elif mid ** 2 < x:
                lp = mid + 1
            else:
                rp = mid - 1
        return 1
        