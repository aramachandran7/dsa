"""
DSA HW Assignment 1
[answers to homework in markdown]
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
        # determine if we're being trolled by a 2 len array edge case, where our imid will never be incremented properly 
        if imid == int((itop-ibtm)/2+ibtm): # we're being trolled
            imid += 1
        else: # This is no edge case, this is the normal operation 
            imid = int((itop-ibtm)/2+ibtm) 
        
        exit_case = ((imid+1)==len(arr) or arr[imid]>arr[imid+1]) and ((imid-1<0) or arr[imid]>arr[imid-1])
        # print("ibtm, imid, itop", ibtm,imid,itop, exit_case) # for debug
        
    return arr[imid]