from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        return (
            nums.index(max(nums))
            if all(i * 2 <= max(nums) for i in nums if i != max(nums))
            else -1
        )
