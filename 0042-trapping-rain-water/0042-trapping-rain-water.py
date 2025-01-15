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
                print(f'curr height(right): {height[right]}')
                print(f'min({high_left}, {high_right}) - {height[right]} = {min(high_left, high_right) - height[right]}')
                result += max(0, (min(high_left, high_right) - height[right] ))
                if height[right] > high_right:
                    high_right = height[right]
                    print('updating right max')
                right -= 1
            else:
                print(f'curr height(left): {height[left]}')
                print(f'min({high_left}, {high_right}) - {height[left]} = {min(high_left, high_right) - height[left]}')
                result += max(0, (min(high_left, high_right) - height[left] ))
                if height[left] > high_left:
                    high_left = height[left]
                    print('updating left max')
                left += 1

        return result    
