def checkPalindrome(inputString):
    reversedstring=''.join(reversed(inputString))
    if reversedstring == inputString:
        return True
    else:
        return False