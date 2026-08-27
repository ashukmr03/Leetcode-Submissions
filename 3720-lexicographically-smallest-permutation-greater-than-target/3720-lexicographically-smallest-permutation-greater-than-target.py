from collections import Counter
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        d = Counter(s)
        ans = []
        p = 0
        n = len(target)
        while p < n and d[target[p]] > 0:
            ans.append(target[p])
            d[target[p]] -= 1
            p += 1
        while True:
            if p < n:
                for code in range(ord(target[p]) + 1, ord('z') + 1):
                    c = chr(code)
                    if d[c] > 0:
                        ans.append(c)
                        d[c] -= 1
                        for ch in sorted(d):
                            ans.append(ch * d[ch])
                        return "".join(ans)
            if p == 0:
                return ""
            p -= 1
            removed = ans.pop()
            d[removed] += 1