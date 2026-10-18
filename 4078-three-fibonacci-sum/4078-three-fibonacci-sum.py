class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        if(n%2==1):
            return False
        ts=int(n/2)
        if(ts<1):
            return False
        fs=[0,1]
        s=fs[-1]+fs[-2]
        if(s==ts):
            return True
        while s<ts:
            s=fs[-1]+fs[-2]
            fs.append(s)
            if(s==ts):
                return True
        return False