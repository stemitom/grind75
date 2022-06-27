from typing import List

"""
[1,0,1,1,0]
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        locations = []
        for i in range(len(nums)):
            if nums[i] == 0:
                locations.append(i)
        # locations = [1, 4]
        print(locations)

        if len(locations) == 0 or len(locations) == 1:
            return len(nums)
        # False, continues

        print("Counting..")
        count = 0
        for i in range(len(locations)):
            if i == 0:
                count = max(count, locations[i + 1])
                # count = max(0,4)
            if i == len(locations) - 1:
                count = max(count, len(nums) - (locations[i - 1] + 1))
                # count = max(4, 5-2)
            else:
                count = max(count, locations[i + 1] - locations[i - 1] - 1)
                # count = max(4, )

        return count
