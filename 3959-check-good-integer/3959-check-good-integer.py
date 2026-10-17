class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        ds=0
        ss=0
        while n:
            ds+=n%10
            ss+=(n%10)*(n%10)
            n=n//10
        return (ss-ds)>=50