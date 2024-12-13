# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
def get_repeating_character(input_string):

   midpoint = len(input_string) // 2

   # Split the string into two parts and store them in a list
   split_strings = [input_string[:midpoint], input_string[midpoint:]]
   # Create an empty list to store the characters
   char_list = []
   repeating_char = ''

   # Iterate through each character in the string and append to the list
   for char in split_strings[0]:
      if char in split_strings[1]:
         repeating_char = char
         return repeating_char

def get_score_of_char(repeating_char, score_dict):
   score = 0
   score += score_dict[repeating_char]
   return score


def get_repeating_char2(string_list):
   str1 = string_list[0]
   str2 = string_list[1]
   str3 = string_list[2]

   repeating_char = ''
   for char in str1:
      if char in str2 and char in str3:
         repeating_char = char
         return repeating_char


if __name__ == '__main__':
   import pandas as pd

   score_dict = {
 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
}

   with open("/Users/pat/Desktop/AdventOfCode2023/Files to Import/inputday3.txt", "r") as file:
      input = file.read()

   string_list = input.splitlines()
   # total_score = 0
   # for line in string_list:
   #    repeating_char = get_repeating_character(line)
   #    total_score += get_score_of_char(repeating_char, score_dict)
   #
   # print(total_score)

   # Part 2
   # Split the list into sublists of 3 items each
   split_list = [string_list[i:i + 3] for i in range(0, len(string_list), 3)]

   total_score = 0
   for line in split_list:
      repeating_char = get_repeating_char2(line)
      total_score += get_score_of_char(repeating_char, score_dict)

   print(total_score)

