class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        if x > 0:
            su = 0
            while x:
                digit = x % 10
                x //= 10
                if su > (INT_MAX - digit) // 10:
                    return 0
                su = su * 10 + digit
            return su
        else:
            x = -x
            su = 0
            while x:
                digit = x % 10
                x //= 10
                if su > (INT_MAX - digit) // 10:
                    return 0
                su = su * 10 + digit
            return -su