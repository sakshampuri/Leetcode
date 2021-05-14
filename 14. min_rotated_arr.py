class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        # sorted case
        if nums[start] <= nums[end]:
            return nums[start]

        while (end - start > 1):
            middle = int((start+end)/2)
            if nums[middle] > nums[start]:
                start = middle
            else:
                end = middle
        return nums[end]
