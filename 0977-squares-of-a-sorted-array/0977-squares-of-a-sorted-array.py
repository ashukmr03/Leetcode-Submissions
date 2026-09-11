class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=[c*c for c in nums]
        return sorted(n)