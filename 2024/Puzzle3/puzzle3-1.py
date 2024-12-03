import re

def run_functions(arr: [str]) -> int:
    total = 0

    for mult in arr:
        numbers = re.findall(r"[0-9]+", mult)
        total += int(numbers[0]) * int(numbers[1])
    return total

def traverse_file(fileName: str) -> [[int]]:
    file = open(fileName)
    return file.readlines()


def main():
    programs = traverse_file("input.txt")
    sum = 0
    for program in programs:
        functions = re.findall(r"mul\([0-9]+,[0-9]+\)", program)
        print(functions)
        sum += run_functions(functions)
    print(sum)


main()