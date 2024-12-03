def is_safe(arr: [int]) -> bool:
    previous = arr[0]
    increase: bool
    for val in arr[1:]:
        diff = previous - val
        try:
            if increase and diff < 0:
                return False
            if not increase and diff > 0:
                return False
        except:
            increase = diff > 0
        if diff > 3 or diff < -3 or diff == 0:
            return False
        previous = val

    return True

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
        if is_safe(report):
            sum += 1
    print(sum)

main()