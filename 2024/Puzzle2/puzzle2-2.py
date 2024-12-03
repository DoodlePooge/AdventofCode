def get_diffs(arr: [int]) -> [int]:
    diffs = []
    previous = arr[0]
    for num in arr[1:]:
        diffs.append(previous - num)
        previous = num
    
    return diffs

def traverse_file(fileName: str) -> [[int]]:
    file = open(fileName)
    lines = file.readlines()
    values = []

    for line in lines:
        chars = line.split(' ')
        numbers = [int(num) for num in chars]
        values.append(numbers)
    return values


def main():
    reports = traverse_file("input.txt")
    sum = 0

    for report in reports:
        print(report)
        diffs = get_diffs(report)
        print(diffs)


    print(sum)

main()