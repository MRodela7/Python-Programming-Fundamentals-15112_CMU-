#################################################
# hw4.py
# name:Mahtabin Rodela Rozbu
# andrew id: mrozbu
#################################################

import cs112_s22_week4_linter
import math, copy
import string
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

def alternatingSum(L):

    if L == [] or L == None:
            return 0
    elif len(L) == 1:
        return L[0]
        
    elif len(L) ==2:
        return L[0]-L[1]
    
    result = L[0]-L[1]
    print ("Result of first two elements:", result)
    NewList = [result] + L[2:]
    print ("NewList:", NewList)
    
    i =1
    summation = NewList[0]
    while i < len(NewList):
        if i%2 == 0:
            print ("Current index in list is", i, "so subtract", NewList[i])
            summation -= NewList[i]
            print ("Sum:", summation)
        
        else:
            
            print ("Current index in list is", i, "so add", NewList[i])
            summation += NewList[i]
            print ("Sum:", summation)
        i+=1
    print ("ALternating:", summation)
    return summation

def median(L):
    length = len(L)

    if length == 0:
        return None
    elif length ==1:
        return L[0]
        
    newList = sorted(L)
    print ("NewList:", newList)
    mid = (length//2)
    print ("Mid:", newList[mid])
    
    
    
    if length%2 == 0:
        othermid = mid-1
        print ("Other:", newList[othermid])
        medianoftwo = (((newList[mid])+(newList[othermid]))/2)
        print ("Medianoftwo:", medianoftwo)
        return medianoftwo
        
    elif length %2 != 0:
        
        return newList[mid]

def smallestDifference(L):
    
    minList = []
    if len(L) <2:
        return -1
    for index in range((len(L))):
        for j in range(1, (len(L))):
            if j != index:
                diff = abs((L[index])-(L[j]))
        
                minList.append(diff)
            else:
                continue
    
    return min(minList)

def nondestructiveRemoveRepeats(L):
    
    newList = [L[0]]
    for i in range(len(L)):
    
        if L[i] not in newList:
            print (L[i])
            newList += [L[i]]
            print (newList)
                
        continue
        
    return newList

def destructiveRemoveRepeats(L):
    i = 1
    while i <= (len(L)-1):
        if L[i] not in L[:i]:
            i+=1
        else:
            print(L[i])
            print(L[:i])
            L.pop(i)

#################################################
# Part B
#################################################

def Descend(L):
    descend= 0
    for i in range(len(L)-1):
        if (L[i] >= L[i+1]):
            print ("Desc...Current:", L[i], "Next:", L[i+1])
            descend +=1
            continue
    if descend == len(L)-1:
        return True
        
def Ascend(L):
    ascend = 0
    for i in range(len(L)-1):
        if (L[i] <= L[i+1]):
            print ("Desc...Current:", L[i], "Next:", L[i+1])
            ascend +=1
            continue
    if ascend == len(L)-1:
        return True

def isSorted(L):
    
    if len(L) == 0 or len(L)== 1:
        return True
    else:
        if Ascend(L) or Descend(L):
            return True
        return False
    


def countConsecutiveDigits(L, a):

    count =1
    for index in range(a, len(L)-1):
        
        if L[index] == L[index+1]:
            count +=1
            continue
            print (count)
              
        break
        
    return count
            
            
        
    print ("occur:", occur)
    return occur
         
def lookAndSay(L):
    final =[]
    value = 0
    index =0
    while index <= (len(L)-1):
    
        
        print ("current num:", L[index])
        count = countConsecutiveDigits(L, index)
        
        print ("COunt:", count)
        value = L[index]
        print ("Value", value)
        final +=[(count, value)]
        print (final)
        if count>1:
            index += count-1
        index+=1
        print ("Index", index)
    return final



def inverseLookAndSay(L):
    
    newList = []
    print (L)
    for tuple in L[::]:
        print ("Tuple:", tuple)
        newList += [(tuple[1])]*tuple[0]
    return newList

def returnLists(List):
    length = len(List)
    x = (length)-1
    newList = []
    ## putting x as form of tuple
    for coeff in range(0, length):
        newList.append([(List[coeff]),x])
        
        x -=1
    return newList

def multiply(p1, p2):
    p1_list = returnLists(p1)
    # print ("P1_tuple_list",p1_tuple_list)
    p2_list = returnLists(p2)
    # print ("P2_tuple_list",p2_tuple_list)
    
    length_p1 = len(p1_list)
    length_p2 = len(p2_list)
    new_list = []
    for list_p1 in p1_list[::]:
       
        for list_p2 in p2_list[::]:
            
            
            index_0_coeff = (list_p1[0])*(list_p2[0])
            # print ("Index_coeff:",index_0_coeff )
            
            index_1_x = (list_p1[1])+(list_p2[1])
            # print ("X coeef:", index_1_x)
            
            new_list += [[index_0_coeff,index_1_x]]
           
    return new_list
            
def removeZerocoeff(p1, p2):
    List =  multiply(p1,p2)
    for pair in List[::]:
        # print ("Tuple is searching for zero-coeff:", tuple)
        if pair[0] ==0:
            List.remove(pair)
    return List
    
def multiplyPolynomials(p1, p2):
    added_pair = []

    L = removeZerocoeff(p1, p2)
    print (L)
    
    lengthFinal = len(p1)+len(p2)-1
    result = [0]*lengthFinal
    
    for i in range(len(L)):
        coef = L[i][0]
        power = L[i][1]
        result[power] += coef
    
    result.reverse()
    
    return result
        

def wordCanbeFormed(dictionary, hand):
    
    wordFormable =[]
    
    
    for word in dictionary:
        count = 0
        hand1 = copy.copy(hand)
        print ("Word in dic:", word)
        
        for letter in word:
            print ("Single Letter in word:", letter)
            if letter in hand1:
                count +=1
                hand1.remove(letter)
        if count == len(word):
            wordFormable.append(word)
            
    if len(wordFormable) !=0:
        print("Word can be formed by hand")
        return True, wordFormable
    else:
        print ("Word cannot be formed by hand")
        return False, []


def calscore(word, letterScores):
    
    result = 0
    for letter in word.lower():
        print ("Letter in word:", letter)
        findindex = string.ascii_lowercase.find(letter)
        print ("The index of the letter in alphabet:", findindex)
        value = int(letterScores[findindex])
        print("The value of the letter in letterscore:", value)
        result += value
    print ("Result:", result)
    return result
        
def bestScrabbleScore(dictionary, letterScores, hand):
    
    if len(dictionary) ==0 or len(hand) ==0:
        print("entered")
        return None
    
    print ("InitialDic:", dictionary)
    print("Letterscore:", letterScores)
    print("CurrentHand:", hand)
    score = 0
    bestscore = -1
    bestword =''
    lstForbestWord = []
  
    finalList = []
  

    
    scrabblePossible, withWords = wordCanbeFormed(dictionary, hand)
    print(scrabblePossible, withWords)
        
    if scrabblePossible == False or len(withWords) ==0:
        return None
    for word in withWords:

        print ("Word:", word)
            
        score = calscore(word, letterScores)
        
        if score == bestscore:
            lstForbestWord.append(word)
            print ("List for the best word", lstForbestWord)
        
        if score > bestscore:
            bestscore = score
            lstForbestWord.append(word)
            print ("List of Best Word", lstForbestWord)
    
    if len(lstForbestWord) >1:
        result = (lstForbestWord, bestscore)
        return result
    else:
        result = (lstForbestWord[0], bestscore)
        return result
    
#################################################
# Bonus/Optional
#################################################

def linearRegression(pointsList):
    return 42

def runSimpleProgram(program, args):
    return 42

#################################################
# Test Functions
#################################################

def _verifyAlternatingSumIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    alternatingSum(a)
    return (a == b)

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(_verifyAlternatingSumIsNondestructive())
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    assert(alternatingSum([-42, 42]) == -42-42)
    
    print('Passed!')

def _verifyMedianIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    median(a)
    return (a == b)

def testMedian():
    print('Testing median()...', end='')
    assert(_verifyMedianIsNondestructive())
    assert(median([ ]) == None)
    assert(median([ 42 ]) == 42)
    assert(almostEqual(median([ 1 ]), 1))
    assert(almostEqual(median([ 1, 2]), 1.5))
    assert(almostEqual(median([ 2, 3, 2, 4, 2]), 2))
    assert(almostEqual(median([ 2, 3, 2, 4, 2, 3]), 2.5))
    # now make sure this is non-destructive
    a = [ 2, 3, 2, 4, 2, 3]
    b = a + [ ]
    assert(almostEqual(median(b), 2.5))
    if (a != b):
        raise Exception('Your median() function should be non-destructive!')
    print('Passed!')

def testSmallestDifference():
    print('Testing smallestDifference()...', end='')
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference([19,2,83,6,27]) == 4)
    assert(smallestDifference(list(range(0, 10**3, 5)) + [42]) == 2)
    print('Passed!')

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = a + [ ] # copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed!")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed!")

def testIsSorted():
    print('Testing isSorted()...', end='')
    assert(isSorted([]) == True)
    assert(isSorted([1]) == True)
    assert(isSorted([1,1]) == True)
    assert(isSorted([1,2]) == True)
    assert(isSorted([2,1]) == True)
    assert(isSorted([2,2,2,2,2,1,1,1,1,0]) == True)
    assert(isSorted([1,1,1,1,2,2,2,2,3,3]) == True)
    assert(isSorted([1,2,1]) == False)
    assert(isSorted([1,1,2,1]) == False)
    assert(isSorted(range(10,30,3)) == True)
    assert(isSorted(range(30,10,-3)) == True)
    print('Passed!')

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = a + [ ] # copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = a + [ ] # copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print("Passed!")

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed Scrabble!")

def relaxedAlmostEqual(d1, d2):
    epsilon = 10**-3 # really loose here
    return abs(d1 - d2) < epsilon

def tuplesAlmostEqual(t1, t2):
    if (len(t1) != len(t2)): return False
    for i in range(len(t1)):
        if (not relaxedAlmostEqual(t1[i], t2[i])):
            return False
    return True

def testLinearRegression():
    print("Testing bonus problem linearRegression()...", end="")

    ans = linearRegression([(1,3), (2,5), (4,8)])
    target = (1.6429, 1.5, .9972)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,0), (1,2), (3,4)])
    target = ((9.0/7), (2.0/7), .9819805061)
    assert(tuplesAlmostEqual(ans, target))

    #perfect lines
    ans = linearRegression([(1,1), (2,2), (3,3)])
    target = (1.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,1), (-1, -1)])
    target = (2.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    #horizontal lines
    ans = linearRegression([(1,0), (2,0), (3,0)])
    target = (0.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    ans = linearRegression([(1,1), (2,1), (-1,1)])
    target = (0.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    print("Passed!")

def testRunSimpleProgram():
    print("Testing bonus problem runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testAlternatingSum()
    testMedian()
    testSmallestDifference()
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()

    # Part B:
    testIsSorted()
    testLookAndSay()
    testInverseLookAndSay()
    testMultiplyPolynomials()
    testBestScrabbleScore()

    # Bonus:
    #testLinearRegression()
    #testRunSimpleProgram() 

def main():
    cs112_s22_week4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
