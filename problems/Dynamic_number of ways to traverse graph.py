'''start from the top left and go to bottom right

'''

def numberOfWaysToTraverseGraph(width, height):
    if width == 1 or height ==1:
		return 1
	
	return numberOfWaysToTraverseGraph(width -1, height) + numberOfWaysToTraverseGraph(width, height -1)
