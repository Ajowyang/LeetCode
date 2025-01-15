class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        high_left = 0
        high_right = 0
        #each space scores min(side_max) - height
        while left <= right:
            if high_left > high_right:
                
                result += max(0, (min(high_left, high_right) - height[right] ))
                if height[right] > high_right:
                    high_right = height[right]
                  
                right -= 1
            else:
                
                result += max(0, (min(high_left, high_right) - height[left] ))
                if height[left] > high_left:
                    high_left = height[left]
                    
                left += 1

        return result    
