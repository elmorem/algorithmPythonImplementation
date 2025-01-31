
Write a function that takes in an an array of positive integers and returns the max sum of non-adjacent elements in the array

'''Algorithm
1.  setup for 2 edge conditions:  if the array is empty or has only one element
2.  initialize a maxSums variable which is going to be a shallwo copy of the array
3. then set maxSums[1] equal to whichever is greater the num in position 0 or pos 1
4.  then setup the for loop, which will start at index 2
5.  here's the heart:  maxSums[i] is going to be equal to whichever is greater:
max(maxSums[i-1], maxSums[i-2]+array[i])

this is a dynamic programming problem because we are basically updating the 3 values as
we move forward
The Key here is that we are keeping track of the max value as we are going forward
'''

Def maxSubsetSumNoAdjacent (array):
	If len(array == 0:
		Return 0
	Elif len(array) ==1:
		Return array[0]
	maxSums = array[:]
	maxSums[1]=max(array[0], array[1])
	for I in range(2,len(array)):
		maxSums[i]=max( maxSums[i-1], maxSums[i-2] + array[i]
	return maxSums[-1]
