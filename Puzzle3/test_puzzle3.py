from puzzle3 import find_the_type, traverse_file, determine_priority, priority_sum

rucksack = 'vJrwpWtwJgWrhcsFMMfFFhFp'
priorities = [16, 38, 42, 22, 20, 19]

def test_find_the_type() -> None:
    mid = len(rucksack) // 2
    assert 'p' == find_the_type(rucksack[:mid], rucksack[mid:])

def test_determine_priority() -> None:
    assert 16 == determine_priority('p')

def test_priority_sum() -> None:
    assert 157 == priority_sum(priorities)

def test_traverse_file() -> None:
    assert priorities == traverse_file('example_input.txt')