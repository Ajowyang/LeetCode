class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = [[temperatures[len(temperatures) - 1], len(temperatures)-1]]
        for i in range(len(temperatures) - 2 , -1, -1):
            print(temperatures[i])
            while len(stack) >= 1:
                if temperatures[i] >= stack[len(stack) - 1][0]:
                    stack.pop()
                else:
                    break
            if stack:
                results[i] += (stack[len(stack)-1][1] - i) 
            
            stack.append([temperatures[i], i])

        return results