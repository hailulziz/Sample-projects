import time
import math
import random

def linearSearch(l, x):
    for item in l:
        if item == x:
            return True
    return False

def binarySearch(l, x):
    mid = math.floor(len(l) / 2)
    #base case
    if len(l) == 0:
        return False

    #recursive step
    if x > l[mid]:
        return binarySearch(l[mid+1:], x)
    elif x < l[mid]:
         return binarySearch(l[0:mid], x)
    else:
        return True


new_list = []
x = random.randint(10000, 20000)
for i in range(x):
    new_list.append(i)
    holder = new_list[i]

start_linear = time.time()
linearSearch(new_list, holder)
end_linear = time.time()
linear_time = end_linear - start_linear
print(f"The worst case running time of linear search algorithm is %f" %(linear_time))

start_binary = time.time()
binarySearch(new_list, holder)
end_binary = time.time()
binary_time = end_binary - start_binary
print(f"The worst case running time of binary search algorithm is %f" %(binary_time))


