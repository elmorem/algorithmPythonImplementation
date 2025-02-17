def inOrderTraverse(tree, array):
    if tree is not None:
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
	return array
# 	left, center, right
def preOrderTraverse(tree, array):
    if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	return array
#  	center, left, right
def postOrderTraverse(tree, array):
    if tree is not None:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array
# 	left, right, center