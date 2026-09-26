import heapq

class Solution:
    def isPossible(self, target: list[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        total = sum(target)
        heap = [-num for num in target]
        heapq.heapify(heap)
        while -heap[0] > 1:
            largest = -heapq.heappop(heap)
            rest = total - largest
            if rest == 1:
                return True
            if rest <= 0 or largest <= rest:
                return False
            previous = largest % rest
            if previous == 0 or previous == largest:
                return False
            heapq.heappush(heap, -previous)
            total = rest + previous
        return True