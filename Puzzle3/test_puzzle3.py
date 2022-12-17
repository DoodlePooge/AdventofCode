from puzzle3 import determine_priority, priority_sum, traverse_file_pt_one, traverse_file_pt_two, find_the_type_pt_one, find_the_type_pt_two

rucksacks = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg']
priorities1 = [16, 38, 42, 22, 20, 19]
priorities2 = [18, 52]

def test_find_the_type_pt_one() -> None:
    mid = len(rucksacks[0]) // 2
    assert 'p' == find_the_type_pt_one(rucksacks[0][:mid], rucksacks[0][mid:])

def test_find_the_type_pt_two() -> None:
    assert 'r' == find_the_type_pt_two(rucksacks)

def test_determine_priority() -> None:
    assert 16 == determine_priority('p')
    assert 52 == determine_priority('Z')

def test_priority_sum() -> None:
    assert 157 == priority_sum(priorities1)
    assert 70 == priority_sum(priorities2)

def test_traverse_file_pt_one() -> None:
    assert priorities1 == traverse_file_pt_one('example_input.txt')

def test_traverse_file_pt_two() -> None:
    assert priorities2 == traverse_file_pt_two('example_input.txt')