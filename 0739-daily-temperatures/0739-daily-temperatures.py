class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]
        stack = [[temperatures[-1], len(temperatures)-1]]
        for i in range(len(temperatures) - 2 , -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                    stack.pop()
                #else:
                #    break
            res = (stack[-1][1] - i) if len(stack) >= 1 else 0
            results.insert(0, res)
            stack.append([temperatures[i], i])
        return results