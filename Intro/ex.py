# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
# {
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }
# Your algorithm should return 41, the sum of the values 23 and 18.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# d = {
#     "cat": "bob",
#     "dog": 23,
#     19: 18,
#     90: "fish"
# }
# total = 0
# for value in d.values():
#     if type(value) is int:
#         total += value
# print(total)

# function compareTwoArrays(arr1, arr2) {
#     # compare the two arrays and if they have the same numbers return true otherwise
#     for(let i = 0; i > arr1.length; i++){
#         if (length(arr1) != length(arr2)){
#             return false
#         }
#         else if (arr1[i] === arr2[i]) {
#             return true
#         }
#     }


# }

# // Test cases to verify
# console.log(compareTwoArrays([1,2,3], [1,2,3])); // true
# console.log(compareTwoArrays([3,3,3], [1,2,3])); // false
# console.log(compareTwoArrays([1,2,3,4], [1,2,3])); // false
# console.log(compareTwoArrays([1,2,3], [1,2,3,4])); // false

# // If you decide to attempt nested arrays
# const a = [1,['a', 'b'],3,4];
# const b = [1,['a', 'b'],3,4];
# console.log(compareTwoArrays(a, b)); // true

# const a = [1,[‘z', ‘z'],3,4];
# const b = [1,['a', 'b'],3,4];
# console.log(compareTwoArrays(a, b)); // false

