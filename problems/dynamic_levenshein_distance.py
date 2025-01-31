''' ALGORITHM:
calculate the number of edits performed on str1 to obtain str2
1. initiate a nested list comprehension that will nest len(str2)lists the length of str1
 so if str1 length is 3 and str2 length is 6 the list will contain 6 lists of length 3
'''
def levenshteinDistance(str1, str2):
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
	for i in range (1, len(str2) + 1):
		edits[i][0] = edits[i - 1][0] +1
		
	for i in range(1, len(str2) + 1):   #each of these
		for j in range(1, len(str1) + 1):   #for each of these
			if str2[i-1] == str1[j-1]:
				edits[i][j] = edits[i - 1][j - 1]
			else:
				edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1])
	return edits[-1][-1]