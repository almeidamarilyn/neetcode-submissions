class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        c=['+','-','*','/']
        for i in tokens:
            if i in c:
                a=stack.pop()
                b=stack.pop()
                if i=='+':
                    value=a+b
                elif i=='-':
                    value=b-a
                elif i=='*':
                    value=a*b
                elif i=='/':
                    value=int(b/a)
                stack.append(value)
            else:
                stack.append(int(i))
        return stack.pop()