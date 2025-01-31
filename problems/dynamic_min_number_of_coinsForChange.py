'''Algorithm:
Logic to solve this is similar to the previous question
1. initalize an array with a list comprehension filling in values of infinity for each one
2. set the first value == 0 what this means is that the minimum
number of coinms needed to make 0 dollars is 0
3.  setup a nested for loop which goes therough each denomiation for each of the possible amounts
up to n+1
4.  set the if condition:  if the denomination is less than or equal to the amount
5. KEY: then the numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1)
6.  finally, return the number of coins at [n] if numOfCoins[n] != float("inf") else -1
7. this last part gets returned when change cannot be made.
'''
def minNumberOfCoinsForChange(n, denoms):
    numOfCoins = [float("inf") for amount in range(n + 1)]
	numOfCoins[0]= 0
	for denom in denoms:
		for amount in range(len(numOfCoins)):
			if denom <= amount:
				numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1)
	return numOfCoins[n] if numOfCoins[n] != float("inf") else -1
