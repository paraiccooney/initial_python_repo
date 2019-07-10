       
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_is__not_in(collection, item):
    assert item not in collection, "{0} contains the value {1}".format(collection, item)

test_is_in([1,2,3,4,5,6], 6)

test_is__not_in([1,2,3,4,5], 6)

print("All tests passed")