import dtw
import pytest

def test_seq1():
    s1 = [1, 2, 3, 4, 5, 5, 5, 4]
    s2 = [3, 4, 5, 5, 5, 4]
    result = ([[0, 0], [1, 0], [2, 0], [3, 1], [4, 2],
               [5, 3], [6, 4], [7, 5]], 2)
    assert dtw.dynamic_time_warping(s1, s2) == result

def test_seq2():
    s1 = [1, 2]
    s2 = [3, 4]
    result = ([[0, 0], [1, 1]], 3)
    assert dtw.dynamic_time_warping(s1, s2) == result

def test_one_elements():
    s1 = [1]
    s2 = [1]
    result = ([[0, 0]], 0)
    assert dtw.dynamic_time_warping(s1, s2) == result

def test_one_elem():
    s1 = []
    s2 = [1]
    with pytest.raises(Exception):
        dtw.dynamic_time_warping(s1, s2)
def test_one_elem2():
    s1 = [1]
    s2 = []
    with pytest.raises(Exception):
        dtw.dynamic_time_warping(s1, s2)

def test_empty_seq():
    s1 = []
    s2 = []
    with pytest.raises(Exception):
        dtw.dynamic_time_warping(s1, s2)

def test_one_seq():
    s1 = [100]
    with pytest.raises(Exception):
        dtw.dynamic_time_warping(s1)

def test_one_seq2():
    s2 = [100]
    with pytest.raises(Exception):
        dtw.dynamic_time_warping(s2)
        
