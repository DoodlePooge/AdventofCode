
def add_calories_held(calories: list[int]) -> int:
    sum = 0
    for cal in calories:
        sum += cal
    return sum

def find_max_calories_held(elves: list[int]) -> int:
    maxCals = 0
    for elf in elves:
        if elf > maxCals:
            maxCals = elf
    return maxCals

def traverse_file(fileName: str) -> list[int]:
    file = open(fileName)
    lines = file.readlines()
    elves: list[int] = []
    calories: list[int] = []

    for line in lines:
        if line == '\n':
            elves.append(add_calories_held(calories))
            calories = []
        else:
            if line.strip():
                calories.append(int(line))
    
    elves.append(add_calories_held(calories))
    return elves


def main() -> None:
    print(find_max_calories_held(traverse_file("input1.txt")))
    return

main()