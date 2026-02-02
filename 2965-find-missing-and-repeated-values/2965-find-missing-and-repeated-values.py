from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        repeat = -1

        # Find repeating number
        for row in grid:
            for num in row:
                if num in seen:
                    repeat = num
                seen.add(num)

        # Find missing number
        for num in range(1, n*n + 1):
            if num not in seen:
                return [repeat, num]
