class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        res=[]
        ans=0
        for k in range(n):
            if n%(k+1)==0:
                ans+=nums[k]*nums[k]
        return ans