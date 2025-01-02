# Roman to integer
link: https://leetcode.com/problems/roman-to-integer/description/

## Using a hash map and an array
Store the catalog of info in a dict, then operate the char array acordingly with the dict.

```Python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = list(s) #arreglo de chars
        res = 0
        catalog = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        i = 0

        while i < len(letters):
            if i+1<len(letters):
                if catalog[letters[i+1]] > catalog[letters[i]]:
                    res += (catalog[letters[i+1]] - catalog[letters[i]])
                    i+=2
                else:
                    res += catalog[letters[i]]
                    i+=1
            else:
                res += catalog[letters[i]]
                i+=1

        return res
```
In leetcode solutions I found a better implementation of the intuition that I had: https://leetcode.com/problems/roman-to-integer/solutions/3651672/best-method-c-java-python-beginner-friendly/
