import re

def find_nums(line: str) -> int:
    legend = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    nums = re.findall(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
    if len(nums[0]) > 1:
        nums[0] = legend[nums[0]]
    if len(nums[-1]) > 1:
        nums[-1] = legend[nums[-1]]
    print(int(nums[0] + nums[-1]))
    return int(nums[0] + nums[-1])



def traverse_file(fileName: str) -> list[int]:
    file = open(fileName)
    lines = file.readlines()
    sum = 0

    for line in lines:
        sum += find_nums(line)
    return sum


def main():
    print(traverse_file("input2.txt"))
main()