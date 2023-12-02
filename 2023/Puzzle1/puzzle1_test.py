from puzzle1 import find_nums, traverse_file

sum1 = 142
example1 = "a1b2c3d4e5f"
example2= "oneight"

def test_traverse_file() -> None:
    assert sum == traverse_file("example_input1.txt")
    
def test_find_nums() -> None:
    assert 15 == find_nums(example1)
    assert 18 == find_nums(example2)