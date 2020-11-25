# Given a hashmap where the keys are integers, print out all of the values of the hashmap in reverse order, ordered by the keys.
# For example, given the following hashmap:
# {
#   14: "vs code",
#   3: "window",
#   9: "alloc",
#   26: "views",
#   4: "bottle",
#   15: "inbox",
#   79: "widescreen",
#   16: "coffee",
#   19: "tissue",
# }
# The expected output is:
# widescreen
# views
# tissue
# coffee
# inbox
# vs code
# alloc
# bottle
# window
# since "widescreen" has the largest integer key, "views" has the second largest, etc.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# words = {
#   14: "vs code",
#   3: "window",
#   9: "alloc",
#   26: "views",
#   4: "bottle",
#   15: "inbox",
#   79: "widescreen",
#   16: "coffee",
#   19: "tissue",
# }

# arr = []
# for key in words:
#     # print(key)
#     arr.append(key)

# arr.sort()
# arr.reverse()
# print(arr)

# for value in arr:
#     print(words[value])
   

# Do not remove these imports. You may add others if you wish.
import sys
# Args:
#    matrix: an NxN list of lists containing the matrix to check
# Returns:
#    The string "VALID" if matrix contains a valid sub-sudoku solution, and
#    "INVALID" otherwise
def check_sub_sudoku(mat):
  # Your code here.
# 1. loop through the row
# 2. loop through the column
# 3. check if each number is less or === to the length of row/column
  length = len(mat)
  for row in range(length):
    for column in range(length):
      if mat[row][column] > length or mat[row][column] < 1:
        return 'INVALID'
  for row in range(length):
    if len(set(mat[row])) != len(mat[row]):
      return 'INVALID'
  columnArray = []
  for column in range(length):
    for row in range(length):
      columnArray.append(mat[row][column])
      if len(set(columnArray)) != len(columnArray):
        return 'INVALID'
    columnArray = []
  return "VALID"