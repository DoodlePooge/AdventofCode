from puzzle2 import total_score, traverse_file_pt_one, traverse_file_pt_two, determine_outcome, determine_play, round_score_pt_one, round_score_pt_two

rounds1: list[int] = [8, 1, 6]
rounds2: list[int] = [4, 1, 7]
    
def test_round_score_pt_one() -> None:
    score = round_score_pt_one('Y', 'win')
    assert score == 8

def test_round_score_pt_two() -> None:
    score = round_score_pt_two('scissors', 'Y')
    assert score == 6

def test_total_score() -> None:
    sum = total_score(rounds1)
    assert sum == 15

def test_determine_outcome() -> None:
    outcome = determine_outcome('A Y')
    assert outcome == 'win'

def test_determine_play() -> None:
    play = determine_play('A X')
    assert play == 'scissors'
    play = determine_play('A Y')
    assert play == 'rock'
    play = determine_play('A Z')
    assert play == 'paper'

def test_traverse_file_pt_one() -> None:
    assert rounds1 == traverse_file_pt_one("exampleInput.txt")


def test_traverse_file_pt_two() -> None:
    assert rounds2 == traverse_file_pt_two("exampleInput.txt")