def find_the_type_pt_one(left: str, right: str) -> str:
    type = ''
    for l in left:
        for r in right:
            if l == r:
                type = r
    return type

def find_the_type_pt_two(rucksacks: list[str]) -> str:
    type = ''
    for f in rucksacks[0]:
        if rucksacks[1].find(f) >= 0:
            if rucksacks[2].find(f) >=0:
                type = f
    return type

def determine_priority(type: str) -> int:
    code = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return code.find(type) + 1

def priority_sum(priorities: list[int]) -> int:
    sum = 0
    for priority in priorities:
        sum += priority
    return sum

def traverse_file_pt_one(fileName: str) -> list[int]:
    file = open(fileName)
    lines = file.readlines()
    priorities: list[int] = []

    for line in lines:
        line = line.strip()
        mid = len(line) // 2
        left = line[:mid]
        right = line[mid:]
        priorities.append(determine_priority(find_the_type_pt_one(left, right)))

    return priorities

def traverse_file_pt_two(fileName: str) -> list[int]:
    file = open(fileName)
    lines = file.readlines()
    priorities: list[int] = []
    i = 0
    rucksacks = ['', '', '']

    for line in lines:
        line = line.strip()
        rucksacks[i] = line
        if i == 2:
            priorities.append(determine_priority(find_the_type_pt_two(rucksacks)))
            i = 0
        else:
            i += 1

    return priorities

def main():
    priorities = traverse_file_pt_one('input3.txt')
    print(priority_sum(priorities))

    priorities = traverse_file_pt_two('input3.txt')
    print(priority_sum(priorities))

main()