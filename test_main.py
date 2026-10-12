from main import (
    freqency_count,
    duplicate_detect,
    index_map,
    grouping_key,
    hash_lookup,
    opposite_end,
    same_direction,
    read_write,
    twoarray
)

def test_frequency_count():
    assert freqency_count([1, 2, 2, 3]) == {
        1: 1,
        2: 2,
        3: 1
    }

    assert freqency_count([]) == {}

    print("Frequency tests passed!")

test_frequency_count()

def test_duplicate_detect():
    assert duplicate_detect([1, 5, 5]) == 5

    assert duplicate_detect([]) == None

    assert duplicate_detect([1,2,4]) == None

    print("Duplicate Detect tests passed!")

test_duplicate_detect()

def test_index_map():
    assert index_map([1, 3, 4], 4) == 2

    assert index_map([1, 3, 4], 7) == -1

    assert index_map([], 6) == -1

    print("index_map tests passed!")

test_index_map()

def test_grouping_key():
    assert grouping_key(['tea', 'ate', 'eat', 'ten','net']) == [['tea','ate','eat'], ['ten','net']]

    assert grouping_key([]) == []

    print("grouping_key tests passed!")

test_grouping_key()

def test_hash_lookup():
    assert hash_lookup([5, 5, 5], 10) == True

    assert hash_lookup([],10) == False

    print("Hash lookup tests passed!")

test_hash_lookup()

def test_opposite_end():
    assert opposite_end([2, 3, 5, 8], 5) == [(2,3)]

    assert opposite_end([2,4,5,7,9], 1) == []

    assert opposite_end([], 5) == []

    print("oppsite end tests passed!")

test_opposite_end()

def test_same_direction():
    assert same_direction([0, 5, 1, 0]) == [5, 1, 0, 0]

    assert same_direction([]) == []

    print("same_direction tests passed!")

test_same_direction()

def test_read_write():
    assert read_write([5, 2, 5, 2, 0, 0]) == [2, 2, 5, 5, 0, 0]

    assert read_write([]) == []

    print("read/write tests passed!")

test_read_write()

def test_twoarray():
    assert twoarray([5, 5, 5], [2, 5, 6]) == [5]

    assert twoarray([2,3,5,6], [1,4,7]) == []

    assert twoarray([],[]) == []

    assert twoarray([5,5,5], []) == []

    assert twoarray([], [2, 5, 6]) == []

    print("two array tests passed!")

test_twoarray()