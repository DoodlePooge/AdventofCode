def max_index(num: [int]) -> int:
    maxIn = 0
    for i, value in enumerate(num):
        if num[maxIn] < value:
            maxIn = i

    return maxIn

def find_joltage(num: [int]) -> int:
    result =[0,0,0,0,0,0,0,0,0,0,0,0]
    offset = len(num) - 11
    start = max_index(num[:offset])
    result[0] = num[start]
    start += 1

    for d in range(1,12):
        start += max_index(num[start:offset+d])
        result[d] = num[start]
        start += 1

    return result

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
        digits = [int(d) for d in str(item.strip())]
        arr = find_joltage(digits)
        result = "".join([str(digit) for digit in arr])
        print(result)
        sum += int(result)

    print(sum)

main()