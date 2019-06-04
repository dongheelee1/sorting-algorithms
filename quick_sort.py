
'''
IDEA: 
  
  Pick pivot (partition function returns this pivot element) and arrange elements based on this pivot. 
  For example, put elements less than pivot to be on the left side and elements greater than pivot to be on the right side. 
  
  Then, call quicksort on the array up to pivot-1 index. 
  
  Call quicksort on the 
  
  partition example 
  
  [2, 5, 7, 3, 4] 
  [2, 5, 7, 3, 4] 
  [2, 5, 7, 3, 4] 
  [2, 5, 7, 3, 4]  
  [2, 3, 7, 5, 4]
  [2, 3, 4, 5, 7]
  
  return index 2

  
'''
  
def partition(arr, left, right): 
  
  pivot = arr[right] #last element 
  
  i = left - 1
  
  for j in range(left, right-1): #exclude the last index (index of the pivot), travel arr from left to right
    
    if arr[j] <= pivot:
      
      i += 1 #as soon as current element is less than or equal to pivot, increment i counter...
      #ith pointer is used to place the current jth element, which is smaller than pivot, on the left side the arr
      #
      
      arr[i], arr[j], = arr[j], arr[i] #swap...before the swap, the ith pointer is pointing to element greater than pivot 
                                       #...after the swap, the ith pointer is pointing to element smaller than pivot and previous element at that swap is put on the right side of arr
  
  arr[i+1], arr[right] = arr[right] #swap the pivot element so that it clearly separates the left (smaller) and right (greater)
  
  return i+1 #return the new pivot index 

def quicksort(arr, left, right): 
  if left < right: 
    partition_idx = partition(arr, left, right)
    quicksort(arr, left, partition_idx-1)
    quicksort(arr, partition_idx+1)
    
        
  
  
  
