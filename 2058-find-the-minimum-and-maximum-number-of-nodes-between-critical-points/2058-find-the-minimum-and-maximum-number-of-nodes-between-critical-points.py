# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res=[]
        prev=head
        curr=head.next
        idx=1
        while curr and curr.next:
            nxt=curr.next
            if(curr.val>nxt.val and curr.val>prev.val):
                res.append(idx)
                idx+=1
                prev=curr
                curr=nxt
            elif(curr.val<nxt.val and curr.val<prev.val):
                res.append(idx)
                idx+=1
                prev=curr
                curr=nxt
            else:
                idx+=1
                prev=curr
                curr=nxt
        if(len(res)<2):
            return [-1,-1]
        mindist = float("inf")
        for i in range(1, len(res)):
            mindist = min(mindist, res[i] - res[i - 1])
        maxdist=res[-1]-res[0]
        return [mindist,maxdist]