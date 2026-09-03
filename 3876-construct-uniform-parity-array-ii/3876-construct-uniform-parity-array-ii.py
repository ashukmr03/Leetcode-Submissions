class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd=[x for x in nums1 if x%2]
        even=[x for x in nums1 if x%2==0]
        return not odd or not even or min(odd)<min(even)