class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        minimum_right=[0]*n
        minimum_right[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            minimum_right[i]=min(nums[i],minimum_right[i+1])
        maximum_left=0
        for i in range(n):
            maximum_left=max(maximum_left,nums[i])
            if maximum_left-minimum_right[i]<=k:
                return i
        return -1