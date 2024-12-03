def min_index(arr: [int]) -> int:
    minIn = 0
    for i, value in enumerate(arr):
        if arr[minIn] > value:
            minIn = i

    return minIn

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
    length = len(arr1)

    for _ in range(length):
        min1 = min_index(arr1)
        min2 = min_index(arr2)
        sum += abs(arr1[min1] - arr2[min2])
        arr1.pop(min1)
        arr2.pop(min2)

    print(sum)

main()