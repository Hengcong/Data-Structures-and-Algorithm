# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:22:53 2022
The procedure assumes that subarrays L and R are in sorted order
@author: Hengcong Guo
"""

arr= input('array to be sorted:')
arr = [int(n) for n in arr.split()]

print(arr)

def MergeSort(array):
    n1 = int(len(array)/2 )
    n2 = len(array) - n1

    L = array[0:n1]
    R = array[n1:]

    i = 0
    j = 0
    for k in range(len(array)):

        if L[i] <= R[j]:

            array[k] = L[i]
            i +=1
            
            if i == len(L):
                array[i+j:] = R[j:]
                break
        else:
            array[k] =R[j]
            j = j+1
            if j == len(R):
                array[i+j:] = L[i:]
                break
    print(array)
    
MergeSort(arr)
