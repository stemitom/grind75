"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from typing import List

class Solution:

    def isAnagram(self, s:str, t:str) -> bool:
        return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = dict()
        for string in strs:
            count = [0] * 26
            
