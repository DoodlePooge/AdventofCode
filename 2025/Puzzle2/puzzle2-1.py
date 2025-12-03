import re

def get_invalid_ids(min:int, max:int) -> [int]:
    ids = []
    while min <= max:
        s = str(min)
        match = re.match(r"^(\d+)\1$", s)
        if match is not None:
            ids.append(min)
        min+=1
    return ids

def traverse_file(fileName: str) -> [[int, int]]:
    file = open(fileName)
    lines = file.readlines()
    ranges = []
    matches = []
    for line in lines:
        matches.extend(re.findall(r"\d*-\d*", line))

    for match in matches:
        arr = match.split("-")
        ranges.append(arr)

    return ranges


def main():
    arr = traverse_file("input.txt")
    sum = 0

    for r in arr:
        ids = get_invalid_ids(int(r[0]),int(r[1]))
        for id in ids:
            sum += id
    
    print(sum)


main()