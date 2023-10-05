#################################################
# hw9.py
#
# Your name: Mahtabin Rodela
# Your andrew id: mrozbu
#################################################

# import cs112_s22_week9_linter
import math, copy, os

#################################################
# Helper functions
#################################################

# def almostEqual(d1, d2, epsilon=10**-7):
#     # note: use math.isclose() outside 15-112 with Python version 3.5 or later
#     return (abs(d2 - d1) < epsilon)

# import decimal
# def roundHalfUp(d):
#     # Round to nearest with ties going away from zero.
#     rounding = decimal.ROUND_HALF_UP
#     # See other rounding options here:
#     # https://docs.python.org/3/library/decimal.html#rounding-modes
#     return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

# def oddCount(L):

#     if len(L)==0:
#         return 0
#     else:
#         if L[0] % 2 != 0:
#             return 1 + oddCount(L[1:])
#         else:
#             return oddCount(L[1:])

# def oddSum(L):
#     if len(L)==0:
#         return 0
#     else:
#         if L[0] % 2 !=0:

#             return L[0] + oddSum(L[1:])
#         else:
#             return oddSum(L[1:])

# def oddsOnly(L):
#     result = []

#     if len(L)==0:
#         return result
#     else:
    
#         if L[0] % 2 != 0:
#             newList = []
#             newList.append(L[0])
#             result+=newList
#             return result + oddsOnly(L[1:])
#         return oddsOnly(L[1:])
        
        
# def maxOdd(L):
#     if len(L)==0:
#         return None
#     largeOdd = maxOdd(L[1:])
#     if L[0]%2 !=0 and largeOdd == None:
#         return L[0]
#     elif L[0]%2 !=0 and largeOdd != None:
#         if L[0]> largeOdd:
#             return L[0]
#         return largeOdd
#     else:
#         return largeOdd
    
        
# def hasConsecutiveDigits(n):

#     if n==0:
#         return False
#     n = abs(n)
#     a = n%10
#     n //=10
#     b = n%10
#     if a != b:
#         return hasConsecutiveDigits(n)
#     return True
        


# def alternatingSum(L):

#     result =0
#     if L==[]:
#         return 0
#     elif len(L) == 1:
#         return L[0]
#     else:
#         a = L[0]
#         b = -(L[1])
#         c = alternatingSum(L[2:])
#         result += a +b + c
#     return result
        
#################################################
# Freddy Fractal Viewer
#################################################
import math
from cmu_112_graphics import *

def appStarted(app):
    app.level = 1

def keyPressed(app, event):
    if event.key in ['Up', 'Right']:
        app.level += 1
    elif (event.key in ['Down', 'Left']) and (app.level > 0):
        app.level -= 1

def drawFractal(app, canvas, level, cx, cy, r, width):

    theta = math.radians(45)
    x = (3/2)*r*(math.sin(theta))
    y = (3/2)*r*(math.cos(theta))

    #min(app.width, app.height)/3)
    if level == 0:
        Freddy(app, canvas, cx, cy, r, width)
    else:
        # call drawfractal twice here, freddy once
        width = width/1.5
        Freddy(app, canvas, cx, cy, r, width) 
        drawFractal(app, canvas, level-1, cx-x, cy-y, r/2, width) #left ear
        drawFractal(app, canvas, level-1, cx+x, cy-y, r/2, width) #right ear
        

def Freddy(app, canvas, cx, cy, r, width):

    
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='brown', outline='black', 
        width= width)

    #position of left eyes:
    (cxLeftEye, cyleftEye, radiusEye) =  cx-r/2, cy-r/2, r/6
    canvas.create_oval(cxLeftEye-radiusEye, cyleftEye-radiusEye,
        cxLeftEye+radiusEye, cyleftEye+radiusEye, fill = "black")

    #position of right eyes:
    (cxRightEye, cyRightEye, radiusEye) =  cx+r/2, cy-r/2, r/6
    canvas.create_oval(cxRightEye-radiusEye, cyRightEye-radiusEye,
        cxRightEye+radiusEye, cyRightEye+radiusEye, fill = "black")
    
    #center position of mouth:
    (cxMouth, cyMouth, radMouth) = cx, cy+(r/4), r/2
    canvas.create_oval(cxMouth-radMouth, cyMouth-radMouth, 
        cxMouth+radMouth, cyMouth+radMouth,fill = "#ffe0b3", 
            outline = "black", width =3)

    #center position of nose:
    (cxN, cyN, radN) = cxMouth, cyMouth-radMouth/2, radiusEye
    canvas.create_oval(cxN-radN, cyN-radN, cxN+radN, 
        cyN+radN,fill = "black", outline = "black")

    #finding shifting radius of x
    theta = math.radians(45)
    x = (3/2)*r*(math.sin(theta))
    y = (3/2)*r*(math.cos(theta))

    #postion of left ear:
    (cxLeftEar, cyLeftEar, radEar) = cx-x, cy-y, r/2
    

    #position of Right Ear
    (cxRightEar, cyRightEar, radEar) = cx+x, cy-y, r/2
    

    #create smile arc:
    (cxArc, cyArc, rad) = cxMouth, cyMouth+2*radMouth/6, radMouth/6
    canvas.create_arc(cxArc-3*rad, cyArc-2*rad, cxArc+rad, cyArc+2*rad, 
        style = "arc", start = -180, extent=180, width =4)
    (cxArc1, cyArc1, rad1) = cxArc+2*rad, cyArc, rad
    canvas.create_arc(cxArc1-rad1, cyArc1-2*rad1, cxArc1+2*rad1, 
        cyArc1+2*rad1,style = "arc", start = -180, extent=180, width = 4)


def redrawAll(app, canvas):
    (cx, cy, r) = (app.width/2, app.height/2, 100)
    width = 10
    drawFractal(app, canvas, app.level, cx, cy, r, width)


def runFreddyFractalViewer():
    print('Running Freddy Fractal Viewer!')
    runApp(width=400, height=400)

#################################################
# Test Functions
#################################################

# def testOddCount():
#     print('Testing oddCount()...', end='')
#     assert(oddCount([ ]) == 0)
#     assert(oddCount([ 2, 4, 6 ]) == 0) 
#     assert(oddCount([ 2, 4, 6, 7 ]) == 1)
#     assert(oddCount([ -1, -2, -3 ]) == 2)
#     assert(oddCount([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 6)
#     print('Passed!')

# def testOddSum():
#     print('Testing oddSum()...', end='')
#     assert(oddSum([ ]) == 0)
#     assert(oddSum([ 2, 4, 6 ]) == 0) 
#     assert(oddSum([ 2, 4, 6, 7 ]) == 7)
#     assert(oddSum([ -1, -2, -3 ]) == -4)
#     assert(oddSum([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 1+3+5+7+9+11)
#     print('Passed!')

# def testOddsOnly():
#     print('Testing oddsOnly()...', end='')
#     assert(oddsOnly([ ]) == [ ])
#     assert(oddsOnly([ 2, 4, 6 ]) == [ ]) 
#     assert(oddsOnly([ 2, 4, 6, 7 ]) == [ 7 ])
#     assert(oddsOnly([ -1, -2, -3 ]) == [-1, -3])
#     assert(oddsOnly([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == [1,3,5,7,9,11])
#     print('Passed!')

# def testMaxOdd():
#     print('Testing maxOdd()...', end='')
#     assert(maxOdd([ ]) == None)
#     assert(maxOdd([ 2, 4, 6 ]) == None) 
#     assert(maxOdd([ 2, 4, 6, 7 ]) == 7)
#     assert(maxOdd([ -1, -2, -3 ]) == -1)
#     assert(maxOdd([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 11)
#     print('Passed!')

# def testHasConsecutiveDigits():
#   print('Testing hasConsecutiveDigits()...', end='')
#   assert(hasConsecutiveDigits(1123) == True)
#   assert(hasConsecutiveDigits(-1123) == True)
#   assert(hasConsecutiveDigits(1234) == False)
#   assert(hasConsecutiveDigits(0) == False)
#   assert(hasConsecutiveDigits(1233) == True)
#   print("Passed!")

# def testAlternatingSum():
#     print('Testing alternatingSum()...', end='')
#     assert(alternatingSum([1,2,3,4,5]) == 1-2+3-4+5)
#     assert(alternatingSum([ ]) == 0)
#     print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # testOddCount()
    # testOddSum()
    # testOddsOnly()
    # testMaxOdd()
    # testHasConsecutiveDigits()
    # testAlternatingSum()
    runFreddyFractalViewer()

def main():
    # cs112_s22_week9_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()


def sameValues(L,M):
    if L == [] or M == []:
        return set()
    else:
        sameValuesOfTheRest = sameValues(L[1:], M[1:])
        if L[0] == M[0]:
            sameValuesOfTheRest.add(L[0])

        return sameValuesOfTheRest

