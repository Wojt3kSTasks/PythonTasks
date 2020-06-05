import math

# Evaluate the quadratic equation for a given a, b, and c
import random


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
    for i in range(number, 1, -1):
        result *= i
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
    primeNumbers = []
    for i in range(2, 101, 1):
        for j in range(2, int(math.sqrt(i)) + 2):
            if (i % j) == 0:
                break
            elif (int(math.sqrt(i)) + 1) == j:
                primeNumbers.append(i)
    print(primeNumbers)


# Write code to display and count the numbers of the all the even number in the range of 1-200
def exercise7():
    evenNumbers = []
    numberOfEvenNumbers = 0
    for i in range(2, 201, 2):
        evenNumbers.append(i)
        numberOfEvenNumbers += 1
    print("In range 1 - 200 there are", numberOfEvenNumbers, "even numbers:", evenNumbers)


# Write a program that performs a rotation cypher
def exercise8():
    print("Enter word to code")
    toCode = input()
    coded = ""
    for c in toCode:
        coded += chr(ord(c) + 1)
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
    howManySmallerThan23 = 0
    smallerThan23 = []
    for i in range(100):
        randomList.append(random.randint(1, 100))
    for number in randomList:
        if number < 23:
            howManySmallerThan23 += 1
            smallerThan23.append(number)
    print("In list:", randomList, "\nthere are", howManySmallerThan23, "numbers smaller than 23:", smallerThan23)


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
    for i in range(3):
        print(sortedItems[i], items[sortedItems[i]])


# Write a program to process a file of DNA text, such as: ATGCAATTGCTCGATTAGCG Count the percent of C+G present in the DNA.
def exercise15():
    file = open("DNA.txt", "r")
    numberOfLetters = 0.0
    numberOfC = 0.0
    numberOfG = 0.0
    for c in file.read():
        numberOfLetters += 1
        if c == "C":
            numberOfC += 1
        if c == "G":
            numberOfG += 1
    pecentOfCAndG = int(round((numberOfC + numberOfG) / numberOfLetters * 100, 0))
    print("Percent of C and G equals ", pecentOfCAndG, "%", sep="")


# def exercise16():
# def exercise17():
# def exercise18():
# def exercise19():
# def exercise20():
# def exercise21():
# def exercise22():
