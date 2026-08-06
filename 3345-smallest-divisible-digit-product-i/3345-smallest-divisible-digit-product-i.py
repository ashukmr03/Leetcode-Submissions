class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x):
            product=1
            while x > 0:
                product*=x%10
                x//=10
            return product
        num=n
        while digit_product(num)%t!=0:
            num+=1
        return num