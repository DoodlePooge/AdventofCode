from puzzle4 import is_contained, total_contained, does_overlap, traverse_file_pt_one, traverse_file_pt_two

assignment = '2-8,3-7'
assignments1 = [False, False, False, True, True, False]
assignments2 = [False, False, True, True, True, True]
assignments3 = [True, True, True, True, False, False]
assignments4 = []

def test_is_contained() -> None:
    sections = assignment.split(',')
    assert is_contained(sections[0], sections[1])

def test_does_overlap() -> None:
    sections = assignment.split(',')
    assert does_overlap(sections[0], sections[1])

def test_total_contained() -> None:
    assert total_contained(assignments1) == 2

def test_traverse_file_pt_one() -> None:
    assert assignments1 == traverse_file_pt_one('example_input1.txt')

def test_traverse_file_pt_two() -> None:
    assert assignments2 == traverse_file_pt_two('example_input1.txt')
    assert assignments3 == traverse_file_pt_two('example_input2.txt')