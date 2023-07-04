from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = [ [1] * x for x in range(1, numRows + 1)]
        for i in range(2, numRows):
            for j in range(1, i):
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
        return matrix


if __name__=='__main__':
    obj = Solution()
    print(obj.generate(6))