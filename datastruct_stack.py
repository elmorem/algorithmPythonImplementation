# The stack abstract data type is defined by the following structure and operations. 
# A stack is structured, as described above, as an ordered collection of items where 
# items are added to and removed from the end called the “top.” Stacks are ordered LIFO. 
# The stack operations are given below.

# Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
# push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
# pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
# peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
# isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
# size() returns the number of items on the stack. It needs no parameters and returns an integer.

from logging import raiseExceptions


class Stack:
    
    def __init__(self):
        self.items = []
        self.min=[]
        self.minVal=float("inf")

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        if len(self.min) == 0:
            self.min.append(item)
            self.minVal = self.min[-1]

        elif item < self.min[-1]:
            self.min.append(item)
            self.minVal = self.min[-1]

    def size(self):
        return len(self.items)

    def pop(self):
        if self.size() == 0:
            print("you messed up.")
        else:
            popped = self.items.pop()
            if popped <= self.minVal:
                self.min.pop()
                self.minVal = self.min[-1]
            return popped
                      
    def peek(self):
        return self.items[len(self.items)-1]

    def getMin(self):
        return self.minVal 


nums=Stack()
nums.push(1)
nums.push(-1)
nums.push(3)
nums.push(5)
nums.push(-2)

print(nums.peek())
print(nums.getMin())
nums.pop()
print(nums.peek())
print(nums.getMin())

nums.pop()
print(nums.peek())
print(nums.getMin())