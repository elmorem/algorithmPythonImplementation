'''
Questions:
1. Node
2.  I think what is so confusing about these problems is that 
they don't really seem to use loops.  instead they turn fundamentally on 
recursion.
'''
########################################################
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
########################################################
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

########################################################
class BSTNode:
    def __init__(self, data = None, left= None, right=None):
        self.data, self.left, self.right = data, left, right

########################################################
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
########################################################
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
########################################################
  class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


########################################################
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array
########################################################
#  DFS // BFS and traversals
########################################################
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
########################################################
def breadthFirstSearch(self, array):
    queue = [self]
    while len(queue) > 0:
        current = queue.pop(0)
        array.append(current.name)
        for child in current.children:
            queue.append(child)
    return array
########################################################
def depthFirstSearch(self, array):
    array.append(self.name)
    for child in self.children:
        child.depthFirstSearch(array)
    return array
########################################################
from collections import deque
def bfs(graph, start_node, end_node):
    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)
    # Keep track of what nodes we've already seen
    # so we don't process them twice
    nodes_already_seen = set([start_node])
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()
        # Stop when we reach the end node
        if current_node == end_node:
            # Found it!
            break
        for neighbor in graph[current_node]:
            if neighbor not in nodes_already_seen:
                nodes_already_seen.add(neighbor)
                nodes_to_visit.append(neighbor)


########################################################

########################################################

########################################################

########################################################

########################################################