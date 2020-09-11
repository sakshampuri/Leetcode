from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        track = {}
        for item in nums:
            if item in track:
                return True
            track[item] = True
        return False

print(Solution().containsDuplicate([1,2,3,4,1]))