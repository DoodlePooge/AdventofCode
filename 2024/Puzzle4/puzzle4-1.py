import re

def is_mas(s: str) -> int:
    if s == "MAS":
        return 1

    return 0

def check_adjacent(x: int, y: int, grid:[str]) -> int:
    occurrences = 0
    
    if y > 2:
        occurrences += is_mas(grid[y-1][x] + grid[y-2][x] + grid[y-3][x])
        if x > 2:
            occurrences += is_mas(grid[y-1][x-1] + grid[y-2][x-2] + grid[y-3][x-3])

        if x < len(grid[0]) - 3:
            occurrences += is_mas(grid[y-1][x+1] + grid[y-2][x+2] + grid[y-3][x+3])
    
    if y < len(grid) - 3:
        occurrences += is_mas(grid[y+1][x] + grid[y+2][x] + grid[y+3][x])
        if x > 2:
            occurrences += is_mas(grid[y+1][x-1] + grid[y+2][x-2] + grid[y+3][x-3])

        if x < len(grid[0]) - 3:
            occurrences += is_mas(grid[y+1][x+1] + grid[y+2][x+2] + grid[y+3][x+3])

    return occurrences

def traverse_file(fileName: str) -> [[int]]:
    file = open(fileName)
    lines = file.read()

    return lines


def main():
    grid = traverse_file("input.txt")
    rows = grid.split()
    sum = 0
    xmas = re.findall(r"(?=(XMAS|SAMX))", grid)
    sum += len(xmas)
    for i, line in enumerate(rows):
        for j, char in enumerate(line):
            if char == "X":
                sum += check_adjacent(j, i, rows)

    print(sum)

main()