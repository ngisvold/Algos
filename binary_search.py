# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:13:54 2017

@nathangisvold

Binary Search Iterative
"""

def binary_search(input_array, value):
    last = len(input_array)-1
    first = 0
    
    while first <= last:
        #print(i, mid, value)
        mid = (first+last)//2
        
        if value == input_array[mid]:
            #return('Index: ', mid)
            return mid
        elif value < input_array[mid]:
            #mid= mid-1
            #mid=mid//2
            last = mid-1
            #print('Mid -1: ', mid)

        else:
            #mid= mid+1
            #mid=mid+ mid//2
            first = mid + 1
            #print('Mid +1: ', mid , i)


    return -1

test_list = [1,2,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
test_val3 = 11
test_val4 = 1
test_val5 = 2
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
#print(binary_search(test_list, test_val3))
#print(binary_search(test_list, test_val4))
print(binary_search(test_list, test_val5))