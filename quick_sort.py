
'''
IDEA: 
  
  Find the partition element (this element will be first sorted)
  Call quicksort to sort the left side of the arr, excluding the partition element 
  Call quicksort to sort the right side of the arr, excluding the partition element 
  
  each recursive call places the pivot element, defined in the partition function, to be in the correct position in the sort

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
    #at each level of the recursive call, partition function puts elements greater than pivot on the right side of arr
    #and elements smaller than pivot on the left side of the arr
    #the pivot element in the partition function, here, is the last element of given arr or element at "right"
    #near the end of the partition function, swap elements one of which being this pivot element so that right 
    #and left sides are clearly divided
    #return the new index where pivot is placed
    partition_idx = partition(arr, left, right) #new pivot idx...this pivot is the first thing that's sorted
    quicksort(arr, left, partition_idx-1) #then call quicksort on the left portion of the arr, excluding the partition idx
    quicksort(arr, partition_idx+1) #call quicksort on the right portion of the arr, excluding the partition idx 
    
#quicksort will sort the given arr in place by first putting element chosen as pivot to be in the correct place in arr
#quicksort will be called again and again on the left and right portions excluding the partition element as they are jumbled but 
#are on the correct side of the partition element
    
        
  
  
  
