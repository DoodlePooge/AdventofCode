def find_the_type(left: str, right: str) -> str:
    type = ''
    for l in left:
        for r in right:
            if l == r:
                type = r
    return type

def determine_priority(type: str) -> int:
    code = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return code.find(type) + 1

def priority_sum(priorities: list[int]) -> int:
    sum = 0
    for priority in priorities:
        sum += priority
    return sum

def traverse_file(fileName: str) -> list[int]:
    file = open(fileName)
    lines = file.readlines()
    priorities: list[int] = []

    for line in lines:
        line = line.strip()
        mid = len(line) // 2
        left = line[:mid]
        right = line[mid:]
        priorities.append(determine_priority(find_the_type(left, right)))

    return priorities

def main():
    priorities = traverse_file('input3.txt')
    print(priority_sum(priorities))

main()