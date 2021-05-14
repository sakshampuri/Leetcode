'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

'''
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i]!=nums[i-1]):
                start = i+1
                end = len(nums)-1
                reqSum = -nums[i]
                while start < end:
                    curSum = nums[start] + nums[end]
                    if curSum == reqSum:
                        result.append([nums[start], nums[end], nums[i]])
                        while start < end and nums[start] == nums[start+1]:
                            start+=1
                        while start < end and nums[end] == nums[end-1]:
                            end-=1
                        start+=1
                        end-=1
                    elif curSum < reqSum:
                        start+=1
                    else:
                        end-=1
        return result

l = [-1,0,1,2,-1,-4]
print(Solution().threeSum(l))