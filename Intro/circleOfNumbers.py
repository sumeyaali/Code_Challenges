def circleOfNumbers(n, firstNumber):
    #  starting num + n / 2 => num you will land on
    if firstNumber < (n/2):
        return firstNumber + (n/2)
    elif firstNumber >= (n/2):
        return firstNumber - (n/2)