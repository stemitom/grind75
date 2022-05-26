"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        return any(c > 1 for c in counts.values())

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numberSet = set()
        for i in nums:
            if i in numberSet:
                return True
            numberSet.add(i)
        return False
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)