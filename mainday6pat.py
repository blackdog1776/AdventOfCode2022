# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
   import pandas as pd

   with open("/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday6.txt", "r") as file:
      input = file.read()

   # print(input)
   index = -1
   char_list = []
   for char in input:
      index = index + 1
      if char not in char_list:
         char_list.append(char)
      else:
         char_list.clear()

      #print(char_list)
      if len(char_list) == 13:
         print(index)
         break
   # Part 2
   print(len(input))