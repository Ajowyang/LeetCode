class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = {}
        result = 0
    #windowLen - count[mostCommonChar] = numCharsToReplace
    #<= k True? then valid

        for right in range(0, len(s)):
            #update character count
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
            if ((right + 1 - left) - max(count.values()) ) <= k:
                result = max(result, (right + 1 - left))
            else:
                count[s[left]] -= 1
                left += 1
           
        return result 






        