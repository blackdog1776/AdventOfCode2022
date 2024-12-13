# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# def get_move_nums(input_move_line):
#    numbers = re.findall(r'\d+', input_string)
#
#    # Convert the numbers to integers and assign to variables
#    num1, num2, num3 = map(int, numbers)
#    return num1, num2, num3
#
#
#
# #def move(input_move_line, input_stacks):
#
#
# def get_each_stack_as_list(input_stacks):
#    stack1 = ['[]', '[]', '[]', '[]', '[D]','[Z]','[T]','[H]']
#    stack2 = ['[]', '[S]', '[C]', '[G]', '[D]','[Z]','[T]','[H]']
#    stack3 = []
#    stack4 = []
#    stack5 = []
#    stack6 = []
#    stack7 = []
#    stack8 = []
#    stack9 = []

# def print_top_of_stacks(stacks):
#    for i, stack in enumerate(stacks, 1):
#       print(f'{stack[-1]}')
#
#
# def process_instructions(stacks, instructions):
#    for instruction in instructions:
#       parts = instruction.split()
#       num_items = int(parts[1])
#       source_stack = int(parts[3]) - 1
#       dest_stack = int(parts[5]) - 1
#
#       for _ in range(num_items):
#          item = stacks[source_stack].pop()
#          stacks[dest_stack].append(item)
#
#    return stacks

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   # with open("/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday5.txt", 'r') as file:
   #    input_lines = file.readlines()
   #
   # stacks = [[] for _ in range(9)]
   #
   # for line in input_lines[:-1]:
   #    for i in range(9):
   #       char = line[i * 4 + 1:i * 4 + 2].strip()
   #       if char:
   #          stacks[i].insert(0, char)
   #
   # with open("/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday5p2.txt", 'r') as file:
   #    instructions = file.readlines()
   #
   #
   # def process_instructions(stacks, instructions):
   #    for instruction in instructions:
   #       parts = instruction.split()
   #       num_items = int(parts[1])
   #       source_stack = int(parts[3]) - 1
   #       dest_stack = int(parts[5]) - 1
   #
   #       # Check if there are enough items in the source stack
   #       if len(stacks[source_stack]) < num_items:
   #          #print(f"Error: Not enough items in stack {source_stack + 1} to move {num_items} items.")
   #          continue  # Skip this instruction and move to the next
   #
   #       insert_crates = []
   #
   #       for _ in range(num_items):
   #          item = stacks[source_stack].pop()
   #          insert_crates.append(item)
   #       #print(insert_crates, instruction, source_stack, dest_stack)
   #
   #       for i in range(len(insert_crates)):
   #          item = insert_crates.pop()
   #          stacks[dest_stack].append(item)
   #
   #    return stacks
   #
   #
   # result = process_instructions(stacks, instructions)
   #
   #
   # def print_top_of_stacks(stacks):
   #    for i, stack in enumerate(stacks, 1):
   #       # Only print the top item if the stack is not empty
   #       if stack:
   #          print(f'{stack[-1]}')
   #       else:
   #          print("Stack is empty")  # You can choose a message like this if stack is empty
   #
   # # Process instructions and modify stacks
   # result = process_instructions(stacks, instructions)
   #
   # # Print the top items of the stacks
   # stacktop = print_top_of_stacks(result)

   # Part 2
   with open("/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday5.txt", 'r') as file:
      input_lines = file.readlines()

   stacks = [[] for _ in range(9)]

   for line in input_lines[:-1]:
      for i in range(9):
         char = line[i * 4 + 1:i * 4 + 2].strip()
         if char:
            stacks[i].insert(0, char)

   with open("/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday5p2.txt", 'r') as file:
      instructions = file.readlines()


   def process_instructions(stacks, instructions):
      for instruction in instructions:
         parts = instruction.split()
         num_items = int(parts[1])
         source_stack = int(parts[3]) - 1
         dest_stack = int(parts[5]) - 1
         substack = stacks[source_stack][-num_items:]
         stacks[source_stack] = stacks[source_stack][:-num_items]
         stacks[dest_stack].extend(substack)

      return stacks


   result = process_instructions(stacks, instructions)


   def print_top_of_stacks(stacks):
      for i, stack in enumerate(stacks, 1):
         print(f'{stack[-1]}')


   stacktop = print_top_of_stacks(result)

   print(stacktop)




