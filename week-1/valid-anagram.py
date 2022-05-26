"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        return sorted(s) == sorted(t)


from collections import Counter
class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        return Counter(s) == Counter(t)


from collections import Counter
class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)