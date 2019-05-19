'''
MERGESORT 
input: list, output: list 

Merge sort is a divide and conquer algorithm. 

At each level of the recursion, halve the input list. 
Then, call mergesort on both halves of the input list like the following: 

left = mergesort(list[:mid])
right = mergesort(list[mid:]

Base case is when there is only one element in the input list, at which point, return the one element.

After calling mergesort on both halves, glue the two halves together by calling merge on the two halves. 

MERGE 
input: list1 and list2, output: list

Merge merges two lists together and outputs a combined list. 
Assume that both list1 and list2 are sorted.

set up counters for list1 and list2 
iterate through both list1 and list2, compare each element and append element that's smaller to output list 
if there are elements left over in either list, add remainder to output list and return 

Time complexity: O(nlogn) 
Space complexity: O(n)
'''
def merge_sort(lst):
    if len(lst) == 1:

        return [lst[0]]

    mid = (len(lst))// 2


    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(lst1, lst2):

    i = 0
    j = 0
    output_lst = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            output_lst.append(lst1[i])
            i += 1
        else:
            output_lst.append(lst2[j])
            j += 1
    output_lst += lst1[i:]
    output_lst += lst2[j:]

    return output_lst

print(merge_sort([1, 5, 4, 8, 3, 7, 30]))
   
  
  
  
