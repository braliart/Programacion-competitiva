# Valid Parentheses
Problema: https://leetcode.com/problems/valid-parentheses/description/
## Python
### Stack solution
Complexity O(n) (I think)
1. We do a dict where the keys are the front parentheses and the values are the back parentheses, a stack to operate and a flag to check if it is valid.
2. We do a global while to advance within the chars of the string.
3. Within the first while there are two whiles, one will push all the front parentheses "(,{,[". The second while will take the current word and pop the top parentheses to check if they correspond or not.
4. If at any point the stack is empty and the current char is a back parentheses "),],}" the string is invalid.
5. At the stack needs to be empty for it to be valid.
```Python
class Solution(object):
    #:type s: str
    #:rtype: bool
    def isValid(self, s):
        flag = True
        stack = []
        repo = {"[":"]","{":"}","(":")"}
        c = 0

        while c<len(s) and flag:
            while c<len(s) and s[c] in repo:
                stack.append(s[c])
                c+=1
            while c<len(s) and s[c] not in repo and flag:
                if len(stack)==0 or s[c] not in repo[stack.pop()]:
                    flag = False
                c+=1
        if len(stack)>0:
            flag = False

        return flag
```
