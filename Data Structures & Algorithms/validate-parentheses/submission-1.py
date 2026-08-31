class Solution:
    def isValid(self, s: str) -> bool:
        hash={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:
            if i not in hash:
                stack.append(i)
            else:
                if not stack:
                    return False
                if hash[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True   
        else: return False