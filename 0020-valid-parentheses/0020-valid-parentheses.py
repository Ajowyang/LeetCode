class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            print(char)
            match char:
                case ('[' | '{' | '('):
                    stack.append(char)
                    continue
                case ']':
                    if len(stack) > 0 and stack[len(stack)-1] == '[':
                        stack.pop()
                        continue
                    else: 
                        return False
                case ')':
                    if len(stack) > 0 and stack[len(stack)-1] == '(':
                        stack.pop()
                        continue
                    else: 
                        return False
                case '}':
                    if len(stack) > 0 and stack[len(stack)-1] == '{':
                        stack.pop()
                        continue
                    else: 
                        return False           
        return (True if len(stack) == 0 else False)