#################################################
# hw5.py
# name: Mahtabin Rodela
# andrew id: mrozbu
#################################################

import cs112_s22_week5_linter
import math, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def rgbString(red, green, blue):
     return f'#{red:02x}{green:02x}{blue:02x}'

#################################################
# Part A
#################################################

def nondestructiveRemoveRowAndCol(A, row, col):
    # remember: do not copy or deepcopy A here.
    # instead, directly construct the result
    finalList =[]
    for i in range(len(A)):
        newList = []
        if i != row:
            for j in range(len(A[0])):
                if j != col:
                    newList.append(A[i][j])
            finalList.append(newList)
    return finalList

def destructiveRemoveRowAndCol(A, row, col):
    
    for elem in A:
        elem.pop(col)
    A.pop(row)
    
def getcol(m, col):
    colList = []
    for row in range(len(m)):
        val = m[row][col]
        colList.append(val)
    return colList
    
def getrow(m, row):
    return m[row]

def matrixMultiply(m1,m2):
    row1 = len(m1)
    row2 = len(m2)
    col1 = len(m1[0])
    col2 = len(m2[0])
  
    if col1 != row2:
        return None
    
    #row1, col2
    result = [ ([0] * col2) for row in range(row1) ]
    
    for row in range(len(result)):
        for col in range(len(result[0])):
            
            colList = getcol(m2, col)
            rowList = getrow(m1, row)
            product = dotProduct(rowList,colList)
            result[row][col] = product
    return result
    
def dotProduct(row, col):
    
    result =0
    for i in range(len(row)):
        product = row[i]*col[i]
        result += product
    return result
    

def isDuplicatedNumber(board):
    
    seen = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] not in seen:
                seen.append(board[row][col])
            else:
                return False
    return True
        
def findOne(board):
    for i in range (len(board)):
        for j in range (len(board[0])):
            #currentPosition
            startrow = i
            startcol = j
            currentval = board[i][j]
            if board[i][j] == 1:
                return startrow, startcol
    else:
        return -1, -1
        
def newPosition(board, startRow, startCol, nextTarget):
    (rows, cols) = (len(board), len(board[0]))
    for drow in [-1,0,1]:
        for dcol in [-1, 0, 1]:
            if (drow, dcol) == (0,0):
                continue
            else:
                row = startRow + drow
                col = startCol + dcol
                if (((row < 0) or (row >= rows) or 
                        col < 0) or (col >= cols)):
                    continue
                if board[row][col] == nextTarget:
                    return row, col
    return -1, -1
    
def isKingsTour(board):
    print(board)
    row = len(board)
    col = len(board[0])
    count = 1
    nextTarget = 2
    
    if (row != col) or isDuplicatedNumber(board)== False:
        return False
    
    startrow, startcol = findOne(board)
    if startrow == -1 and startcol ==-1:
        return False
    for _ in range(row*col-1):
        startrow, startcol  = newPosition(board, startrow, startcol, 
                    nextTarget)
        if startrow ==-1 and startcol ==-1:
            return False
        nextTarget +=1
    return True
    

#################################################
# Part B
#################################################
def checkValidlst(a):
    seen =[]
    for i in a:
        if isinstance(i, list): #checks type is only list
            for j in i:
                if isinstance(j, int) == False:
                    return False #checks only int present in list
                else:
                    if j in seen:
                        return False
                    else:
                        seen.append(j)
        else:
            return False
        for i in range(len(a)):#Checks consistent column length
            if len(a[0]) != len(a[i]):
                return False
    return True

def getrow(a, row):
    return a[row]
    
def getCol(a, col):
    colList = []
    for row in range(len(a)):
        val = a[row][col]
        colList.append(val)
    return colList

def getDiag(a):
    row = len(a)
    col = len(a[0])
    digonalList_negativeSlope =[]
    digonalList_positiveslope =[]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i ==j:
                digonalList_negativeSlope.append(a[i][j])
            if ((i + j) == (col - 1)):
                digonalList_positiveslope.append(a[i][j])
    return digonalList_negativeSlope, digonalList_positiveslope

def isMagicSquare(a):
    
    if checkValidlst(a):
        TrueSum = sum(a[0])
        for i in range(len(a)):
            rowList = getrow(a, i)
            colList = getCol(a, i)
            if sum(rowList) !=TrueSum and sum(colList) != TrueSum:
                return False
            
        digonal_1, digonal_2 = getDiag(a)
        if (sum(digonal_2)== TrueSum and sum(digonal_1) == TrueSum and 
            sum(digonal_1) == sum(digonal_2)):
            # print ("Diagonals don't match")
            return True
        else:
            return False
    return False
            

def wordSearch(board, word):
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != None):
                return result
    return None

def wordSearchFromCell(board, word, startRow, startCol):
    for drow in [-1, 0, +1]:
        for dcol in [-1, 0, +1]:
            if (drow, dcol) != (0, 0):
                result = wordSearchFromCellInDirection(board, word,
                    startRow, startCol,drow, dcol)
                if (result != None):
                    return result
    return None

def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):
    
    (rows, cols) = (len(board), len(board[0]))
    dirNames = [ ["up-left"  ,   "up", "up-right"],
                 ["left"     ,   ""  , "right"   ],
                 ["down-left", "down", "down-right" ] ]
    wordIndex = 0
    boardIndex =0
    while wordIndex < len(word):
        
        row = startRow + boardIndex*drow
        col = startCol + boardIndex*dcol
        
        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols)):
            return None
        if (board[row][col] == word[wordIndex]):
            wordIndex += 1
        elif isinstance(board[row][col], int):
            wordIndex +=(board[row][col])
            if wordIndex > len(word):
                return False
        boardIndex+=1
    return (word, (startRow, startCol), dirNames[drow+1][dcol+1])
    
def wordSearchWithIntegerWildcards(board, word):
    if wordSearch(board, word):
        return True
    return False

def areLegalValues(values):
    seen =[]
    n = len(values)
    if isinstance(values, list): #checks type is only list
        for digit in values:
            if isinstance(digit, int) == False:
                    return False #checks only int present in list
            else:
                if digit != 0 and (digit in seen or digit<0 or digit>n):
                    
                    return False
                else:
                    seen.append(digit)
                    # print("Seen:", seen)
    else:
        return False
    return True
    
def isLegalRow(board, row):
    row = board[row]
    if areLegalValues(row):
        return True
    return False

def isLegalCol(board, col):
    colList = []
    for row in range(len(board)):
        val = board[row][col]
        colList.append(val)
    if areLegalValues(colList):
        return True
    return False
    
def isLegalBlock(board : list, block: int):
    n = int(math.sqrt(len(board))) #block size
    row = (block//n)*n
    col = (block%n)*n
    blockList = []
    for checkRow in range(row, row+n):
        for checkCol in range(col, col+n):
            blockList.append(board[checkRow][checkCol])
    if areLegalValues(blockList):
        return True
    return False
    

def isLegalSudoku(board):
    for i in range(len(board)):
        if not isLegalRow(board, i):
            return False
        if not isLegalCol(board, i):
            return False
        if not isLegalBlock(board, i):
            return False
    return True
    
            

#################################################
# Bonus/Optional
#################################################

#def makeWordSearch(wordList, replaceEmpties):
    #return 42

#################################################
# Test Functions (#ignore_rest)
#################################################

def testIsMagicSquare():
    print("Testing isMagicSquare()...", end="")
    assert(isMagicSquare([[42]]) == True)
    assert(isMagicSquare([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == True)
    assert(isMagicSquare([[4-7, 9-7, 2-7], [3-7, 5-7, 7-7], [8-7, 1-7, 6-7]])
           == True)
    a = [[7  ,12 ,1  ,14],
         [2  ,13 ,8  ,11],
         [16 ,3  ,10 ,5],
         [9  ,6  ,15 ,4]]
    assert(isMagicSquare(a))
    a = [[113**2, 2**2, 94**2],
         [ 82**2,74**2, 97**2],
         [ 46**2,127**2,58**2]]
    assert(isMagicSquare(a) == False)
    a = [[  35**2, 3495**2, 2958**2],
         [3642**2, 2125**2, 1785**2],
         [2775**2, 2058**2, 3005**2]]
    assert(isMagicSquare(a) == False)
   
    assert(isMagicSquare([[1, 2], [2, 1]]) == False)
    assert(isMagicSquare([[0], [0]]) == False) # Not square!
    assert(isMagicSquare([[1, 1], [1, 1]]) == False) # repeats
    assert(isMagicSquare('do not crash here!') == False)
    assert(isMagicSquare(['do not crash here!']) == False)
    assert(isMagicSquare([['do not crash here!']]) == False)
    assert(isMagicSquare([[8, 1,6], [3, 5,7],[4,9]]) == False)
    assert(isMagicSquare([42]) == False)
    print("Passed!")

def testNondestructiveRemoveRowAndCol():
    print('Testing nondestructiveRemoveRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    aCopy = copy.copy(a)
    assert(nondestructiveRemoveRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == aCopy)
    assert(nondestructiveRemoveRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == aCopy)
    b = [[37, 78, 29, 70, 21, 62, 13, 54, 5],
    [6,     38, 79, 30, 71, 22, 63, 14, 46],
    [47,    7,  39, 80, 31, 72, 23, 55, 15],
    [16,    48, 8,  40, 81, 32, 64, 24, 56],
    [57,    17, 49, 9,  41, 73, 33, 65, 25],
    [26,    58, 18, 50, 1,  42, 74, 34, 66], 
    [67,    27, 59, 10, 51, 2,  43, 75, 35],
    [36,    68, 19, 60, 11, 52, 3,  44, 76],
    [77,    28, 69, 20, 61, 12, 53, 4,  45]]

    c = [[37, 78, 29, 70, 21, 62,     54, 5],
    [6,     38, 79, 30, 71, 22,     14, 46],
    [47,    7,  39, 80, 31, 72,     55, 15],
    [16,    48, 8,  40, 81, 32,     24, 56],
    [57,    17, 49, 9,  41, 73,     65, 25],
    [26,    58, 18, 50, 1,  42,     34, 66], 
    [67,    27, 59, 10, 51, 2,      75, 35],
    [36,    68, 19, 60, 11, 52, 44, 76]]

    bCopy = copy.copy(b)
    assert(nondestructiveRemoveRowAndCol(b,8,6) == c)
    assert(b == bCopy)
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    A = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]
        ]
    B = [ [ 2, 3, 5],
          [ 0, 1, 3]
        ]
    assert(destructiveRemoveRowAndCol(A, 1, 2) == None)
    assert(A == B) # but now A is changed!
    A = [ [ 1, 2 ], [3, 4] ]
    B = [ [ 4 ] ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    A = [ [ 1, 2 ] ]
    B = [ ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    print("Passed!")

def testMatrixMultiply():
    print("Testing matrixMultiply()...", end='')
    m1 = [[1,2],
          [3,4]] # 2x2
    m2 = [[4],
          [5]]     # 2x1
    m3 = [[14],
          [32]]
    assert(matrixMultiply(m1,m2) == m3) 
    assert(matrixMultiply([[3, 7], [4, 5], [5, 4], [5, 6], [8, 9], [7, 4]], 
                          [[9, 8, 3],
                           [5, 1, 3]])==
                          [[62, 31, 30],
                           [61, 37, 27],
                           [65, 44, 27],
                           [75, 46, 33],
                           [117, 73, 51],
                           [83, 60, 33]])
    assert matrixMultiply([[8]],[[5]])==[[40]]
    print("Passed!")

def testIsKingsTour():
    print("Testing isKingsTour()...", end="")
    a = [ [  3, 2, 1 ],
          [  6, 4, 9 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  2, 8, 9 ],
          [  3, 1, 7 ],
          [  4, 5, 6 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 9 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 1 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 9 ],
          [  6, 4, 1 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 1 ],
          [  6, 4, 0 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  1, 2, 3 ],
          [  7, 4, 8 ],
          [  6, 5, 9 ] ]
    assert(isKingsTour(a) == False)
    a = [ [ 3, 2, 1 ],
          [ 6, 4, 0 ],
          [ 5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    print("Passed!")

def testWordSearchWithIntegerWildcards():
    print("Testing wordSearchWithIntegerWildcards()...", end='')
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
            ]
    assert(wordSearchWithIntegerWildcards(board, "dog") == True)
    assert(wordSearchWithIntegerWildcards(board, "cat") == True)
    assert(wordSearchWithIntegerWildcards(board, "tad") == True)
    assert(wordSearchWithIntegerWildcards(board, "cow") == False)
    board = [ [ 'd', 'o',  1  ],
              [  3 , 'a', 'c' ],
              [ 'o', 'q' ,'t' ],
            ]
    assert(wordSearchWithIntegerWildcards(board, "z") == True)
    assert(wordSearchWithIntegerWildcards(board, "zz") == False)
    assert(wordSearchWithIntegerWildcards(board, "zzz") == True)
    assert(wordSearchWithIntegerWildcards(board, "dzzzo") == True)
    assert(wordSearchWithIntegerWildcards(board, "dzzo") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzd") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzo") == True)
    board = [ [ 3 ] ]
    assert(wordSearchWithIntegerWildcards(board, "zz") == False)
    assert(wordSearchWithIntegerWildcards(board, "zzz") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzz") == False)
    board = [ [ 'a', 'b', 'c' ],
              [ 'd',  2 , 'e' ],
              [ 'f', 'g', 'h' ]]
    assert(wordSearchWithIntegerWildcards(board, "aqqh") == True)
    assert(wordSearchWithIntegerWildcards(board, "aqqhh") == False)
    assert(wordSearchWithIntegerWildcards(board, "zz") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzc") == True)
    assert(wordSearchWithIntegerWildcards(board, "zaz") == False)
    print("Passed!")

def testIsLegalSudoku():
    # From Leon Zhang!
    print("Testing isLegalSudoku()...", end="")
    board = [[0]]
    assert isLegalSudoku(board) == True
    board = [[1]]
    assert isLegalSudoku(board) == True

    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [[0, 4, 0, 0],
             [0, 0, 3, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 2]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 1, 2],
             [2, 1, 4, 3],
             [4, 3, 2, 1]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 4, 2],
             [2, 4, 4, 3],
             [4, 3, 2, 1]]    
    assert isLegalSudoku(board) == False

    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    assert isLegalSudoku(board) == True
    
    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 9, 7, 9 ]
    ]
    assert isLegalSudoku(board) == False
    board = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6, 8]]
    assert isLegalSudoku(board) == True
    # last number is supposed to be 8, not 10
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6,10]]
    assert isLegalSudoku(board) == False
    print("Passed!")

def testMakeWordSearch():
    print("Testing makeWordSearch()...", end="")
    board = makeWordSearch([], False)
    assert(board == None)

    board = makeWordSearch(["ab"], False)
    assert(board == [['a', 'b'], ['-', '-'] ])
    board = makeWordSearch(["ab"], True)
    assert(board == [['a', 'b'], ['c', 'd'] ])
    board = makeWordSearch(["ab", "bc", "cd"], False)
    assert(board == [['a', 'b'], ['c', 'd'] ])
    board = makeWordSearch(["ab", "bc", "cd", "de"], False)
    assert(board == [['a', 'b', '-'], ['c', 'd', '-'], ['d', 'e', '-']])
    board = makeWordSearch(["ab", "bc", "cd", "de"], True)
    assert(board == [['a', 'b', 'a'], ['c', 'd', 'c'], ['d', 'e', 'a']])

    board = makeWordSearch(["abc"], False)
    assert(board == [['a', 'b', 'c'], ['-', '-', '-'], ['-', '-', '-']])
    board = makeWordSearch(["abc"], True)
    assert(board == [['a', 'b', 'c'], ['c', 'd', 'a'], ['a', 'b', 'c']])

    board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], False)
    assert(board == [['a', 'b', 'c'], ['d', 'e', '-'], ['c', 'f', 'g']])
    board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], True)
    assert(board == [['a', 'b', 'c'], ['d', 'e', 'a'], ['c', 'f', 'g']])

    board = makeWordSearch(["abcd", "abc", "dcb"], False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['-', '-', '-', '-'], 
                     ['-', '-', '-', '-'],
                     ['-', '-', '-', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya"], False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', '-', '-'], 
                     ['-', 'a', '-', '-'],
                     ['-', '-', '-', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya", "bax", "dca"],
                           False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', 'c', '-'], 
                     ['-', 'a', '-', '-'],
                     ['-', '-', 'b', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya", "bax", "dca"],
                           True)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', 'c', 'a'], 
                     ['b', 'a', 'd', 'e'],
                     ['c', 'e', 'b', 'a']])

    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testMatrixMultiply()
    testIsKingsTour()

    # Part B:
    testIsMagicSquare()
    testWordSearchWithIntegerWildcards()
    testIsLegalSudoku()

    # Bonus:
    # testMakeWordSearch()

def main():
    cs112_s22_week5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()

'''
def lightsOut(board):
    
    board = [[0,0,0,1,1],[1,0,0,1,1]] ##assuming board is always legal
    
    
    while boardHaslights(board) == True: ##Game not over
    
        playerInput = input("Please enter two number:")
    
        while checkValidity(playerInput, board)== False:
    
            print ("Please enter only two number, the row and col:")
            playerInput = input("Please enter a valid number:")
    
    
        row, col = findingRowcol(playerInput, board) ## extracting string row and 
                                              ## col the player entered
        if row == -1 or col ==-1:
            print ("Invalid row and col, Out of range")
        board = flip(row, col, board)
        print("Board", board)
        if boardHaslights(board): 
            continue
        else:
            print ("LightsOut, Finally Done!")
            print(board)
            break
    print ("GameOver")
    
def checkValidity(s, board):
    row = len(board)
    col = len(board[0])
    for item in s.split():
        if item.isdigit() and int(item) <=row and int(item) <= col:
            return True
        return False
    return False

    
def findingRowcol(s, board):
    if checkValidity(s, board):
        s = s.split()
        row = int(s[0])
        print (row)
        col = int(s[1])
        return row, col
    return -1,-1
    

def flip(row, col, board):
    rows = len(board)
    cols = len(board[0])
    startRow = row
    startCol = col
    if board[row][col] == 0: ##assigning 'flips' to the row, col 
        board[row][col] = 1
    if board[row][col] == 1: 
        board[row][col]= 0     
    for drow in [-1,0,1]:
        for dcol in [-1, 0, 1]:
            if (drow, dcol) == (0,0):
                continue
            else:
                row = startRow + drow
                col = startCol + dcol
                if (((row < 0) or (row >= rows) or 
                        col < 0) or (col >= cols)):
                    continue
                if board[row][col] == 0:
                    board[row][col] =1
                elif board[row][col] == 1:
                    board[row][col] =0
                
    return board
        
            
def boardHaslights(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                return True
    return False
    
def main():
    board = [[0,0,0,1,1],[1,0,0,1,1]]
    print(lightsOut(board))
    
'''


