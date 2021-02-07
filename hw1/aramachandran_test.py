
"""
todo: 
get pytest working with python3, <-- get pip working with python3 
get edge case of 2 nums working
get basic proof down
"""

import pytest
from hw1 import find_max_val_unimodal_arr

__author__ = "Adi Ramachandran"

# You are welcome to use a different format for your pytest testing; this is
# just a suggested way to do it. Something that you *must* keep with your
# testing, however, is the timeout decorator: "@pytest.mark.timeout(1)".

test_cases = [
    # Insert test cases here.
    [4,9,12,13,14,13,12,11,4,-1, -29],
    [-44449999,-44449998,-44449993,-44449992, -44449991, -44449990, 0, -55550000],
    [1,2], 
    [1,2,3,2],
]


# @pytest.mark.timeout(1)
# @pytest.mark.parametrize("test_case", test_cases)
def test_find_max_val_unimodal_arr(test_cases):
    """
    [Fill out docstring]
    """
    # Complete function
    
    for case_num, test_case in enumerate(test_cases): 
        print('testing case: ', case_num)
        found = find_max_val_unimodal_arr(test_case)
        # assert found == max(test_case)

        if found == max(test_case): 
            print("passed case ", case_num, " | Found max value to be ", found)



if __name__=="__main__": 
    test_find_max_val_unimodal_arr(test_cases)
