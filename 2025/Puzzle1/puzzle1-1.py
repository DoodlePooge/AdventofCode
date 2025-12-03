

def traverse_file(fileName: str) -> [str]:
    file = open(fileName)
    lines = file.readlines()
    arr = []

    for line in lines:
        arr.append(line)
    return arr


def main():
    arr = traverse_file("input.txt")
    clicks = 0
    pos = 50

    for turn in arr:
        direction, notch = turn[0],int(turn[1:])
        if direction == "L":
            pos -= notch
            while pos < 0:
                pos = 100 + pos
        elif direction == "R":
            pos += notch
            while pos > 99:
                pos = pos - 100
        if pos == 0:
            clicks += 1


    print(clicks)

main()