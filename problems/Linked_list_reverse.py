Reverse linked list

# This is an input class. Do not edit.
'''
we need to swap the self and next values.  And in order to make the whole thing
work, we need to have three pointers and they must update simultaneously.  This is
actually very rare.  most of the time we only need 2 for problems like this. AND
how do we update all 3?  in this scenario, we call the 3 pointers (p1,p2,p3) and 
they will correspond to previousNode, currentNode and nextNode(currentNode.next)... so we
set nextNode(p3)= currentNode.next // set currentNode.next = previousNode //
previousNode to currentNode//currentNode=nextNode
0(n)time and O (1)space because it is inplace
Algo:
1.initialize previousNode and CurrentNOde and set their values to None and head.
2. initiate a while loop set to run as long as there is a currentNode.
3. initialize the third pointer(nextNode) and set it to currentNode.next
4. then begin the shifting (exactly in the order below)
5.  set currentNode.next to previousNode
6. set previousNOde to currentNode
7. then set currentNode to nextNOde
8. return previousNode
'''

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    previousNode, currentNode = None, head
	while currentNode is not None:
		nextNode = currentNode.next
		currentNode.next= previousNode
		previousNode=currentNode
		currentNode= nextNode
	return previousNode
