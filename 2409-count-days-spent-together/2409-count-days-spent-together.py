class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def to_day(date: str) -> int:
            month, day = map(int, date.split("-"))
            return sum(months[:month - 1]) + day
        a1, a2 = to_day(arriveAlice), to_day(leaveAlice)
        b1, b2 = to_day(arriveBob), to_day(leaveBob)
        start = max(a1, b1)
        end = min(a2, b2)
        return max(0, end - start + 1)