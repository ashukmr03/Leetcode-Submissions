class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)/2
        m=len(set(candyType))
        return int(m) if m<n else int(n)