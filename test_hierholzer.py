from hierholzer import hierholzer, str_list_to_dict


def simple_input():
    input = ["0 -> 3", "1 -> 0", "2 -> 1,6", "3 -> 2",
             "4 -> 2", "5 -> 4", "6 -> 5,8", "7 -> 9", "8 -> 7", "9 -> 6"]
    return str_list_to_dict(input)


def test_simple():
    assert hierholzer(simple_input()) == [(0, 3), (3, 2), (2, 6), (6, 8), (
        8, 7), (7, 9), (9, 6), (6, 5), (5, 4), (4, 2), (2, 1), (1, 0)]
