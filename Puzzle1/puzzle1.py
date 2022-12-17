
def add_calories_held(calories: list[int]) -> int:
    sum = 0
    for cal in calories:
        sum += cal
    return sum

def find_max_calories_held(elves: list[int]) -> int:
    maxCals = 0
    for elf in elves:
        if elf > maxCals:
            maxCals = elf
    return maxCals

def find_top_three_calories_held(elves: list[int]) -> int:
    mergesort(elves)
    return add_calories_held(elves[:3])

def mergesort(arr: list[int]):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
 
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def traverse_file(fileName: str) -> list[int]:
    file = open(fileName)
    lines = file.readlines()
    elves: list[int] = []
    calories: list[int] = []

    for line in lines:
        if line == '\n':
            elves.append(add_calories_held(calories))
            calories = []
        else:
            if line.strip():
                calories.append(int(line))
    
    elves.append(add_calories_held(calories))
    return elves


def main():
    print(find_max_calories_held(traverse_file("input1.txt")))
    print(find_top_three_calories_held(traverse_file("input1.txt")))
main()