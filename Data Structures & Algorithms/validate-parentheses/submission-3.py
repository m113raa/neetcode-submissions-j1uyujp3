class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashS = {
            "]" : "[",
            ")" : "(",
            "}" : "{",
        }
        for x in s:
            if x in hashS:
                if stack and hashS[x] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False



        