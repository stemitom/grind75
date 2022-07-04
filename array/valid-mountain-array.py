from typing import List


class Solution:
    def strictly_moving(self, arr: List[int], up=True) -> bool:
        for i in range(len(arr) - 1):
            if not up:
                if arr[i + 1] < arr[i]:
                    continue
                else:
                    return False
            else:
                if arr[i + 1] > arr[i]:
                    continue
                else:
                    return False
        return True

    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        if arr[0] > arr[1]:
            return False
        if arr[-1] > arr[-2]:
            return False
        # finding the index of the last occurence of maximum number
        maxNum, res = max(arr), []
        res[:] = arr
        res.reverse()
        final = res.index(maxNum)
        idx = len(arr) - final - 1

        if self.strictly_moving(arr[: idx + 1]) == self.strictly_moving(
            arr[idx:], up=False
        ):
            return True
        return False


