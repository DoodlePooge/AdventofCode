def max_index(num: [int]) -> int:
    maxIn = 0
    for i, value in enumerate(num):
        if num[maxIn] < value:
            maxIn = i

    return maxIn

def find_double_digit(num: [int]) -> int:
    maxIn = max_index(num)
    if maxIn == (len(num) - 1):
        d2 = maxIn
        d1 = max_index(num[:-1])
    else:
        d1 = maxIn
        d2 = max_index(num[d1+1:]) + len(num[:d1+1])

    return int(f'{num[d1]}{num[d2]}')

def traverse_file(fileName: str) -> [str]:
    file = open(fileName)
    lines = file.readlines()
    arr = []

    for line in lines:
        arr.append(line)
    return arr


def main():
    arr = traverse_file("input.txt")
    sum = 0

    for item in arr:
        digits = [int(d) for d in str(item[:-1])]
        sum += find_double_digit(digits)

    print(sum)

main()