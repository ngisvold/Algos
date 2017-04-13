# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 22:27:53 2017

@nathangisvold
"""
a=[1,1,1,2,2,9,5,3,55,57,34]

counter=[0]
    
def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        #print(lefthalf)
        #print(righthalf)
        
        merge_sort(lefthalf)
        merge_sort(righthalf)
        
        #print(lefthalf)
        #print(righthalf)
        
        i = 0
        j = 0
        k = 0
                
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                counter[0]+=len(lefthalf) #Inversion
                j += 1
            
            k +=1
            #print('R: ', arr)
            
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i +=1
            k +=1
            #print('L: ', arr)
            
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1
            
    #print('merg ', arr)
               
merge_sort(a)
print(counter)
