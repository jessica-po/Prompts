class Solution:
     def generateMatrix(self, n):
         """
         :type n: int
         :rtype: List[List[int]]
         """
         if n<1:
             return []
         left=0
         right=n-1
         up=0
         bottom=n-1
         self.matrix=[[0 for i in range(n)] for j in range(n)]
         count=1
         while left<=right:
             if left<right:
                 count=self.DrawRow(up,left,right,count)
                 count=self.DrawCol(right,up,bottom,count)
                 count=self.DrawRow(bottom,right,left,count)
                 count=self.DrawCol(left,bottom,up,count)
             else:
                 count=self.DrawCol(left,up,bottom+1,count)
                 break
             up+=1
             bottom+=-1
             left+=1
             right+=-1
         return self.matrix
 
     def DrawRow(self,row,start,end,value):
         add=1
         if start>end:
             add=-1
         for i in range(start,end,add):
             self.matrix[row][i]=value
             value+=1
         return value
     def DrawCol(self,col,start,end,value):
         add=1
         if start>end:
             add=-1
         for i in range(start,end,add):
             self.matrix[i][col]=value
             value+=1
         return value