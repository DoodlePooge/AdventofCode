def is_contained(sec1: str, sec2: str) -> bool:
    first: list[int] = sec1.split('-')
    second: list[int] = sec2.split('-')

    return (first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1])

def does_overlap(sec1: str, sec2: str) -> bool:
    first: list[int] = sec1.split('-')
    second: list[int] = sec2.split('-')

    if first[0] == second[0] or first[0] == second[1] or first[1] == second[0] or first[1] == second[1]:
        return True

    if first[0] < second[0]:
        if first[1] >= second[1]:
            return True
        else:
            return first[1] > second[0]
    else:
        if first[1] <= second[1]:
            return True
        else:
            return first[1] < second[0]


def total_contained(assignments: list[bool]) -> int:
    sum = 0
    for assignment in assignments:
        if assignment:
            sum += 1
    return sum

def traverse_file_pt_one(fileName: str) -> list[bool]:
    file = open(fileName)
    lines = file.readlines()
    assignments: list[bool] = []

    for line in lines:
        sections = line.split(',')
        assignments.append(is_contained(sections[0], sections[1].strip()))

    return assignments

def traverse_file_pt_two(fileName: str) -> list[bool]:
    file = open(fileName)
    lines = file.readlines()
    assignments: list[bool] = []

    for line in lines:
        sections = line.split(',')
        assignments.append(does_overlap(sections[0], sections[1].strip()))

    return assignments

def main():
    assignments1 = traverse_file_pt_one('input4.txt')
    print(assignments1)
    print(total_contained(assignments1))
    assignments2 = traverse_file_pt_two('input4.txt')
    print(assignments2)
    print(total_contained(assignments2))

main()