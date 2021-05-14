class Solution:
    def maxArea(self, height):
        # basically finding largest l and b
        # l is distance between indices and b the value a(i)
        # staring from both ends and optimizing accordignly
        start, end, area = 0, len(height)-1, 0
        while start < end:
            if height[start] < height[end]:
                area = max(area, height[start]*(end-start))
                start += 1
            else:
                area = max(area, height[end]*(end-start))
                end -= 1
        return area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

