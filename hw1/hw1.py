"""
DSA HW Assignment 1
Question 1: 
Each list takes up a continuous segment in memory. 

With concatenation, assuming the arrays are able to be concatenated (they are of objects of the same type, etc),
you must find a new place in memory (O(1) time) to store the concatenated array, and you must copy over every item 
from the first list, and then every item from the 2nd list right afterwards. If there are A items in the first list 
and B items in the second list, then the time complexity will be O(A+B + 1).  

Question 2: 
a) unimodal means an increasing followed by decreasing sequence...
Perform a binary search for the maximum element - AKA, use the property that it is sorted, and we can always tell which 
'half' of the array we're in when given an element and it's surrounding elements. We can also use the fact that the largest 
item has a smaller items on both the left and right ... 

----- pseudocode -------
define a top and bottom index 
while !((item > item-1) and (item > item + 1))

    redefine a top and bottom based on the surroudning elements - should the bottom shift up to the current item index, or the top shift down
    recompute the item index, it's in the middle of the top and bottom 

once we land on the largest item return it

* note all operations are done with item indices
---
why does it run in O(log(N)) time: with every step it cuts in half the number of elements it needs to search through. It takes log2(N) iterations 
to return a value. Thus it's complexity is O(log(N)). 

b) 
loop invariant - 
initialization - 
maintenance - 
termination - 
"""

__author__ = "Adi Ramachandran"

def find_max_val_unimodal_arr(arr): 
    """
    returns highest value in unimodal array via ~binary search
    """
    itop = len(arr)-1
    ibtm = 0
    imid = int((itop-ibtm)/2+ibtm)
    exit_case = arr[imid]>arr[imid+1] and ((imid-1<0) or arr[imid]>arr[imid-1])

    while not (exit_case): # only one of these needs to be true 
        # determine which side of the arr we're on, and always move towards the 'middle' --> however, we can only use the right side bc we're only guaranteed a number on the right side. 
        if arr[imid]<arr[imid+1]: 
            # we're on the left side so we wanna move right
            ibtm = imid
        else: 
            itop = imid
        imid = int((itop-ibtm)/2+ibtm)
        exit_case = arr[imid]>arr[imid+1] and ((imid-1<0) or arr[imid]>arr[imid-1])
        print(imid, exit_case)
        

    return arr[imid]