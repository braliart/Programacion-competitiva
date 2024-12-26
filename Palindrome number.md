# Palindrome number

Problema: https://leetcode.com/problems/palindrome-number/

## Primera solución

El enfoque es volver el int a string y luego a un arreglo de chars para comparar entrada por entrada el principio y el final.

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
## Otro enfoque

Otro enfoque más eficiente es convertir a string e invertirlo, debe ser igual. No se me ocurrió, lo vi en las soluciones de leetcode.

```Python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag = False
        y = str(x)[::-1] #Truco de slicing para invertir un string
        if str(x) == y:
            flag = True
        return flag
```
