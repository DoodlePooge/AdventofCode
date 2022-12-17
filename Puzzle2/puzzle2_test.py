from puzzle2 import round_score, total_score, traverse_file

rounds: list[int] = [8, 1, 6]
calories: list[int] = [7000, 8000, 9000]
    
def test_round_score() -> None:
    score = round_score('Y', 'win')
    assert score == 8

def test_add_calories_held() -> None:
    sum = total_score(rounds)
    assert sum == 15

def test_traverse_file() -> None:
    assert rounds == traverse_file("exampleInput.txt")