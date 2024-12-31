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
## Solcuiones en C++
Mismas soluciones, pero en c++.

### Con char array
Se complicó copiar el string al char array con strcpy, se debió usar un const para definir el tamaño del arreglo.

```c++
class Solution {
public:
    bool isPalindrome(int x) {
        std::string s = std::to_string(x);
        bool flag = true;
        const int n = s.size();
        int begin = 0;
        int end = n-1;
        char arr[n + 1];
        std::strcpy(arr, s.c_str());
        
        while(flag and begin<end) {
            if(arr[begin] != arr[end]){
                flag = false;
            }
            begin++;
            end--;
        }

        return flag;
    }
};
```
### Invertir el número

Se hace utilizando la lógica de manejo de números decimales. Donde 121 = 100 + 20 + 1.

```c++
class Solution {
public:
    bool isPalindrome(int x) {
        bool flag = true;
        if (x < 0) {
            flag = false;
        }

        long long reversed = 0;
        long long temp = x;

        while (temp != 0) {
            int digit = temp % 10;
            reversed = reversed * 10 + digit;
            temp /= 10;
        }
        cout<<reversed;

        if (reversed != x) {
            flag = false;
        }
        return flag;
    }
};
```
