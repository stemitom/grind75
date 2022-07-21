from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = [1] * n
        t = [1] * n

        for i in range(1, n):
            s[i] = s[i - 1] * nums[i - 1]

        for i in reversed(range(n - 1)):
            t[i] = t[i + 1] * nums[i + 1]

        return [s[i] * t[i] for i in range(n)]
