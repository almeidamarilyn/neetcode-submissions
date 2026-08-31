class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1={}     
        for i,val in enumerate(nums):
            complement=target-val
            if complement in hash1:
                return [hash1[complement],i]
            hash1[val]=i       