# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
from collections import defaultdict

from collections import defaultdict

class Directory:
    def __init__(self):
        self.files = []  # Stores file sizes
        self.subdirs = {}  # Maps subdirectory names to Directory objects

    def add_file(self, size):
        self.files.append(size)

    def add_subdir(self, name):
        if name not in self.subdirs:
            self.subdirs[name] = Directory()
        return self.subdirs[name]

    def get_total_size(self):
        # Recursively calculates total size of the directory
        total = sum(self.files)
        for subdir in self.subdirs.values():
            total += subdir.get_total_size()
        return total

def parse_filesystem(input_lines):
    root = Directory()
    cwd = [root]  # Stack to track the current working directory

    for line in input_lines:
        line = line.strip()
        if line.startswith('$ cd'):
            _, _, path = line.split()
            if path == '/':
                cwd = [root]
            elif path == '..':
                cwd.pop()
            else:
                cwd.append(cwd[-1].add_subdir(path))
        elif line.startswith('$ ls'):
            continue  # Skip ls commands
        else:
            size_or_dir, name = line.split(maxsplit=1)
            if size_or_dir == 'dir':
                cwd[-1].add_subdir(name)
            else:
                cwd[-1].add_file(int(size_or_dir))

    return root

def find_small_directories(root, size_limit):
    def traverse(directory):
        total_size = directory.get_total_size()
        if total_size <= size_limit:
            small_dirs.append(total_size)
        for subdir in directory.subdirs.values():
            traverse(subdir)

    small_dirs = []
    traverse(root)
    return sum(small_dirs)

def find_smallest_deletable_directory(root, total_disk_space, required_space):
    used_space = root.get_total_size()
    free_space = total_disk_space - used_space
    needed_space = required_space - free_space

    if needed_space <= 0:
        return 0  # No deletion needed

    def find_candidates(directory):
        total_size = directory.get_total_size()
        if total_size >= needed_space:
            candidates.append(total_size)
        for subdir in directory.subdirs.values():
            find_candidates(subdir)

    candidates = []
    find_candidates(root)
    return min(candidates) if candidates else None

if __name__ == '__main__':
    # Replace with your input file path
    input_file = '/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday7.txt'
    with open(input_file, 'r') as file:
        input_lines = file.readlines()

    filesystem = parse_filesystem(input_lines)
    size_limit = 100000
    result = find_small_directories(filesystem, size_limit)

    print(f'Sum of total sizes of directories with size at most {size_limit}: {result}')

    # Solve the second part
    total_disk_space = 70000000
    required_space = 30000000
    smallest_deletable = find_smallest_deletable_directory(filesystem, total_disk_space, required_space)

    print(f'Smallest directory size to delete to free up space: {smallest_deletable}')


