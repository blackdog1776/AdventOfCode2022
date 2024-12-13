# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def get_both_actions(input_df_line):
   opponent = input_df_line[0]
   me = input_df_line[1]
   return opponent, me

def get_score(opponent, me):
   score = 0
   if me == 'X':
      score += 1
   elif me == 'Y':
      score += 2
   elif me == 'Z':
      score += 3

   if (opponent == 'A' and me == 'X') or (opponent == 'B' and me == 'Y') or (opponent == 'C' and me == 'Z'):
      score += 3
   elif (opponent == 'A' and me == 'Y') or (opponent == 'B' and me == 'Z') or (opponent == 'C' and me == 'X'):
      score += 6
       
   return score


def get_score2(opponent, me):
   score = 0

   if opponent == 'A':
      if me == 'X':
         score += 3
      elif me == 'Y':
         score += 4
      elif me == 'Z':
         score += 8
   elif opponent == 'B':
      if me == 'X':
         score += 1
      elif me == 'Y':
         score += 5
      elif me == 'Z':
         score += 9
   elif opponent == 'C':
      if me == 'X':
         score += 2
      elif me == 'Y':
         score += 6
      elif me == 'Z':
         score += 7

   return score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   import pandas as pd

   input = pd.read_csv("/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday2.txt", header = None, sep = ' ')
   # print(input)

   total_score = 0
   for index, line in input.iterrows():
      opponent, me = get_both_actions(line)
      curr_score = get_score2(opponent, me)
      total_score +=curr_score

   print(total_score)

   #Part 2

   # string_var1 = str(df.loc[0, 'column1'])
   # string_var2 = str(df.loc[0, 'column2'])


