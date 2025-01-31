'''
best time O(n) worst time O (n2) space o(1)
logic:
overall logic here is that we start 
by sort of assuming that the beginning of the list is 
sorted and then iterating through the array arranging
things.
1.initialize the for loop and begin at 1
because you start comparing the value at index 0 with 
each of the values you cycle through the array.
2. initialize a second index called j
3. setup a while loop the logic of the while loop is:
while the number we're looking at is  not in the first positon
and as long as a number to the left is LESS THAN
j, we swap those values.
4.  then we decrement j as it moves to the left and try the while
loop again.  if it's good, we move on the the next value at i.

'''

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array

def swap(i, j, array):
    array[i], array[j]= array[j], array[i]