class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        prefix = {0: 0}
        suffix = []
        ps = 0
        ss = 0
        for i in range(n):
            ps += nums[i]
            if ps > x:
                break
            prefix[ps] = i + 1
        for i in range(n - 1, -1, -1):
            ss += nums[i]
            if ss > x:
                break
            suffix.append((ss, n - i))
        ans = prefix.get(x, n + 1)
        for suffix_sum, suffix_count in suffix:
            needed = x - suffix_sum
            if needed in prefix:
                prefix_count = prefix[needed]
                if prefix_count + suffix_count <= n:
                    ans = min(ans, prefix_count + suffix_count)
        return -1 if ans == n + 1 else ans