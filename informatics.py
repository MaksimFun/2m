from random import randint
from math import sqrt

def gcd(a, b):
    a, b = max(a, b), min(a, b) 
    while (b != 0):
        a, b = b, a % b
    return a

def primeFactors(n):
    primes = []
    m = int(sqrt(n)) + 1
    for i in range(2, m):
        while n % i == 0:
            primes.append(i)
            n //= i
    if (n != 1):
        primes.append(n)
    return primes

def findDivisors(n):
    divisors = []
    divisorsend = []
    m = int(sqrt(n)) + 1
    for i in range(1, m):
        if n % i == 0:
            divisors.append(i)
            divisorsend.append(n//i)
    if (divisors[-1] == divisorsend[-1]):
        divisorsend.pop()
    divisors += divisorsend[::-1]
    return divisors

def arrGenerator(n, n1, n2):
    arr = [0] * n
    for i in range(n):
        arr[i] = randint(n1, n2)
    return arr

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

def greedyKnapsack(price):
    coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    n = len(coins)
    need = [0] * n
    for i in range(n):
        num = price // coins[i]
        price -= num * coins[i]
        need[i] = num
        print (coins[i], ":", num)
    return need[i]

n = randint(2, 1000)
m = randint(2, 1000)
print("Random number n :", n, "\nRandom number m :", m)
print("GCD(n, m) =", gcd(n, m))
print("Prime factors n :", primeFactors(n))
print("Find divisors n :", findDivisors(n))

arr = arrGenerator(10, 1, 100)
print("Random array arr :", arr)
print("Bubble sort of arr :", bubbleSort(arr))
print("Insertion sort of arr :", insertionSort(arr))

print("Minimum number of coins for n :", n)
greedyKnapsack(n)