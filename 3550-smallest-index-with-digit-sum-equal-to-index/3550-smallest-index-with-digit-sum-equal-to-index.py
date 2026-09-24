class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def calcsum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        for i in range(len(nums)):
            if i == calcsum(nums[i]):
                return i

        return -1