class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s1 = s.replace("-", "").upper()
        first_len = len(s1) % k
        if first_len == 0:
            first_len = k
        ans = s1[:first_len]
        for i in range(first_len, len(s1), k):
            ans += "-" + s1[i:i+k]
        return ans