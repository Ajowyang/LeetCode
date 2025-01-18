class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        letter_set = set()
        while right < len(s):
            if s[right] not in letter_set:
                letter_set.add(s[right])
                max_len = max(len(letter_set), max_len)
                right += 1
            else:
                while s[right] in s[left:right]:
                    left += 1
                letter_set = set(list(s[left:right+1]))
                right += 1
            
        return max_len