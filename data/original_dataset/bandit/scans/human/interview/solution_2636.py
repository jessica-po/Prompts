class Solution(object):
     def getSkyline(self, buildings):
         """
         :type buildings: List[List[int]]
         :rtype: List[List[int]]
         """
         cp= set([b[0] for b in buildings]+[b[1] for b in buildings])
         i, active, res = 0, [], []
         for c in sorted(cp):
             while i<len(buildings) and buildings[i][0]<=c:
                 heapq.heappush(active, (-buildings[i][2], buildings[i][1]))
                 i+=1
 
             while active and active[0][1]<=c:
                 heapq.heappop(active)
 
             h= len(active) and -active[0][0]
             if not res or h!=res[-1][1]:
                 res.append([c, h])
         return res