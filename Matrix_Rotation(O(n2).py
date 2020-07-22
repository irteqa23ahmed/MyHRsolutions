# LeetCode := Rotate an N X N matrix 90 degree clockwise (1 rotation - right)

'''
1 rotation - right -> reverse the rows & Transpose the matrix

for eg. [[1,2,3],    reverse rows       [[7,8,9],    transpose        [[7,4,1],
         [4,5,6],   ----------->>>      [4,5,6],   ------------>>>     [8,5,2],
         [7,8,9]]                       [1,2,3]]                       [9,6,3]]
         
2 rotaion - right -> reverse rows, reverse each row

3 rotation - right - > reverse each row, then transpose

'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        for i in range((n//2)+1):
            matrix[i],matrix[n-i] = matrix[n-i],matrix[i]
        for i in range(1,n+1):
            j = 0
            while j < i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j+=1
        return matrix
        
