# Longest common prefix

Problema: 

## Python
O(n^2) Complexity.
1. The array is sorted so the word with the longest common prefix is the first one.
2. The first element of the array is compared substring by substring (via slicing and the method startswith()) with all the other elements until the prefix is found, once it is the flag pops and it breaks the loop.
```Python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        c=0
        flag1 = True
        res = ""

        while flag1 and c<len(strs[0]):
            for i in range(0,len(strs)):
                temp = strs[0][:c+1]
                if not strs[i].startswith(temp):
                    flag1 = False
            if flag1:
                res = temp
            c+=1
                
        return res
```
