def check_possible(game: str) -> bool:
    contents = {"red": 12, "green": 13, "blue": 14}
    rounds = game.split(';')
    for round in rounds:
        cubes = round.split([' ', ','])
        for index in range(cubes)/2:
            if cubes[index+1] is contents[0] and cubes[index] <= contents['red']:
                return False
              
        print(round)
    return True

def traverse_file(fileName: str) -> list[int]:
    file = open(fileName)
    lines = file.readlines()
    sum = 0

    for line in lines:
        gameInfo = line.split(':')
        if check_possible(gameInfo[1]):
            sum += int(gameInfo[0].split(' ')[1])
    return sum


def main():
    print(traverse_file("example_input1.txt"))
main()