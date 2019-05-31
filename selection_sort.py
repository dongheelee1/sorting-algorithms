'''
IDEA: 

// Find the minimum element in arr[0...4]
// and place it at beginning

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4] 

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
'''



for i in range(0, len(arr)): 
  
  min = i 
  
  for j in range(i+1, len(arr)): 
    if arr[min] > arr[j]: 
      min = j 
      
  arr[i], arr[min] = arr[min], arr[i] 
      
