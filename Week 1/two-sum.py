"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""
#...0(n^2) solution --> Bruteforce
class Solution:
    def twoSum(nums, target):
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

assert Solution.twoSum([2,7,8,9], 10) == [0,2]

#....0(n) solution --> Hashmap
class Solution:
    def twoSum(nums, target):
        hashMap = {}
        for i, value in enumerate(nums):
            remainder = target - nums[i]
            if remainder in hashMap:
                return [i, hashMap[remainder]]
            hashMap[value] = i

assert sorted(Solution.twoSum([2,7,8,9], 10)) == [0,2]