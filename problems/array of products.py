'''Algorithm
1. initialize a list comprehension called products
2. begin a for loop  cycling thrugh the range of the length of the array.
    initialize running product  == 1
3.  begin a nested for that will be:  for every i item in the array take the j value of 
all the remaining items in the array (where i is not equal to j) take the running product and 
multiply it by all other values of array[j]  and update the running product.
4. returning to the outer loop we assign products[i] to the runningProduct and tehn
5. return products
'''

def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    for i in range(len(array)):
        runningProduct = 1
		for j in range(len(array)):
			if i != j:
				runningProduct *= array[j]
		products[i] = runningProduct
		
	return products
