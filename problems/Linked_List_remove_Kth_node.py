#Linked List Remove Kth node from list

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
def removeKthNodeFromEnd(head, k):
    first = head
	second = head
	counter = 1
	#You want this counter to start at 1 so that you don't get any off by one
	#errors
	while counter <= k:
		second = second.next
		counter +=1
	if second is None:
		#if you have a condition where second is none and the head is the one you 
		#want to remove, you can't just delete the head. You need to update the head value to 
		#point to head.next.value and head. next to equal head.next.nect
		head.value = head.next.value
		head.next = head.next.next
		return 
	#if so you just want it to end and return (nothing)
	while second.next is not None:
		#while that is true, increment both pointers
		second = second.next
		first = first.next
	#so because we said when second.next is not none when we break out of the while loop
	#we will be left with the final value. SO THE FIRST POINTER WILL BE POINTING
	#to the node right before the one we want to remove all we have to do is is set 
	#first.next=first.next.next
	first.next = first.next.next
