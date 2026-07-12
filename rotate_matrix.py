from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range (i+ 1, n):
                matrix[j][i] , matrix[i][j] =  matrix[i][j], matrix[j][i]


    def reflect(self,matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j] , matrix [i][-j-1] = matrix [i][-j-1],matrix[i][j]




def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate(matrix)
    print(matrix)

if __name__ == "__main__":
    main()




