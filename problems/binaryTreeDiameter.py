'''Binary tree diameter

# This is an input class. Do not edit.
#we're going to want to use some type of a depth-first search pattern because we know
#that we're going to want to travel deep into the tree
'''

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(0,0)
	
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
	maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
	currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
	currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
	
	return TreeInfo(currentDiameter, currentHeight)

class TreeInfo:
	def __init__(self, diameter, height):
		self.diameter = diameter
		self.height = height
