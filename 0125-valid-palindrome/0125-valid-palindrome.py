class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ''.join(char for char in s if char.isalnum()).lower()
        result = True
        left = 0
        right = len(check)-1
        while left < right:
            if check[left] != check[right]:
                result = False
            left += 1
            right -= 1
        return result
        