'''
4 3 2 10 12 1 5 6 
3 4 2 10 12 1 5 6 
.
.
.
'''
def insertion_sort(arr): 
  
  for i in range(1, len(arr)): 
    current_elem = arr[i] 
    j = i - 1
    while j >= 0 and arr[j] > current_elem: #while j is at least 0 and elem at j is smaller than the current element 
      #shift every element to the right by overriding what is exactly right of it 
      arr[j+1] = arr[j] 
      j -= 1
    #once arr[j] is not greater than what is right of it, replace with current_elem 
    arr[j+1] = current_elem #place
