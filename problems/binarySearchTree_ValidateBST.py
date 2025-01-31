'''Validate BST

OO principles:  if we are going to have a helper function like we do here, the first time that we use it
as we do in the return statement for the primary function we initialize the extra values that are passed in.
in this case negative and positive infinity.
THEN:
when we are defining the helper function we use the generic terms (which in this case are minValue and maxValue,
but in the case of binary search are left and right.
Write a function that take in a potentially incalid BST and returns a boolean representing whether 
it is valid or not
'''
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minValue, maxValue):
	if tree is None:
		return True
    # what's hapening here?  checking to be sure that the value is greater than the min value
    #and less than the max value.  otherwise it returns false 
	if tree.value < minValue or tree.value >= maxValue:
		return False
        #now we need to check if the left subtree is valid
	leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
	return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)
    #then the AND statement here in the last line checks to see if the right sub tree is valid
    #if they both return true then the function will return true
