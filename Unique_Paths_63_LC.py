'''A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.
Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

# Recursive Solution
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
      m = len(obstacleGrid)
      n = len(obstacleGrid[0])
      return self.count_unq_paths(0,0,m,n,obstacleGrid)
      
    def count_unq_paths(self,i,j,m,n,obstacleGrid):
      if i>m-1 or j>n-1 or obstacleGrid[i][j]==1:
        return 0
      elif i==m-1 and j==n-1:
        return 1
      else:
        return self.count_unq_paths(i,j+1,m,n,obstacleGrid)+self.count_unq_paths(i+1,j,m,n,obstacleGrid)
