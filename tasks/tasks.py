import random
import numpy


# Evaluate the quadratic equation for a given a, b, and c
def exercise1():
    print("Enter a:")
    a = int(input())
    print("Enter b:")
    b = int(input())
    print("Enter c:")
    c = int(input())
    print("Delta =", b ** 2 - 4 * a * c)


# Write a Python program that prompts the user for his/her amount of money, then reports how manyIPhoneX ‘s the person
# can afford, and/or how much more money he/she will need to afford one IPhoneX or how many additional units can buy
def exercise2():
    print("How much money do you have?")
    money = float(input())
    iphoneXPrice = 2500
    if money > iphoneXPrice:
        print("You can buy", int(money / iphoneXPrice), "iPhone X's")
    else:
        print("You need", round(iphoneXPrice - money, 2), "zl more money to buy iPhone X")


# How would we print the "99 Bottles of Beer" song?
def exercise3():
    for x in range(99, 0, -1):
        if x == 1:
            print('1 bottle of beer on the wall, 1 bottle of beer!')
            print('So take it down, pass it around, no more bottles of beer on the wall!')
        else:
            print(x, ' bottles of beer on the wall,', x, ' bottles of beer!')
            print('So take it down, pass it around,', x, ' more bottles of beer on the wall!')


# Write a Python program that computes the factorial of an integer
def exercise4():
    print("Enter the number for calculating the factorial")
    number = int(input())
    result = 1
    for i in range(number, 0, -1):
        result *= i  # result = result * i
    print("Factorial of", number, "equals", result)


# Write code to display and count the divisors of number
def exercise5():
    print("Enter the number to show its divisors")
    number = int(input())
    divisors = []
    for i in range(1, number + 1, 1):
        if number % i == 0:
            divisors.append(i)
    print("Given number", number, "has", len(divisors), "divisors:", divisors)


# Write code to display all the prime numbers from the range of 1-100
def exercise6():
    primeNumbers = [2, ]
    for i in range(2, 101, 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
            elif (i - 1) == j:
                primeNumbers.append(i)
    print(primeNumbers)


# Write code to display and count the numbers of the all the even number in the range of 1-200
def exercise7():
    evenNumbers = []
    for i in range(2, 201, 2):
        evenNumbers.append(i)
    print("In range 1 - 200 there are", len(evenNumbers), "even numbers:", evenNumbers)


# Write a program that performs a rotation cypher
def exercise8():
    print("Enter word to code")
    toCode = input()
    coded = ""
    for letter in toCode:
        if letter == 'Z':
            coded += 'A'
        elif letter == 'z':
            coded += 'a'
        else:
            coded += chr(ord(letter) + 1)
    print("Your word coded:", coded)


# Write a program that reverse given text
def exercise9():
    print("Enter text to reverse")
    toReverse = input()
    reversed = ""
    chars = []
    for c in toReverse:
        chars.append(c)
    for i in range(len(toReverse) - 1, -1, -1):
        reversed += chars[i]
    print("Your text reversed:", reversed)


# Write a program that removes duplicates from the given list [1, 3, 5, 6, 3, 5, 6, 1, 3, 8, 9, 1, 5]
def exercise10():
    list = [1, 3, 5, 6, 3, 5, 6, 1, 3, 8, 9, 1, 5]
    newList = []
    while len(list) > 0:
        number = list[0]
        numberOfOccurencies = list.count(number)
        for i in range(numberOfOccurencies):
            list.remove(number)
        newList.append(number)
    print(newList)


# Write a program that calculates how many numbers in the randomly generated list of 100 elements are smaller than 23
def exercise11():
    randomList = []
    smallerThan23 = []
    for i in range(100):
        randomList.append(random.randint(1, 100))
    for number in randomList:
        if number < 23:
            smallerThan23.append(number)
    print("In list:", randomList, "\nthere are", len(smallerThan23), "numbers smaller than 23:", smallerThan23)


# Write a python program to calculate the sum of all numbers raised to the square in the tuple
# (1, 3, 5, 6, 3, 5, 6, 1, 3, 85, 96, 1, 5, 123, 456, 8674)
def exercise12():
    myTuple = (1, 3, 5, 6, 3, 5, 6, 1, 3, 85, 96, 1, 5, 123, 456, 8674)
    mySum = 0
    for number in myTuple:
        mySum += number ** 2
    print("Sum of squares of numbers in given tuple equals", mySum)


# Write a python program to find the minimal number in a tuple (31, 16, 32, 56789, 688, 85, 96, 5, 123, 456, 8674)
# not using min(tuple) function
def exercise13():
    myTuple = (31, 16, 32, 56789, 688, 85, 96, 5, 123, 456, 8674)
    minInTuple = myTuple[0]
    for number in myTuple:
        if number < minInTuple:
            minInTuple = number
    print("Minimum number in tuple:", myTuple, "is", minInTuple)


# Write a Python program to get the top three items in a shop
def exercise14():
    items = {"item 1": 45.50, "item 2": 35, "item 3": 41.30, "item 4": 55, "item 5 ": 24}
    sortedItems = sorted(items, key=items.get, reverse=True)
    print("Top 3 items:")
    for i in range(0, 3, 1):
        print(sortedItems[i], items[sortedItems[i]])


# Write a program to process a file of DNA text, such as: ATGCAATTGCTCGATTAGCG Count the percent of C+G present in the DNA.
def exercise15():
    file = open("DNA.txt", "r")
    numberOfLetters = 0.0
    numberOfC = 0.0
    numberOfG = 0.0
    for letter in file.read():
        numberOfLetters += 1
        if letter == "C":
            numberOfC += 1
        if letter == "G":
            numberOfG += 1
    percentOfCAndG = int(round((numberOfC + numberOfG) / numberOfLetters * 100, 0))
    print("Percent of C and G equals ", percentOfCAndG, "%", sep="")


# Write a Python function that checks whether a passed string is palindrome or not
def exercise16():
    def palindromeCheck():
        print("Enter text to check if it's palindrome:")
        stringToCheck = input()
        isPalindrome = True
        lower = stringToCheck.lower()
        j = len(stringToCheck)
        for i in range(int(len(lower) / 2)):
            j -= 1
            if lower[i] != lower[j]:
                isPalindrome = False
                break
        if isPalindrome:
            print("Text:", stringToCheck, "is palindrome")
        else:
            print("Text:", stringToCheck, "is not palindrome")

    palindromeCheck()


# Write a Python program using Python function that print the triangle numbers from
# randomly generated list of 50 elements in the range of 1-1000
def exercise17():
    def generateTriangleNumbersTo1000():
        triangleNumbers = []
        i = 0
        actualNumber = 0
        while actualNumber <= 1000:
            triangleNumbers.append(actualNumber)
            i += 1
            actualNumber += i
        return triangleNumbers

    def generateRandomNumbersList():
        randomNumbers = []
        for i in range(50):
            randomNumbers.append(random.randint(1, 1000))
        return randomNumbers

    triangleNumbers = generateTriangleNumbersTo1000()
    randomNumbers = generateRandomNumbersList()
    resultList = []
    for number in randomNumbers:
        if number in triangleNumbers:
            resultList.append(number)
    print("In list:", randomNumbers, "\nfollowing numbers are triangle numbers:", resultList)


# Write a Python program using Python function that converts in given text symbols of emojis :) to 😃 and :( to 😞. Please
# try to utilize the data structure such as the dictionary
def exercise18():
    emojis = {":D": "\U0001F603", ">.<": "\U0001F606", ":)": "\U0001F642", "(:": "\U0001F643", ";)": "\U0001F609",
              "^_^": "\U0001F60A",
              ":*": "\U0001F618", ":|": "\U0001F610", ":(": "\U0001F641", "8-)": "\U0001F60E"}
    print("Enter your emoji")
    emoji = input()
    print("Your emoji converted:", emojis[emoji])


# Write a Python program using Python functions that generates 300 randomly generated strings,
# utilizing capitals characters only, each of the string has to have 50 characters, save them to the file mutant.txt then
# read them from the file and calculate the sum of all the ASCI codes which are contained in each string
def exerciseMUTANT():
    def generateRandomStrings():
        randomStrings = []
        for i in range(300):
            randomString = ""
            for i in range(50):
                randomString += chr(random.randint(65, 90))
            randomStrings.append(randomString)
        file = open("mutant.txt", "w")
        for string in randomStrings:
            file.writelines(string + "\n")

    def calculateSumOfASCICodes():
        file = open("mutant.txt", "r")
        sumOfASCICodes = []
        for i in range(300):
            string = file.readline()
            sumOfASCICode = 0
            for j in range(50):
                sumOfASCICode += ord(string[j])
            sumOfASCICodes.append(sumOfASCICode)
        return sumOfASCICodes

    generateRandomStrings()
    print("Sums of ASCI codes of random generated strings:", calculateSumOfASCICodes())


# Write a Python program adding two matrixes MxN . You specify the size of matrixes by giving
# the size of M and N. All the elements in the matrix must be randomly generated from the range (1,14). Calculate the
# time of execution your code using module time
def exercise19Basic():
    print("Specify sizes of matrixes you want to add")
    print("Enter M:")
    m = int(input())
    print("Enter N:")
    n = int(input())
    matrixes = []
    for i in range(2):
        matrix = []
        for j in range(m):
            row = []
            for k in range(n):
                row.append(random.randint(1, 4))
            matrix.append(row)
        matrixes.append(matrix)
    matrix = []
    for i in range(len(matrixes[0])):
        row = []
        for j in range(len(matrixes[0][0])):
            row.append(matrixes[0][i][j] + matrixes[1][i][j])
        matrix.append(row)
    matrixes.append(matrix)
    print(matrixes[0], "+", matrixes[1], "=", matrixes[2])


# Write the same program as Exercise 19 basic but utilizing python module numpy
def exercise19():
    print("Specify sizes of matrixes you want to add")
    print("Enter M:")
    m = int(input())
    print("Enter N:")
    n = int(input())
    matrix1 = numpy.random.randint(14, size=(m, n))
    matrix2 = numpy.random.randint(14, size=(m, n))
    resultMatrix = numpy.add(matrix1, matrix2)
    print(matrix1, "+", matrix2, "=", resultMatrix, sep="\n")


# Napisz program NumPy#1, aby obliczyć mnożenie dwóch podanych macierzy
def numPy1():
    m = 5
    n = 5
    matrix1 = numpy.random.randint(14, size=(m, n))
    matrix2 = numpy.random.randint(14, size=(m, n))
    resultMatrix = numpy.matmul(matrix1, matrix2)
    print(matrix1, "x", matrix2, "=", resultMatrix, sep="\n")


# Napisz program NumPy#2, aby obliczyć iloczyn zewnętrzny dwóch podanych wektorów
def numPy2():
    m = 5
    vector1 = numpy.random.randint(14, size=(m))
    vector2 = numpy.random.randint(14, size=(m))
    resultVector = numpy.outer(vector1, vector2)
    print(vector1, "*", vector2, "=\n", resultVector)


# Napisz program NumPy#3, aby obliczyć iloczyn krzyżowy dwóch podanych wektorów.
def numPy3():
    m = 3
    vector1 = numpy.random.randint(14, size=(m))
    vector2 = numpy.random.randint(14, size=(m))
    resultVector = numpy.cross(vector1, vector2)
    print(vector1, "x", vector2, "=", resultVector)


# Napisz program NumPy#4, aby obliczyć wyznacznik danej macierzy kwadratowej.
def numPy4():
    m = 2
    n = 2
    matrix = numpy.random.randint(14, size=(m, n))
    det = round(numpy.linalg.det(matrix), 2)
    print("det\n", matrix, "\n=", det)


# Napisz program NumPy#5, aby obliczyć iloczyn Kroneckera dwóch podanych macierzy wielowymiarowych
def numPy5():
    m = 2
    n = 2
    matrix1 = numpy.random.randint(14, size=(m, n))
    matrix2 = numpy.random.randint(14, size=(m, n))
    resultMatrix = numpy.kron(matrix1, matrix2)
    print(matrix1, "⊗", matrix2, "=", resultMatrix, sep="\n")


# Napisz program NumPy#6, aby obliczyć odwrotność danej macierzy
def numPy6():
    m = 2
    n = 2
    matrix = numpy.random.randint(14, size=(m, n))
    inversedMatrix = numpy.linalg.inv(matrix)
    print(matrix, "^-1\n=", inversedMatrix)


# Napisz program NumPy#7, aby obliczyć sumę elementu ukośnego danej macierzy
def numPy7():
    m = 2
    n = 2
    matrix = numpy.random.randint(14, size=(m, n))
    sumOfDiagonalElement = numpy.trace(matrix)
    print(matrix, "\nsum of the diagonal element =", sumOfDiagonalElement)
