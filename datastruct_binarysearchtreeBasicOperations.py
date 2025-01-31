class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#average O (logn) space O (1)
# worst O (n) space O (1)
    def insert(self, value):
        currentNode = self
		while True:   #this essentially means forever intil we hit a break
			if value < currentNode.value:
				if currentNode.left is None:
					currentNode.left = BST(value)
					break
				else:
#If there is already some value in there, that value then becomes the new current node.
					currentNode = currentNode.left
	#if this value is GREATER than the current node
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode= currentNode.right
        return self

    def contains(self, value):
        currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				currentNode = currentNode.left
			elif value > currentNode.value:
				currentNode = currentNode.right
			else:
				return True
		return False
			

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
