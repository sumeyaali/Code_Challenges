def reverse(self, x: int) -> int:
#         create x to be a string that holds the abs value of x
        reversed = str(abs(x))
#     strip the ending/leading zeros
        reversed = reversed.strip()
#     reverse each digit from the end
        reversed = reversed[::-1]
#     return x to be an integer
        output = int(reversed)
        
        if output >= 2**31 or output <= -2**31:
            return 0
        elif x < 0:
            return -1 * output
        else:
            return output