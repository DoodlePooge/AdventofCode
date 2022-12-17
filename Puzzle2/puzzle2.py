

def round_score(play: str, outcome: str) -> int:
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

def total_score(rounds: list[int]) -> int:
    sum = 0
    for round in rounds:
        sum += round
    return sum

def traverse_file(fileName: str) -> list[int]:
    return [0]

def main():
    return

main()