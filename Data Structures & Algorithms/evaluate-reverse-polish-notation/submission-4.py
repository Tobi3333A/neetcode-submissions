class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sdk = []
        for i in tokens:
            if i not in '+-*/':
                sdk.append(int(i))
            else:
                a = int(sdk.pop())
                b = int(sdk.pop())
                if i == '+':
                    sdk.append(a+b)
                elif i == '-':
                    sdk.append(b-a)
                elif i == '*':
                    sdk.append(a*b)
                else:
                    sdk.append(int(b/a))
        return sdk.pop()
