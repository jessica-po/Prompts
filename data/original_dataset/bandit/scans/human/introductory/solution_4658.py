class Solution:
    def reverseBits(self, n: int) -> int:
        rev = ''
        for i in reversed(bin(n)[2:]):
            rev = rev + i
        rev = rev + '0'*(32-len(rev)) 
        
        return int(rev, 2)