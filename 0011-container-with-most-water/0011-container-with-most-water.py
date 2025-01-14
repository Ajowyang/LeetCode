class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > result:
                print(f'{(right - left)} * {max(height[left], height[right])} = {area}')
                result = area
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else: 
                left += 1
        return result