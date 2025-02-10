# Find the index of the first occurrence in a string
Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
## Python
**Time Complexity:** *O(n)*, where n is the length of the s.

**Space Complexity:** *O(n)*, as we use anly the given array and some variables.

We use the split() method to split the string everytime it occurs, then we catalog the cases. split() makes an array of the parts were needle doesnt occur, then we analyze the first slot of the array.

1. If it is equal to haystack then there is no occurrence.
2. If it equals '' the occurrence is at the beginning.
3. If any of the other, then the occurrence will be at the end of the first slot, that´s why we use `len(arr[0])`.

```Python
class Solution(object):
    #:type haystack: str
    #:type needle: str
    #:rtype: int
    def strStr(self, haystack, needle):
        arr = haystack.split(needle)
        ans = 0

        if arr[0] == '':#the occurrence is at the beginning
            ans = 0
        elif arr[0] == haystack:#there arent occurrences
            ans = -1
        else:#the occurrence is in some place at the array
            ans = len(arr[0])

        return ans
```
