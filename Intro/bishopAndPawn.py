def bishopAndPawn(bishop, pawn):
    letters = ['a','b','c','d','e','f','g','h']
    numbers = ['1','2','3','4','5','6','7','8']

#Separate bishop position in something like ['A','1']
    listBishop = list(bishop)

    listPawn = list(pawn)
#Check if the pawn is in a position that can be crossed
#Than can be +-1*(length of letters).

    for i in range(len(letters)):
        if listBishop[0] == letters[i]:
            idxBshp = i

        if listPawn[0] == letters[i]:
            idxPawn = i

    dstLtr = abs(idxBshp-idxPawn)

#So, there will be a match if the number coincide with +-1*(length of letters)

    if (int(listBishop[1]) == (int(listPawn[1]) - dstLtr) ) | (int(listBishop[1]) == (int(listPawn[1]) + dstLtr) ):
        return True
    else:
        return False