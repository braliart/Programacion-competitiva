# Palindrome number

```Python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag = True
        s = str(x)
        c = list(s)
        begin = 0
        end = len(c)-1

        while flag and begin<end:
            if c[begin] != c[end]:
                flag = False
            begin+=1
            end-=1

        return flag
```
