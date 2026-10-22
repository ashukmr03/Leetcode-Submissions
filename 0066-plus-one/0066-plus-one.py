class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(len(digits)-1,-1,-1):
            sm=digits[i]+carry
            digits[i]=sm%10
            carry=sm//10
        if carry>0:
            return [carry]+digits
        return digits