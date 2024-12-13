# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
from collections import defaultdict

from collections import defaultdict

def get_border_num(input):
    visible_count = 0
    visible_count += 2*(len(input[0]))
    visible_count += 2*(len(input) - 2)
    return visible_count

def get_visible_from_up(input):
    visible_count = 0
    currow = -1
    for line in input:
        currow += 1
        currchar = -1
        for char in line:
            currchar +=1
            if currow == 0:
                visible_count +=1

            # Get List of nums in same column
            column_nums = []
            for num in range(currow):
                if input[num][currchar] != '\n':
                    column_nums.append(input[num][currchar])
            column_nums.pop()
            print(max(column_nums))







if __name__ == '__main__':
    # Replace with your input file path
    with open('/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday8.txt', "r") as f:
        grid = [list(map(int, line.strip())) for line in f.readlines()]


    def visible(grid, x, y):
        if all(grid[y][i] < grid[y][x] for i in range(x)):
            return True
        if all(grid[y][i] < grid[y][x] for i in range(x + 1, len(grid[0]))):
            return True
        if all(grid[i][x] < grid[y][x] for i in range(y)):
            return True
        if all(grid[i][x] < grid[y][x] for i in range(y + 1, len(grid))):
            return True

        return False


    def find_visible_points(grid):
        visible_points = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if visible(grid, x, y):
                    visible_points.add((x, y))

        return visible_points


    visible_points = find_visible_points(grid)

    print(len(visible_points))




