from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        frequencyListMap = {}
        res = []

        for num in nums:
            if num in frequencyMap:
                frequencyMap[num] += 1
            else:
                frequencyMap[num] = 1

        for key, value in frequencyMap.items():
            if value in frequencyListMap:
                frequencyListMap[value].append(key)
            else:
                frequencyListMap[value] = [key]

        for i in range(len(nums), 0, -1):
            print(i)
            if len(res) >= k:
                break
            if i in frequencyListMap:
                res.extend(frequencyListMap[i])
        return res
