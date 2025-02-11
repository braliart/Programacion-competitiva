# Find the index of the first occurrence in a string
Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
## Python
We set the length of needle and start traveling haystack until we found it.

1. Set two pointers: one will start at cero, the other will start at `len(needle)`.
2. Increase the pointers until we find the first occurrence.
3. If the second pointer reach the end of the string there is no occurrence.
   
**Time Complexity:** *O(n)*, where n is the length of the string.

**Space Complexity:** *O(n)*, as we use only the given array and some variables.
```python []
class Solution(object):
    #:type haystack: str
    #:type needle: str
    #:rtype: int
    def strStr(self, haystack, needle):
        p1 = 0
        p2 = len(needle)

        while p2 <= len(haystack) and haystack[p1:p2] != needle:
            p1+=1
            p2+=1
        if p2 > len(haystack):
            p1 = -1
        return p1 
```
## C++
Beats 100%
Same solution in c++ but only uses one pointer and the length of needle since it uses substr() method instead of python´s slicing. It uses try catch instead of manually checking in the while.

*¿Why try catch?* if not I had to do multiple if´s and all exception can be catched if the substr() method fails. It gets the code cleaner and since exceptions are rare it doesnt impact too much on time performance, yet it affects space performance. *Learnings*: catch(...) is used to catch any exception without setting a parameter.
```c++
class Solution {
public:
    int strStr(string haystack, string needle) {
        int c = 0;
        
        try {
            while(needle != haystack.substr(c,needle.length())) {
                c++;
            }
        } catch(...) {
            c = -1;
        }
        return c;
    }
};
```
