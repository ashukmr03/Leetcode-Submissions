class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[c*c for c in nums]
        nums.sort()
        n=len(nums)
        s=0
        if(n%2==0):
            k=int(n/2)
            for i in range(k,n):
                s+=nums[i]
            for i in range(k):
                s-=nums[i]
        else:
            k=n//2
            for i in range(k,n):
                s+=nums[i]
            for i in range(k):
                s-=nums[i]
        return s