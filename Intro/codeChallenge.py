'''
You and your friends are all fans of the hit TV show ThroneWorld and like to discuss it on social media. Unfortunately, some of your friends don't watch every new episode the minute it comes out. Out of consideration for them you would like to obfuscate your status updates so as to keep them spoiler-free.

You settle on a route cipher, which is a type of transposition cipher. Given a message and integers r and c, to compute the route encryption of the message:

Write out the message row-wise in a grid with r rows and c columns
then read the message column-wise.

You are guaranteed that r * c == len(message).

Your task is to write a function that, given a message, r, and c, returns the route encryption of the message.

Example:

message = "One does not simply walk into Mordor", r = 6, c = 6

O n e   d o
e s   n o t
  s i m p l
y   w a l k
  i n t o  
M o r d o r

-> "Oe y Mnss ioe iwnr nmatddoploootlk r"

Other examples:

message = "1.21 gigawatts!", c = 5, r = 3
1 . 2
1   g
i g a
w a t
t s !

-> "11iwt. gas2gat!"

message = "1.21 gigawatts!", r = 3, c = 5 -> "1ga.it2gt1as w!"

Complexity analysis:

n: the length of the message



Example:

message = "One does not simply walk into Mordor", r = 6, c = 6

O n e   d o
e s   n o t
  s i m p l
y   w a l k
  i n t o  
M o r d o r

-> "Oe y Mnss ioe iwnr nmatddoploootlk r"

'''

# Plan:
# Iterate through the message and break to a new row once I reach the len(row)
message = "One does not simply walk into Mordor"
def encryption(message, r, c):
    prev = 0
    next = r
    new_list = []
#     newString= ''
    for element in message:
        sliceString = slice(prev, next)
        prev += r
        next += r
        # new_list.append(sliceString)
        # print('helooo',new_list)
        print(message[sliceString][0])

print(encryption(message, 6,6))


# message1 = "One does not simply walk into Mordor"
# r1 = 6
# c1 = 6

# message2 = "1.21 gigawatts!"
# r2 = 5
# c2 = 3
# r3 = 3
# c3 = 5
