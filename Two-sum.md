## Two sum
This is a problem from leetcode: https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
![image](https://github.com/user-attachments/assets/d884b8ce-f6d8-476a-a79c-000ab0a9d2b8)

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

### Two sum with arrays
Solución por fuerza bruta. Recorrer un arreglo dos veces es como recorrer una matriz, por el tipo de problema se puede solo recorrer la parte superior de la matriz haciendolo con whiles, con lo que se reduce la complejidad de O(n^2) a O((n^2)/2).

``` Python
class Solution(object):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def twoSum(self, nums, target):
        i = 0
        j = 1
        while i<len(nums) and nums[i]+nums[j] != target:
            while j<len(nums) and nums[i]+nums[j] != target:
                j += 1
            if j==len(nums) and i<len(nums)-1:
                i += 1
                j = i+1
                
        return [i,j]
```

Tras ver la solución optimizada en Java procedo a hacer la versión optimizada en Python.

### Two Sum with hash maps

Esta versión del problema usa diccionarios (hashmaps) para mejorar la velocidad sacrificando memoria. Se mejora de O(n2) a O(n). 

``` Python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        #Se meten como llaves los valores del arreglo y como valores del diccionario se meten los índices del arreglo.
        for i in range(len(nums)):
            dic[nums[i]] = i
        #Target = a+b -> a = target-b. B lo tenemos al recorrer el arreglo entonces buscamos a (target-b).
        # El complemento lo tomamos del arreglo nums para no tener problema de llaves mapeadas
        for i in range(len(nums)):
            if target - nums[i] in dic and dic[target-nums[i]] != i:
                res = [i,dic[target-nums[i]]]
        return res
```
            
            
