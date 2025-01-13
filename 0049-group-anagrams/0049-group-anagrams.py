class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in range(0, len(strs)):
            sort_str = ''.join(sorted(strs[i]))
            if sort_str not in dict:
                dict[sort_str] = [strs[i]]
            else:
                dict[sort_str].append(strs[i])
        result = []
        for key, value in dict.items():
            result.append(value)
        return(result)  