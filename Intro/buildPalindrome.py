def buildPalindrome(st):
    length = len(st)
    for i in range(length):
        subString = st[i:length]
        if isPalindrome(subString):
            nonPalinPart = st[0:i]
            return st + nonPalinPart[::-1]
    return 'whatever'
    
def isPalindrome(string):
    return string == string[::-1]