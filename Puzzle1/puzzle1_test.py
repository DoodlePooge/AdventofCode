from puzzle1 import find_max_calories_held, add_calories_held, traverse_file

elves: list[int] = [6000, 4000, 11000, 24000, 10000]
calories: list[int] = [7000, 8000, 9000]

def test_add_calories_held() -> None:
    sum = add_calories_held(calories)
    assert sum == 24000

def test_traverse_file() -> None:
    assert elves == traverse_file("exampleInput1.txt")
    
def test_find_max_calories_held() -> None:
    max = find_max_calories_held(elves)
    assert max == 24000