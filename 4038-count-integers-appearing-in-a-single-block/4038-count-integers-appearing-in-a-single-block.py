from collections import Counter
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        temp=[]
        for current_num in nums:
            if not temp or temp[-1]!=current_num:
                temp.append(current_num)
        freq=Counter(temp)
        return sum(1 for count in freq.values() if count==1)