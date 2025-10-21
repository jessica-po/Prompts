class Solution:
    def reverseWords(self, s: str) -> str:
        sLst = s.split()
        # print(sLst)
        reverseStr = ""

        for i in range(len(sLst)-1,-1,-1):
            if i == (len(sLst)-1):
                reverseStr+=sLst[i]
            else:
                reverseStr+=(" "+sLst[i])
        return reverseStr