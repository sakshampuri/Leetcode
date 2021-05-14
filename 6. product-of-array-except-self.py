class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        o = [1]*len(nums)
        for i in range(1, len(nums)):
            o[i] = o[i-1]*nums[i-1]
        b = 1
        for i in reversed(range(len(nums))):
            o[i] = o[i]*b
            b *= nums[i]
        return o

