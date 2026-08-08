class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {0: 0, 1: 0, 2: 0}  # pre-initialize all colors
        for c in nums:
            d[c] = d.get(c, 0) + 1

        i = 0
        for val in [0, 1, 2]:
            for _ in range(d[val]):
                nums[i] = val
                i += 1