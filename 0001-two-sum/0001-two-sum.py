class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            a=nums[i]
            for j in range(i+1,n):
                
                b=nums[j]
                if((a+b)==target):
                    return [i,j]