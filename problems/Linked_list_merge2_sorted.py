#Linked list merge 2 sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# instantiate a variable to hold a value previous to the head.
# in this case, listnode(-1)
        prehead=ListNode(-1)
#set that prehead equal to previous
        prev=prehead
#initiate a while list that will process the 2 lists as long as they have nodes
        while list1 and list2:
# if the value of list1 head is less than or equal to list2 head
            if list1.val<=list2.val:
#set prev.next= to list1 
                prev.next=list1
                list1=list1.next
 #otherwise we set it to list 2
  else:
                prev.next =list2
                list2=list2.next
#then we move forward
            prev=prev.next
#now we need to deal with the condition where either list1 or list2 is empty.
#here we set prev.next == to whichever is not None

        prev.next=list1 if list1 is not None else list2
#finally we return prehead.next
        return prehead.next
