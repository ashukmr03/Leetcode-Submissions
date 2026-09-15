class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0 
        position=0
        while n:
            if n & 1:
                if position % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>=1 
            position += 1
        return [even,odd]