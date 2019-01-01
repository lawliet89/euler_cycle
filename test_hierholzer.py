import pytest
from hierholzer import hierholzer, str_list_to_dict, get_edges


def simple_input():
    input = ["0 -> 3", "1 -> 0", "2 -> 1,6", "3 -> 2",
             "4 -> 2", "5 -> 4", "6 -> 5,8", "7 -> 9", "8 -> 7", "9 -> 6"]
    return str_list_to_dict(input)


@pytest.fixture(scope="module", params=["fixtures/dataset_203_2.txt"])
def data(request):
    with open(request.param, "r") as f:
        return str_list_to_dict(f.readlines())


def test_simple():
    assert hierholzer(simple_input()) == [(0, 3), (3, 2), (2, 6), (6, 8), (
        8, 7), (7, 9), (9, 6), (6, 5), (5, 4), (4, 2), (2, 1), (1, 0)]


def test_output(data):
    output = hierholzer(data)
    edges = get_edges(data)
    # Let's do some sanity check
    assert(set(edges) == set(output))
    # Check that it loops back
    assert(output[0][0] == output[-1][1])

    # Trace the path to see if it "breaks" along the way
    previous = output[0][1]
    for i in range(1, len(output)):
        (left, right) = output[i]
        assert(left == previous)
        previous = right
