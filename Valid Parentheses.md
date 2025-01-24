# Valid Parentheses
Problema: https://leetcode.com/problems/valid-parentheses/description/
## Python
### Stack solution
**Time Complexity:** *O(n)*, where n is the length of the string. Each character is processed once.

**Space Complexity:** *O(n)*, as the stack may store all the characters in the worst case (e.g., all opening brackets).
1. We do a dict where the keys are the front parentheses and the values are the back parentheses, a stack to operate and a flag to check if it is valid.
2. If the char is "[,{,(" it will be pushed into the stack, if not then the top char will be popped from the stack to see if it matches.
3. If at any point the stack is empty and the current char is a back parentheses "),],}" the string is invalid.
4. At the stack needs to be empty for it to be valid.
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
            if s[c] in repo:
                stack.append(s[c])
            elif len(stack)==0 or s[c] not in repo[stack.pop()]:
                flag = False
            c+=1
        if len(stack)>0:
            flag = False

        return flag
```
## C++
### Stack Solution
Same complexity and intuition, but here it beats 100%.

Diferences: stack.pop() is a void method, to access the top element in the stack I need to use stack.top()
```C++
class Solution {
public:
    bool isValid(string s) {
        bool flag = true;
        int c = 0;
        stack<char> stack;
        unordered_map<char,char> map;
        map['{']='}';
        map['[']=']';
        map['(']=')';

        while(c<s.size() && flag) {
            if(map.contains(s[c])) {
                stack.push(s[c]);
            } else {
                if(stack.empty() || map[stack.top()]!=s[c]) {
                    flag = false;
                } else {
                    stack.pop();
                }
            }
            c++;
        }
        if(!stack.empty()) {
            flag = false;
        } 
        return flag;
    }
};
```
