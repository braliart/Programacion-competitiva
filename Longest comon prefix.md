# Longest common prefix

Problem: https://leetcode.com/problems/longest-common-prefix/

## Python
### Sort array and startswith() solution
O(n^2) Complexity. Beats 100%
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
### Trie solution
A Trie is a Tree made of the letters of the alphabet so in encapsules all of the words in the given strings. Example:
![image](https://github.com/user-attachments/assets/9a7042aa-4c27-4193-aedc-1141a63d8629)

Output: Contents of Trie: answer, any, bye, their, there 
1. We first implement the Trie class with just a method to add words.
2. Then add the words to the Trie and look for the shortest word.
3. Then we check the array and append letters until one node has more than one entry, that would mean at least one word doesnt have that prefix.
4. We put the len of the shortest word to prevent the case of substrings.

```Python
class TrieNode():
    def __init__(self):
        self.children = {}

class Trie():
    def __init__(self):
        self.root = TrieNode()
    def addWord(self,word):
        curr = self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        trie = Trie()
        curr = trie.root
        res = ""
        c = 0 #To control case of substrings array
        mini = strs[0]

        if '' not in strs: #check if there are not empty strings
            for i in strs:
                trie.addWord(i)
                if len(i)<mini:#Search for the shortest word
                    mini = len(i)
            dic = curr.children.keys()        
            while len(dic) == 1 and c<mini:
                curr = curr.children[dic[0]]
                res += dic[0]
                dic = curr.children.keys()
                c+=1

        return res
```
