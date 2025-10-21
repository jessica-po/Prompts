class Solution:
     def compareVersion(self, version1, version2):
         """
         :type version1: str
         :type version2: str
         :rtype: int
         """
         while version1 and version2:
             result1 = version1.split('.', 1)
             if len(result1) == 2:
                 digit1, version1 = result1[0], result1[1]
             else:
                 digit1 = result1[0]
                 version1 = ""
             result2 = version2.split('.', 1)
             if len(result2) == 2:
                 digit2, version2 = result2[0], result2[1]
             else:
                 digit2 = result2[0]
                 version2 = ""
             if int(digit1) > int(digit2):
                 return 1
             elif int(digit1) < int(digit2):
                 return -1
 
         if version1 and sum(map(lambda x: int(x), version1.split('.'))) != 0:
             return 1
         if version2 and sum(map(lambda x: int(x), version2.split('.'))) != 0:
             return -1
         return 0