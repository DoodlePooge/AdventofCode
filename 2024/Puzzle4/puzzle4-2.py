def is_mas(s: str) -> bool:
    return s == "MAS" or s == "SAM"

def check_adjacent(x: int, y: int, grid:[str]) -> int:
    occurrences = 0

    if y > 0 and y < len(grid) - 1 and x > 0 and x < len(grid[0]) - 1:
        if is_mas(grid[y-1][x-1] + grid[y][x] + grid[y+1][x+1]) and is_mas(grid[y-1][x+1] + grid[y][x] + grid[y+1][x-1]):
            occurrences += 1

    return occurrences

def traverse_file(fileName: str) -> [[int]]:
    file = open(fileName)
    lines = file.read().split()

    return lines


def main():
    grid = traverse_file("input.txt")
    sum = 0

    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "A":
                sum += check_adjacent(j, i, grid)

    print(sum)

main()