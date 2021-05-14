class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algo
        local, glob = nums[0], nums[0]
        for i in nums[1:]:
            local = max(i, i+local)
            glob = local if local > glob else glob
        return glob
        