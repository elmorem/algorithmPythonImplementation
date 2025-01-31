def first(element, array):
    for i, array_element in enumerate(array):
        if element == array_element:
            return (i+1)
    return -1

def first(element, array):
    for i, array_element in enumerate(array):
        if array_element == element:
            return i
    return -1
def first(element, array):
    for i, array_element in enumerate(array):
        return array_element == element
    return -1

def has_pos_neg(nums):
    has_pos = False
    has_neg = False
    for num in nums:
        has_pos=num > 0
        has_neg= num<0
    return (has_pos, has_neg)
    
def func(a,b):
    a += 1
    b.append(1)



def build_word_tree_from_sentences(sentence_list):
    root = {}
    for sentence in sentence_list:
        base = root
        for word in sentence.split(' '):
            if not base.get(word):
                base[word]= {}
            base = base[word]
    return root

tree= build_word_tree_from_sentences(['Hello world', "Hello there"])



import random

def select(values, k):
    pivot =random.choice(values)
    low, high = [], []
    for value in values:
        if value < pivot:
            low.append(value)
        elif value > pivot:
            high.append(value)
    if k < len(low):
        return select(low, k)
    k += len(high) - len(values)
    if k< 0:
        return pivot
    return select(high, k)


def select(values, k):
    pivot =random.choice(values)
    low, high = [], []
    for value in values:
        if value < pivot:
            low.append(value)
        elif value > pivot:
            high.append(value)
    if k < len(low):
        return select(low, k)
    k = len(low)
    if k< 0:
        return pivot
    return select(high, k)

def recursive_string_reverse(string):
    if len(string) <=1:
        return string
    first_char = string[0]
    last_chars = string[1:len(string)]
    return recursive_string_reverse(last_chars) + first_char




def sample(items, n):
    result = []
    for i, item in enumerate(items):
        if i < n:
            result.append(item)
        else:
            j = random.randint(0,i)
            if j < n:
                result.append(item)
    return result

def sample(items, n):
    result = []
    for i, item in enumerate(items):
        if i < n:
            result.append(item)
        else:
            j = random.randint(0,i)
            if j < n:
                result[j]= item
    return result

def deleteBlank(items):
    i = 0
    while i < len(items):
        if len(items[i]) == 0:
            del items[i]
        i +=1 

def format(num, sep=','):
    parts= []
    while num:
        num, mod = divmod(num, 1000)
        parts.append(f'{mod:03}')
    return sep.join(reversed(parts)) or '0'


import queue
import threading
import time

q = queue.Queue()
for i in [3,2,1]:
    def f():
        time.sleep(i)
        q.put(i)
    threading.Thread(target=f).start()
print(q.get())

try:
    file= open(filepath)
    data= file.read()
finally:
    file.close()

def _(func, items):
    i = 0
    for item in items:
        if func(item):
            items[i]= item
            i +=1
    del items[i:]
    
def func(i):
    return i

print(words)
['Hello', 'World']

for i, word in enumerate(words):
    words.lower()
    words[i] = word[::-1]




def rec(string):
    if len(string) <= 1:
        return string
    first = string[0]
    last = string[1:len(string)]
    return rec(last)

def rec(string):
    if len(string) <= 1:
        return string
    first = string[0]
    last = string[1:len(string)]
    return rec(last) + first

def rec(string):
    if len(string) <= 1:
        return string
    first = string[0]
    last = string[1:len(string)]
    return first + rec(last)

words = ['Hello', 'World']

for i, word in enumerate(words):
    words.lower()
    words[i] = word[::-1]
