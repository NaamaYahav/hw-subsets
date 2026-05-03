import pytest
from subsets import sorted_subset_sums
from testcases import parse_testcases
from itertools import islice

testcases = parse_testcases("testcases.txt")

def run_testcase(input:str):
    from itertools import takewhile, islice
    output = ""
    for i in eval(input):
        output += f"{i}, "
    output = output[:-2]  # remove last comma
    return output

@pytest.mark.parametrize("testcase", testcases, ids=[testcase["name"] for testcase in testcases])
def test_cases(testcase):
    actual_output = run_testcase(testcase["input"])
    assert actual_output == testcase["output"], f"Expected {testcase['output']}, got {actual_output}"


def test_new_cases():
    # your new tests here
    #empty set
    assert list(sorted_subset_sums([])) == [0]
    #single element
    assert list(sorted_subset_sums([5])) == [0, 5]
    #unordered input
    assert list(sorted_subset_sums([4,1,2])) == [0,1,2,3,4,5,6,7]
    # increasing order
    res = list(sorted_subset_sums([1,3,5]))
    assert res == sorted(res)
    #duplicate sums
    res = list(sorted_subset_sums([1,2,3]))
    assert res.count(3) == 2
    # large numbers
    res = list(islice(sorted_subset_sums([100,200,300]), 5))
    assert res == [0, 100, 200, 300, 300]
    # strictly increasing
    res = list(sorted_subset_sums([2,5,9]))
    for i in range(len(res)-1):
        assert res[i] <= res[i+1]
    
