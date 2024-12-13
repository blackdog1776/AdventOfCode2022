# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   import pandas as pd

   with open("/Users/pat/Desktop/AdventOfCode2023/Files to Import/input.txt", "r") as file:
      input = file.read()

   #print(input)
   string_list = input.splitlines()
   string_split_list = []
   current_list = []
   # print(string_list)
   for item in string_list:
      if item == '':  # Split on blanks
         if current_list:
            string_split_list.append(current_list)
            current_list = []
      else:
         current_list.append(item)

   # Append the last group if any
   if current_list:
      string_split_list.append(current_list)

   #print(string_split_list)

   int_list = [[int(item) for item in sublist] for sublist in string_split_list]
   #print(int_list)

   sum_list = []
   for line in int_list:
      sum_list.append(sum(line))

   top_3_largest = sorted(sum_list, reverse=True)[:3]
   print(sum(top_3_largest))

   # input = pd.read_csv("/Users/pat/Desktop/AdventOfCode2023/Files to Import/input.txt", header = None)
   # print(input)
   # elf_cal_list = []
   #
   # for index, row in input.iterrows():
   #    row_str = row.to_string(index=False)
   #    el

