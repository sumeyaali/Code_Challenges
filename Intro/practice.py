# def reverseString(s): 
#   str = "" 
#   for i in s: 
#     # print(i)
#     str = i + str
#     print(i + str)
#   return str
# s = 'Geeksforgeeks'

# print(reverseString(s))
word = 'jksdofirwsjifdijjarehouvneec'

myCounter = {}

def iterate(string):

    # for(let i = 0; i < word.length; i++)
    for i in range(len(string)):
        if word[i] in myCounter:
            myCounter[word[i]] = myCounter[word[i]] + 1
        else:
            myCounter[word[i]] = 1

    #     if (myCounter[word[i]]) {
    #         // if letter is in my dictionary, than increment the value of the leter by 1, else add it to my dictionary
    #         myCounter[word[i]] = myCounter[word[i]] + 1
    #     }
    #     else {
    #       myCounter[word[i]] = 1
    #     }
    # }
    return myCounter
print(iterate(word))