Dynamic Programming – ways to make change

'''Algorithm
1.Like other dynamic programming questions, this one begins by initializing a datastructure within 
2. which to build up the values.  we do this with a list complrehension.  
3. we then set the first value of this to 1
4. we are then going to loop through  each of the denominations for 
    each of the amounts.  (we therefore have a nested loop.)
5.  if the denomination is less than or equal to the amount we do
6. 
time O(nd) space O (n)
n= target amount of money
denoms = coin denominations
Inputs:  
'''

def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n + 1)]
	ways[0] = 1
	for denom in denoms:
		for amount in range(1, n + 1):
			if denom <= amount:
				ways[amount] +=ways[amount - denom]
				# same as ways[amount] = ways[amount] + ways[amount-denom]
	return ways[n]
