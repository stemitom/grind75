from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in hashMap:
                return hashMap[remainder], i
            hashMap[num] = i
