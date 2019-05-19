'''
BUBBLE SORT

for each pass, the biggest element in the current pass bubbles to the rightmost end of the list
repeat above step n times 

time complexity: O(N^2) (nested for loop) ==> worst case is when input list is in reverse order, best case is when input is already sorted
auxiliary space: O(1) (swap)

input array: [10, 9, 8, 7, 6]
[9, 8, 7, 6, 10]
[8, 7, 6, 9, 10]
[7, 6, 8, 9, 10]
[6, 7, 8, 9, 10]
[6, 7, 8, 9, 10]
[6, 7, 8, 9, 10]
'''
#optimized version (include a swapped flag to return arr if there was no swap in a pass) 
def bubble_sort(arr):
    
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j+1] <= arr[j]: #swap if the next element is greater than the current element 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True 
        if swapped == True: 
            return arr

    return arr
    
print(bubble_sort([1, 4, 2, 7, 8, 4]))
