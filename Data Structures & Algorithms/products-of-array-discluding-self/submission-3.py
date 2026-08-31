class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res
        
        
        # prod=1
        # nums2=[1]*len(nums)
        # for i in range(len(nums)):
        #     prod*=nums[i]
        # for i in range(len(nums)):
        #     nums2[i]=prod/nums[i]
        # ints = [int(x) for x in nums2]
        # return ints






        # nums2=[0]*len(nums)
        # for i in range(len(nums)):
        #     prod=1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         else:
        #             prod*=nums[j]
        #     nums2[i]=prod
        # return nums2