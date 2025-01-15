class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstack = []
        operatorstack = []

        for token in tokens:
            if token[0] == "-" and token[1:len(token)].isdigit():
                numstack.append(int(token))
                #print(f'numstack: {numstack}')
            elif token.isdigit():
                numstack.append(int(token))
                #print(f'numstack: {numstack}')
            elif token.isdigit() == False:
                operatorstack.append(token)
                #print(f'opstack: {operatorstack}')
                sec = numstack.pop()
                first = numstack.pop()
                match token:
                    case "+":
                        numstack.append(first + sec)
                        operatorstack.pop()
                        #print(f'numstack: {numstack}')
                    case "-":
                        numstack.append(first - sec)
                        operatorstack.pop()
                        #print(f'numstack: {numstack}')
                    case "*":
                        numstack.append(first * sec)
                        operatorstack.pop()
                        #print(f'numstack: {numstack}')
                    case "/":
                        numstack.append(int(first / sec))
                        operatorstack.pop()
                        #print(f'numstack: {numstack}')
        
        return int(numstack[0])
        