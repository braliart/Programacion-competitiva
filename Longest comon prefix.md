# Longest common prefix

Problem: https://leetcode.com/problems/longest-common-prefix/

## Python
### Sort array, compare extremes
O(n) Complexity. Beats 100%
1. The array is sorted so the word with the longest common prefix.
2. Comparing it with the last gives the longest common prefix since it is sorted.
```Python
class Solution(object):
    #:type strs: List[str]
    #:rtype: str
    def longestCommonPrefix(self, strs):
        strs.sort()
        c=0
        while c<len(strs[0]) and strs[0][c] == strs[len(strs)-1][c]:
            c+=1
                
        return strs[0][:c]
```
### Trie solution
A Trie is a Tree made of the letters of the alphabet so in encapsules all of the words in the given strings. It is implemented with nested dicts, example:
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
