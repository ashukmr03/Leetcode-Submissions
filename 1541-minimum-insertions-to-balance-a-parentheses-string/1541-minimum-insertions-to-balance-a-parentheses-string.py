class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append('(')
                i += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    if stack:
                        stack.pop()
                    else:
                        ans += 1
                    i += 2
                else:
                    if stack:
                        stack.pop()
                        ans += 1
                    else:
                        ans += 2
                    i += 1
        return ans + 2 * len(stack)