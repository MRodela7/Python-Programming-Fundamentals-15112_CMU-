#################################################
# hw6.py
#
# Your name: Mahtabin Rodela
# Your andrew id:mrozbu
#
# Your partner's name:David Kim
# Your partner's andrew id: sukwonk
#################################################

# import cs112_s22_week6_linter
import math, copy, random

from cmu_112_graphics import *

#################################################
Helper functions
################################################

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

def isPerfectSquare(n):
    n = abs(n)
    if ((int(math.sqrt(n)))**2) == n:
        return True
    return False

def sortN(n):
    i =0
    digitList = []
    while n>0:
        digitList.append(n%10)
        n//=10
    # print (digitList)
    sorted_n_list= sorted(digitList)
    
    for element in range(len(sorted_n_list)):
        
        i *= 10
        i +=sorted_n_list[element]
    # print ("i:", i)
    return i

def isSortOfSquarish(n):
    if isPerfectSquare(n) or zeroDetected(n) or n<0:
        return False
    sorted_n = sortN(n)
    # print("Sorted_n:", sorted_n)
    if isPerfectSquare(sorted_n):
        return True
    return False

def nthSortOfSquarish(n):
    guess = 0
    found = 0
    while found <=n:
        guess +=1
        if isSortOfSquarish(guess) == True:
            found +=1
    return guess

def zeroDetected(n):
    if n == 0:
        return True
    while n > 0: 
        if n%10 == 0:
            return True
        n //=10
    return False

#################################################
# s21-midterm1-animation
#################################################
def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 +(y2-y1)**2)


def s21MidtermAnimation_appStarted(app):
    
    app.radius = 20
    app.color = 'green'
    app.timerDelay = 50
    app.dots = []
    app.lines = []
    app.count = 0
def s21MidtermAnimation_keyPressed(app, event):
    
    if event.key =="r":
        app.dots = []
        app.lines =[]
        app.count = 0
        
def s21MidtermAnimation_mousedPressed(app, event):
        
def s21MidtermAnimation_timerFired(app):
    app.count += timeDelay
        if app.count >= 5000:
            app.dots = []
            app.lines =[]

def s21MidtermAnimation_redrawAll(app, canvas):
    for j in range(app.i+1):
        x = app.width/len(app.label) * (j + 0.5)
        y = app.height/2 if (j < app.i) else app.y
        canvas.create_text(x, y, fill=app.color,
                           text=app.label[j], font=f'Arial 30 bold')

def s21Midterm1Animation():
    runApp(width=400, height=400, fnPrefix='s21MidtermAnimation_')

#################################################
# Tetris
#################################################

def appStarted(app):
    app.label = 'Tetris!'
    app.color = 'orange'
    app.size = 0

def keyPressed(app, event):
    app.color = random.choice(['red', 'orange', 'yellow', 'green', 'blue'])

def timerFired(app):
    app.size += 10  

def redrawAll(app, canvas):
    for s in ((app.size % 300), ((app.size + 150) % 300)):
        canvas.create_text(app.width/2, app.height/2, fill=app.color,
                           text=app.label, font=f'Arial {s} bold')

def playTetris():
    runApp(width=400, height=400)

#################################################
# Test Functions
#################################################

def testIsPerfectSquare():
    print('Testing isPerfectSquare(n))...', end='')
    assert(isPerfectSquare(4) == True)
    assert(isPerfectSquare(9) == True)
    assert(isPerfectSquare(10) == False)
    assert(isPerfectSquare(225) == True)
    assert(isPerfectSquare(1225) == True)
    assert(isPerfectSquare(1226) == False)
    print('Passed')


def testIsSortOfSquarish():
    print('Testing isSortOfSquarish(n))...', end='')
    assert(isSortOfSquarish(52) == True)
    assert(isSortOfSquarish(16) == False)
    assert(isSortOfSquarish(502) == False)
    assert(isSortOfSquarish(414) == True)
    assert(isSortOfSquarish(5221) == True)
    assert(isSortOfSquarish(6221) == False)
    assert(isSortOfSquarish(-52) == False)
    print('Passed')


def testNthSortOfSquarish():
    print('Testing nthSortOfSquarish()...', end='')
    assert(nthSortOfSquarish(0) == 52)
    assert(nthSortOfSquarish(1) == 61)
    assert(nthSortOfSquarish(2) == 63)
    assert(nthSortOfSquarish(3) == 94)
    assert(nthSortOfSquarish(4) == 252)
    assert(nthSortOfSquarish(8) == 522)
    print('Passed')

def testAll():
    testIsPerfectSquare()
    testIsSortOfSquarish()
    testNthSortOfSquarish()

################################################
main
################################################

def main():
    cs112_s22_week6_linter.lint()
    testAll()
    s21Midterm1Animation()
    playTetris()

if __name__ == '__main__':
    main()



