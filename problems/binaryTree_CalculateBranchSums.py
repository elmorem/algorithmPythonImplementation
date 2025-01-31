'''LOGIC
1. initialize an array (sums that will)
2. we create a helper function that will do the work of calculating the branch sums
3.  helper function initializes newRunningSums

'''

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
		
#we use this function to collect the branch sums
def branchSums(root):
    sums=[]
	calculateBranchSums(root, 0, sums)
	return sums

def calculateBranchSums(node, runningSum, sums):
    # I think this is the base case here	
    # but the way he described is in cases where there might be a left node but no right node
	if node is None:
		return
	#both of the returns here kick us out of the conditional logic
	newRunningSum = runningSum + node.value
	
	#Initialize
	#how does the algorithm know that it has reached a branch node?   
	# It knows when it has reached a leaf 
	#with no left or right node -- that is what the 2 lines below do.
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
	#if we reach a leaf node we append the new sum, which is the running sum 
	#plus the nodes value
		return
	calculateBranchSums(node.left, newRunningSum, sums)
	calculateBranchSums(node.right, newRunningSum, sums)

    # this function doesn't return anything it just collects running sums and 
    #then collects and appends those to the array sums
#
