
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ans = []
        for c in nums:
            s = 0
            k = c
            while k:
                s += k % 10
                k = k // 10
            ans.append([s, c])
        ans.sort()
        #ai help starts from here
        # Extract the sorted array
        target = [c for s, c in ans]
        # Map each number to its current index
        pos = {num: i for i, num in enumerate(nums)}
        swaps = 0
        visited = [False] * len(nums)
        for i in range(len(nums)):
            if visited[i] or pos[target[i]] == i:
                continue
            # Count the cycle
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[target[j]]
                cycle_size += 1
            swaps += cycle_size - 1
        return swaps