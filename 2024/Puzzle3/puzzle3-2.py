import re

def run_functions(arr: [str]) -> int:
    total = 0

    for mult in arr:
        numbers = re.findall(r"[0-9]+", mult)
        total += int(numbers[0]) * int(numbers[1])
    return total

def remove_do_nots(arr: [str]) -> [str]:
    do = True
    toDos = []
    for function in arr:
        if "don't" in function:
            do = False
        elif "do()" in function:
            do = True
        elif do:
            toDos.append(function)
    return toDos

def traverse_file(fileName: str) -> [[int]]:
    file = open(fileName)
    lines = file.readlines()
    program = ""
    for line in lines:
        program += line
    return program


def main():
    program = traverse_file("input.txt")
    sum = 0

    functions = re.findall(r"do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\)", program)
    sum += run_functions(remove_do_nots(functions))
    print(sum)


main()