# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.


   


if __name__ == '__main__':
   import pandas as pd

   #input = pd.read_csv("/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday4.txt", header=None, sep=',')

   # rangepairs = []
   #
   # with open('/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday4.txt', 'r') as file:
   #    for line in file:
   #       range1, range2 = line.strip().split(',')
   #       start1, end1 = map(int, range1.split('-'))
   #       start2, end2 = map(int, range2.split('-'))
   #       rangepairs.append(((start1, end1), (start2, end2)))
   #
   # total = 0
   #
   # for range1, range2 in rangepairs:
   #    s1, e1 = range1
   #    s2, e2 = range2
   #    if ((s1 >= s2 and e1 <= e2) or (s1 <= s2 and e1 >= e2)):
   #       total += 1
   #
   # print(total)

   # Part 2
   rangepairs = []

   with open('/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday4.txt', 'r') as file:
      for line in file:
         range1, range2 = line.strip().split(',')
         start1, end1 = map(int, range1.split('-'))
         start2, end2 = map(int, range2.split('-'))
         rangepairs.append(((start1, end1), (start2, end2)))

   total = 0

   for range1, range2 in rangepairs:
      s1, e1 = range1
      s2, e2 = range2
      if ((e1 >= s2 and s1 <= e2)):
         total += 1

   print(total)
