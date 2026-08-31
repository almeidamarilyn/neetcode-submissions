import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursneeded(v):
            return sum(math.ceil(pile/v)for pile in piles )

        lo,hi=1,max(piles)
        while lo<=hi:
            mid=(lo+hi)//2

            if hoursneeded(mid)<=h:
                val=mid
                hi=mid-1
            else:
                lo=mid+1

        return val