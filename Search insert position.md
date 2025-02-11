# Search insert position
Problem:
## Python
It is programing the binary search with two pointers.

1. We set p1 at the beginning and p2 at the middle of the array.
2. We observe if target is higher or lower than p2.
3. If it is lower we leave the pointers like that, otherwise we set p1 in the middle and p2 at the end of the array.
4. We increase p1 until find target or getting to p2.
5. Return p1.

```python
class Solution(object):
    #:type nums: List[int]
    #:type target: int
    #:rtype: int
    def searchInsert(self, nums, target):
        p1 = 0
        p2 = len(nums)/2
        
        if target >= nums[p2]:
            p1 = p2
            p2 = len(nums)
        while p1<p2 and nums[p1]<target:
            p1+=1

        return p1
```
