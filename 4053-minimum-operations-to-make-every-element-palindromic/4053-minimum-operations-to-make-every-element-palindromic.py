from bisect import bisect_left
palindromes = []
for p in range(1, 100000):
    s = str(p)
    palindromes.append(int(s + s[:-1][::-1]))
    palindromes.append(int(s + s[::-1]))
evens = sorted([x for x in palindromes if x % 2 == 0])
odds = sorted([x for x in palindromes if x % 2 == 1])
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        v = nums    
        total_ops = 0
        for x in v:
            arr = odds if x % 2 == 1 else evens
            idx = bisect_left(arr, x)   
            min_diff = float('inf')
            if idx < len(arr):
                min_diff = min(min_diff, arr[idx] - x)
            if idx > 0:
                min_diff = min(min_diff, x - arr[idx - 1])
            total_ops += min_diff // 2
        return total_ops