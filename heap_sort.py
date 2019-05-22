'''
Heapsort algorithm (Geeks-for-Geeks as resource)

A complete binary tree: A binary tree in which every level is completely filled except for possibly the last level.

A binary heap in comes in two flavors: max heap or min heap
A complete binary tree is where the parent node is greater (max heap) or smaller (min heap) than the values of both the left and right child.

Array-based representation for binary heap: if the idx for a parent node is i, then the idx for child node is 

1. 
'''
#build_max_heap on subtree rooted at i 

def build_max_heap(arr, i): 
  
  parent_idx = i #value at this index is supposed to be greater than the value of both the left and right child
  left_idx = 2*i + 1
  right_idx = 2*i + 2
  
  #if left child of the parent exists and is greater than the parent value
  if left_idx < len(arr) and arr[left_idx] > arr[parent_idx]: 
    #update the parent_idx to be left_idx
    parent_idx = left_idx
  #if right child of the parent exists and is greater than the parent value 
  if right_idx < len(arr) and arr[right_idx] > arr[parent_idx]: 
    #update the parent_idx to be right_idx
    parent_idx = right_idx
    
  #if parent_idx has been changed to either the right_idx or left_idx (whichever is max)
  if parent_idx != i
    #swap elements
    arr[parent_idx], arr[i] = arr[i], arr[parent_idx]
    #original parent element arr[i] is set at the parent_idx (either updated to right_idx or left_idx)
    #now, pass in the parent_idx to build_max_heap to heapify subtree rooted at parent_idx 
    build_max_heap(arr, parent_idx)
    
 
  
  
  
  
