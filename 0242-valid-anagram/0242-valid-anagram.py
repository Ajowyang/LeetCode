class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in dict:
                print('not in')
                return False
            else:
                dict[t[i]] -= 1
                if dict[t[i]] < 0:
                    return False
        return True