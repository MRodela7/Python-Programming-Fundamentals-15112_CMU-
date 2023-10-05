#################################################
# hw12.py
#
# Your name: Mahtabin Rodela Rozbu
# Your andrew id: mrozbu
#################################################

import cs112_n22_hw12_linter
import math, copy

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
    return int(decimal.Decimal(d).to_integral_numue(rounding=rounding))

#################################################
# Functions for you to write
#################################################
def evalPrefixNotation(L):
    if len(L) == 1: return L[0]
    else:
        val = L[0]
        L.pop(0)
        #get num
        if isinstance(val, int):return val
        # call function twice to get the numbers
        if val in ["+", "-", "*"]:
            num1 = evalPrefixNotation(L)
            num2 = evalPrefixNotation(L)
            #operate
            return cal(num1, num2, val)
        else:
            rasiedAnError = True
            print(raisedAnError)
            
def cal(num1, num2, val):
    if val == '+':return num1 +num2
    if val == '-':return num1 -num2
    if val == '*':return num1 *num2


def knightsTour(rows, cols):
    #initialize board
    board = [[0*col for col in range(cols)] for row in range(rows)]
    board[0][0] =1
    return helper(board, rows, cols, count=1, currRow=0, currCol=0)
    
def helper(board, rows, cols, count, currRow, currCol):
    directions = ([(1,2), (2,1), (-1, -2), (-2, -1), (-1,2), 
        (-2, 1), (2,-1), (1,-2)])
    if count == rows*cols: return board
    else:
        #traverse
        for direc in directions:
            newRow = currRow + direc[0]
            newCol = currCol + direc[1]
            #check for valid move
            if isLegal(newRow, newCol, board, rows, cols):
                count +=1
                currRow = newRow
                currCol = newCol
                board[currRow][currCol] = count
                sol = helper(board, rows, cols, count, currRow, currCol)
                if sol !=None:return sol
                #backtrack
                else:
                    count-=1
                    board[currRow][currCol]=0
                    currRow-=direc[0]
                    currCol -=direc[1]
        return None

def isLegal(newRow, newCol, board, rows, cols):
    if (newRow<0 or newRow>=rows) or (newCol<0 or 
        newCol>=cols) or (board[newRow][newCol] !=0):return False
    else:return True


#################################################
# Test Functions
#################################################

def testEvalPrefixNotation():
    print('Testing evalPrefixNotation()...', end='')
    assert(evalPrefixNotation([42]) == 42)          # (42)
    assert(evalPrefixNotation(['+', 3, 4]) == 7)    # (3 + 4)
    assert(evalPrefixNotation(['-', 3, 4]) == -1)   # (3 - 4)
    assert(evalPrefixNotation(['-', 4, 3]) == 1)    # (4 - 3)
    assert(evalPrefixNotation(['+', 3, '*', 4, 5]) == 23)   # (3 + (4 * 5))

    # ((2 * 3) + (4 * 5))
    assert(evalPrefixNotation(['+', '*', 2, 3, '*', 4, 5]) == 26)
    # ((2 + 3) * (4 + 5))
    assert(evalPrefixNotation(['*', '+', 2, 3, '+', 4, 5]) == 45)
    # ((2 + (3 * (8 - 7))) * ((2 * 2) + 5))
    assert(evalPrefixNotation(['*', '+', 2, '*', 3, '-', 8, 7,
                               '+', '*', 2, 2, 5]) == 45)
    
    #Make sure to raise an error for operators that are not +, -, or *
    raisedAnError = False
    try:
        evalPrefixNotation(['^', 2, 3])
    except:
        raisedAnError = True
    assert(raisedAnError == True)
    print('Passed.')


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
    testEvalPrefixNotation()
    testKnightsTour()
def main():
    cs112_n22_hw12_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()
