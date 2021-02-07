"""
[Insert description]

pytest documentation: https://docs.pytest.org/en/stable/getting-started.html
Documentation on parameterizing test functions: https://docs.pytest.org/en/stable/parametrize.html#parametrize
How to run the test(s) in this file: `pytest [this file name].py`. Any function whose name begins with "test_" is
identified by pytest as a test and will be run.

You are welcome to use a different format for your pytest testing; this is just a suggested way to do it. Something that
you *must* keep with your testing, however, is the timeout decorator: "@pytest.mark.timeout(1)".
"""

import pytest
# Import your unimodal max value function here


__author__ = "[Insert your name here]"


test_cases = [
    # Test with nominal odd-length array
    (
        [1, 2, 3, 2, 1],  # input unimodal list
        3  # maximum value expected
    ),
    # [Insert the rest of your test cases here]
]

@pytest.mark.timeout(1)  # tell pytest to consider the test failed if it takes more than 1 second to complete
@pytest.mark.parametrize("test_case", test_cases)  # pass in each element of the test_cases array as the test_case arg
def test_find_max_val_unimodal_arr(test_case):
    """
    [Fill out docstring]
    """

    # When pytest is run, each item in the test_cases list will be used as the test_case argument for this function. Use
    # an assert statement to assert that the output your function returns

    pass

# You can add more test functions if you like, but it is not necessary. If you do, the function name must begin with
# "test_", and you must use a "@pytest.mark.timeout(1)" decorator
