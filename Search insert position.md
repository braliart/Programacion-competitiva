# Search insert position
Problem: https://leetcode.com/problems/search-insert-position/
## Python
It is programing the binary search with two pointers.

1. We set p1 at the beginning and p2 at the middle of the array.
2. We observe if target is higher or lower than p2.
3. If it is lower we leave the pointers like that, otherwise we set p1 in the middle and p2 at the end of the array.
4. We increase p1 until find target or getting to p2.
5. Return p1.

**Time Complexity:** *O(log n)*, where n is the length of the array.

**Space Complexity:** *O(n)*, as we use only the given array and some variables.
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
## C++
Same implementation, no significant difference.
```python
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int p1 = 0, p2 = nums.size()/2;

        if(target >= nums[p2]) {
            p1 = p2;
            p2 = nums.size();
        }
        while(p1<p2 && nums[p1]<target) {
            p1++;
        }

        return p1;
    }
};
```
