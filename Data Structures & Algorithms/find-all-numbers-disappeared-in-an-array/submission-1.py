class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        myset=set(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if i not in myset:
                res.append(i)

        return res