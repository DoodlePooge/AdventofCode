

def round_score_pt_one(play: str, outcome: str) -> int:
    playScore = 0
    outcomeScore = 0

    if play == 'X':
        playScore = 1
    elif play == 'Y':
        playScore = 2
    else:
        playScore = 3

    if outcome == 'win':
        outcomeScore = 6
    elif outcome == 'tie':
        outcomeScore = 3

    return playScore + outcomeScore

def round_score_pt_two(play: str, outcome: str) -> int:
    playScore = 0
    outcomeScore = 0

    if outcome == 'X':
        outcomeScore = 0
    elif outcome == 'Y':
        outcomeScore = 3
    else:
        outcomeScore = 6

    if play == 'scissors':
        playScore = 3
    elif play == 'paper':
        playScore = 2
    else:
        playScore = 1

    return playScore + outcomeScore

def total_score(rounds: list[int]) -> int:
    sum = 0
    for round in rounds:
        sum += round
    return sum

def determine_play(line: str) -> str:
    if line == 'A X' or line == 'B Z' or line == 'C Y':
        return 'scissors'
    elif line == 'A Y' or line == 'B X' or line == 'C Z':
        return 'rock'
    return 'paper'

def determine_outcome(line: str) -> str:
    if line == 'A X' or line == 'B Y' or line == 'C Z':
        return 'tie'
    elif line == 'A Y' or line == 'B Z' or line == 'C X':
        return 'win'
    return 'loss'

def traverse_file_pt_one(fileName: str) -> list[int]:
    file = open(fileName)
    lines = file.readlines()
    rounds: list[int] = []

    for line in lines:
        rounds.append(round_score_pt_one(line[-2], determine_outcome(line.strip())))
    
    return rounds

def traverse_file_pt_two(fileName: str) -> list[int]:
    file = open(fileName)
    lines = file.readlines()
    rounds: list[int] = []

    for line in lines:
        rounds.append(round_score_pt_two(determine_play(line.strip()), line[-2]))
    
    return rounds

def main():
    rounds = traverse_file_pt_one('input2.txt')
    print(total_score(rounds))
    rounds = traverse_file_pt_two('input2.txt')
    print(total_score(rounds))

main()