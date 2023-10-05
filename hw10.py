#################################################
# hw10.py
#
# Your name: Mahtabin Rodela
# Your andrew id: mrozbu
#################################################

import cs112_s22_week10_linter
import math, os

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def findLargestFile(path):
    # Wrapper to extract just the bestPath from the helper
    # function that returns both bestPath and bestSize
    bestPath = findLargestFileAndSize(path)[0]
    return bestPath

def findLargestFileAndSize(path):
    # Returns (bestPath, bestSize) starting from this path, which could
    # be to either a folder or a file
    if os.path.isdir(path) == False:
        fileSize = os.path.getsize(path)
        return (path, fileSize)
    else:
        bestFile = ""
        bestSize = 0
        for file in os.listdir(path):
            currFile, currSize = findLargestFileAndSize(path + "/" + file)
            if currSize > bestSize:
                bestSize = currSize
                bestFile = currFile
        return bestFile, bestSize

def knightsTour(rows, cols):
    board = [[0]*cols for i in range(rows)]
    currRow = 0
    currCol = 0
    currStep = 1
    board[currRow][currCol] = currStep
    return helpKnight(rows,cols, board, currRow, currCol, currStep)


def helpKnight(rows,cols, board, currRow, currCol, currStep):
    possibleMoves =[(2,1),(2,-1),(-2,1),(-2,-1), (1,2),(
        1,-2), (-1,2), (-1,-2)]
    if currStep == (rows*cols):
        return board
    else:
        for move in possibleMoves:
            drow = move[0]
            dcol = move[1]
            if isLegal(currRow+drow, currCol+dcol, board,rows, cols):
                currRow += drow
                currCol += dcol
                currStep +=1
                board[currRow][currCol] = currStep
                result = helpKnight(rows,cols, board, currRow, 
                    currCol, currStep)
                if result != None:
                    return result
                else: #undo move
                    board[currRow][currCol] = 0
                    currRow -= drow
                    currCol -= dcol
                    currStep -=1
        return None


def isLegal(currRow, currCol, board, rows, cols):

    if currRow >= rows or currRow<0:
        return False
    elif currCol >= cols or currCol<0:
        return False
    elif board[currRow][currCol] != 0:
        return False
    return True
            
            
#################################################
# Test Functions
#################################################

def testFindLargestFile():
    print('Testing findLargestFile()...', end='')
    assert(findLargestFile('sampleFiles/folderA') ==
                           'sampleFiles/folderA/folderC/giftwrap.txt')
    assert(findLargestFile('sampleFiles/folderB') ==
                           'sampleFiles/folderB/folderH/driving.txt')
    assert(findLargestFile('sampleFiles/folderB/folderF') == '')
    print('Passed!')

def testKnightsTour():
    print('Testing knightsTour()....', end='')
    def checkDims(rows, cols, ok=True):
        T = knightsTour(rows, cols)
        s = f'knightsTour({rows},{cols})'
        if (not ok):
            if (T is not None):
                raise Exception(f'{s} should return None')
            return True
        if (T is None):
            raise Exception(f'{s} must return a {rows}x{cols}' +
                             ' 2d list (not None)')
        if ((rows != len(T)) or (cols != (len(T[0])))):
            raise Exception(f'{s} must return a {rows}x{cols} 2d list')
        d = dict()
        for r in range(rows):
            for c in range(cols):
                d[ T[r][c] ] = (r,c)
        if (sorted(d.keys()) != list(range(1, rows*cols+1))):
            raise Exception(f'{s} should contain numbers' +
                             ' from 1 to {rows*cols}')
        prevRow, prevCol = d[1]
        for step in range(2, rows*cols+1):
            row,col = d[step]
            distance = abs(prevRow - row) + abs(prevCol - col)
            if (distance != 3):
                raise Exception(f'{s}: from {step-1} to {step}' +
                                 ' is not a legal move')
            prevRow, prevCol = row,col
        return True
    assert(checkDims(4, 3))
    assert(checkDims(4, 4, ok=False))
    assert(checkDims(4, 5))
    assert(checkDims(3, 4))
    assert(checkDims(3, 6, ok=False))
    assert(checkDims(3, 7))
    assert(checkDims(5, 5))
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testFindLargestFile()
    testKnightsTour()

def main():
    cs112_s22_week10_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()