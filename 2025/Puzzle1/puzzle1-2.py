

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

    # This code sux :)
    for turn in arr:
        direction, notch = turn[0],int(turn[1:])
        fromZero = pos == 0
        clicks += int(notch/100)
        notch = int(notch%100)
        if direction == "L":
            pos -= notch
            if pos < 0:
                if not fromZero:
                    clicks += 1
                pos = 100 + pos
        elif direction == "R":
            pos += notch
            if pos > 99:
                pos = pos - 100
                if pos != 0:
                    clicks += 1
        if pos == 0:
            clicks += 1

        print(turn)
        print(pos)
        print(clicks)


    print(clicks)

main()