class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        l=0
        max_length=-1
        running_sum=0
        target=sum(nums)-x
        for r in range(len(nums)):
            running_sum+=nums[r]
            while l<=r and running_sum>target:
                running_sum-=nums[l]
                l+=1
            if(running_sum==target):
                max_length=max(max_length,r-l+1)
        if max_length==-1:
            return -1 
        else:
            return len(nums)-max_length