'''
INVERT BINARY TREE
the initial logic here with the queue and the while loop is a pattern he uses several times.
1.  so we instantiate a queue which is a list formed from the tree.
2.  then we say that while the queue still has a length (that is, it does not ==0 which would evaluate to false)
   we then perform the stuff inside.
   3.  we first pop off the initial value
   4.  then we run the swap function on current
   5. then we append the left side to the queue
 ISSUE:  why is there no return statement
 '''

def invertBinaryTree(tree):
    queue = [tree]
	while len(queue):
		current = queue.pop(0)
		if current is None:
			continue
		swapLeftAndRight(current)
		queue.append(current.left)
		queue.append(current.right)
	return tree
		
# this is the helper function that will swap our children nodes		
def swapLeftAndRight(tree):
	tree.left, tree.right = tree.right, tree.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
