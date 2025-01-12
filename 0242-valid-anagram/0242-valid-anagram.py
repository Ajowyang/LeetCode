class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        while len(list_s) > 0:
            char = list_s[0]
            if char in list_t:
                list_t.pop(list_t.index(char))
            else:
                return False
            list_s.pop(0)
        if len(list_s) != len(list_t):
            return False
        return True