import re

def find_nums(line: str) -> int:
    print(line)
    nums = re.findall("[0-9]", line)
    print(nums)
    return int(nums[0] + nums[-1])



def traverse_file(fileName: str) -> list[int]:
    file = open(fileName)
    lines = file.readlines()
    sum = 0

    for line in lines:
        sum += find_nums(line)
    
    return sum


def main():
    print(traverse_file("input1.txt"))
main()