# Find the index of the first occurrence in a string
Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
## Python
We set the length of needle and start traveling haystack until we found it.

1. Set two pointers: one will start at cero, the other will start at `len(0)`.
2. Increase the pointers until we find the first occurrence.
3. If the second pointer reach the end of the string there is no occurrence.
**Time Complexity:** *O(n)*, where n is the length of the s.

**Space Complexity:** *O(n)*, as we use anly the given array and some variables.
```python []
class Solution(object):
    #:type haystack: str
    #:type needle: str
    #:rtype: int
    def strStr(self, haystack, needle):
        flag = True
        k = len(needle)
        l = len(haystack)
        c = 0

        while flag and k<=l:
            if haystack[c:k] == needle:
                flag = False
            else:
                c+=1
                k+=1
        if k>l:
            c = -1
        
        return c
```
