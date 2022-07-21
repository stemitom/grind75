from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashSet = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if (
                    num + "-row " + str(i) in hashSet
                    or num + "-col " + str(j) in hashSet
                    or num + "-box " + str(i // 3) + str(j // 3) in hashSet
                ):
                    return False
                hashSet.add(num + "-row " + str(i))
                hashSet.add(num + "-col " + str(j))
                hashSet.add(num + "-box " + str(i // 3) + str(j // 3))

        return True
