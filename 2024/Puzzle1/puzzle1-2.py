def num_occurs(val: int, arr: [int]) -> int:
    total = 0

    for num in arr:
        if num == val:
            total += 1

    return total

def traverse_file(fileName: str) -> tuple[[int], [int]]:
    file = open(fileName)
    lines = file.readlines()
    arr1, arr2 = ([], [])

    for line in lines:
        numbers = line.split('   ')
        arr1.append(int(numbers[0]))
        arr2.append(int(numbers[1]))
    return arr1, arr2


def main():
    arr1, arr2 = traverse_file("input1.txt")
    sum = 0
    unique = list(set(arr1))

    for val in unique:
        occur1 = num_occurs(val, arr1)
        occur2 = num_occurs(val, arr2)
        sum += val * occur2 * occur1

    print(sum)

main()