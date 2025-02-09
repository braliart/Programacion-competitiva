# Remove element
Problem:

## Python
**Time Complexity:** *O(n)*, where n is the length of the array.

**Space Complexity:** *O(n)*, as we use anly the given array and some variables.

This is a problem of **swapping** the undesired val to the end of the array. We need to set 2 pointers, one that begins at the first instance of val and the other that begins at the first element which we can swap the val for. Pointer 1 is going to increase while pointer 2 is going to decrease.

*Why is it a swapping problem if it says remove?* because swapping is faster than deleting so swapping all the vals to the end of the array is more optimal than deleting them.

1. First we **set the pointers**. In setting the pointers we use a try catch to handle all the cases were the array doesnt have the val, it is empty, it is full of vals, etc.
2. Then we travel the array swapping the val in pointer 1 with the val in pointer 2 whenever pointer 1 is a val. We always increase pointer 1, however we only decrease pointer 2 if there is a swap.
3. We **stop increasing** pointer 1 when we approach the end of the array that has all the swapped vals to prevent pointer 1 be higher than pointer 2. This doesnt work with just `p1 < p2` because it will stop counting the `k` instances that val repeats itself in the array, therefore giving a wrong answer. We achieve that decreasing p1 whenever `p1 == val and p2 == val`.

NOTE: another way to do this is using the index() method on the while too, but it is slower and uses more space. It does the trick since it will set the value in the first occurrence of val, not letting p1 to be higher than p2.
```Python
class Solution(object):
    #:type nums: List[int]
    #:type val: int
    #:rtype: int
    def removeElement(self, nums, val):
        flag = True
        k=0
        p2 = -1 #pointer 2
        l = len(nums)
        ans = 0

        try:
            p1 = nums.index(val) #establish initial pointer 1
            while nums[p2] == val: #establish initial pointer 2
                k+=1
                p2-=1
        except:
            if l == k: #case array full of vals
                ans = 0
            else: #any other case that breaks
                ans = l
            return ans

        while p1 < l-k and p1<l:
            if nums[p1] == val:
                nums[p1],nums[p2] = nums[p2],nums[p1]#swap elements
                if nums[p2] == val: #set p1 in the first occurrence as if using index()
                    p1-=1
                p2-=1
                k+=1
            p1+=1

        return l-k
```
