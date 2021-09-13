# Single Line Comment
"""
Multi Line Comment

BUILT-IN MODULES
1. random
2. math
3. os
4. sys
5. platform
6. json

EXTERNAL MODULES
1. flask
2. django
3. requests
4. pyaudio
5. pydictionary
6. pandas
7. pygame
8. virtualenv
9. wikipedia
10. numpy
11. pipwin
12. pyttsx3
13. pyinstaller
14. wheel
15. gtts
16. SpeechRecognition
"""

# VARIABLES - IMMUTABLE
# num1 = 10
# num2 = 20
# num3 = 25.25
# str = "This is a string"
# print(num1 + num2)
# print(str)
# print(10 * 'Hello ')

# OBJECT INTROSPECTION
# print(type(str))
# print(dir(str))
# print(id(num1))

# TYPE CASTING + INPUT() + ESCAPE SEQUENCES + F-STRINGS
# num1 = input("Enter the number1: \n")
# num2 = input("Enter the number2: \n")
# avg = (int(num1) + int(num2))/2
# print(f"The average of two numbers {num1} and {num2} is: {avg}")

# STRINGS - IMMUTABLE
# str = "Aakash is the best programmer in the world"
# print(len(str))
# print(str.upper())
# print(str.lower())
# print(str.title())
# print(str.capitalize())
# print(str.count('m'))
# print(str.replace('is', 'are'))
# print(str.split(' '))
# # print(" and ".join(str))
# a = str.split(' ')
# print(" and ".join(a))
# print(str.isalnum())
# print(str.isalpha())
# print(str[::])
# print(str[::-1])

# LISTS - MUTABLE
# mylist = ["Aakash", "is", "the", "best"]
# print(mylist.count("Aakash"))
# print(mylist.append("In"))
# print(mylist)
# print(mylist.remove("In"))
# print(mylist)
# num1 = [1,2,3,4]
# num2 = [1,2,3,4]
# num = num1 + num2
# print(num)
# num.sort()
# num.reverse()
# print(num)

# TUPLE - IMMUTABLE
# tp = (1, )
# print(tp)

# DICTIONARY - MUTABLE
# dict1 = {"Aakash":"Programmer", "Manish":"Tester", "Divyanshu":"Developer"}
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# dict1["Rahul"] = "Cloud Engineer"
# print(dict1)
# l1 = []
# l2 = []
# for k, v in dict1.items():
#     l1.append(k)
#     l2.append(v)
# print(l1, l2)

# SWAPPING - 2-Methods
# a = 10
# b = 20
# temp = a
# a = b
# b = temp
# print(a, b)
# a, b = b, a
# print(a, b)

# SETS - MUTABLE
# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(1)
# s.add(2)
# print(s)
# print(s.pop())
# print(s)

# IF-ELSE + ONE LINE IF-ELSE
# num1 = 20
# num2 = 30
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# else:
#     print(f"{num2} is greater than {num1}")
# print(f"{num1} is greater than {num2}") if num1 > num2 else print(f"{num2} is greater than {num1}")

# FOR LOOP
# mylist = [1,2,3,4]
# list1 = [["Harry", "Programmer"], ["Aakash", "Developer"], ["Manish", "Manual-Tester"]]
# for i in mylist:
#     print(i)
# newdic = dict(list1)
# print(newdic)
# for k, v in newdic.items():
#     print(k, v)
# for index, item in list1:
#     print(index, item)

# FOR-ELSE
# lis = ["roti", "chawal", "sabji"]
# for i in lis:
#     print(i)
# else:
#     print("Yes")

# WHILE LOOP + QUIZ
# i = 0
# list1 = ["Aakash", 20, 545.54, int, float, 5]
# while i<len(list1):
#     if str(list1[i]).isnumeric() and list1[i] > 6:
#         print(list1[i])
#     i += 1

# OPERATORS
# num1 = 10
# num2 = 20
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 ** num2)
# print(num1 // num2)
# print(5 is num1)

# IS V/S ==
# a = [1,2,3]
# b = a
# print(a==b)
# print(a is b)

# FUNCTIONS
# def average(a, b):
#     return (a + b)/2

# v = average(10, 20)
# print(v)
# print(average.__doc__)

# ANONYMOUS OR LAMBDA FUNCTIONS
# v = lambda a, b: (a+b)/2
# print(v(10, 20))

# l1 = [[21,42], [73,24], [543,6532]]
# l1.sort(key=lambda x: x[1])
# print(l1)

# # RECURSION
# def repeat(n):
#     if n==10:
#         return n
#     return repeat(n+1)
# v = repeat(1)
# print(v)

# EXCEPTION HANDLING
# a = 10
# b = 0
# try:
#     c = a/b
# except Exception as e:
#     print(e)
# else:
#     print("This statement will not print any result on screen if exception statement executed...")
# finally:
#     print("This will always executed...")

# FILE HANDLING
# f = open('myfile.txt', 'w')
# f.write("Aakash is a good boy \n")
# f.close()

# with open('myfile.txt', 'r+') as f:
#     print(f.tell())
#     print(f.read())
#     f.write("Aakash is the best programmer in the world \n")
#     print(f.readlines())
#     print(f.tell())
#     f.seek(0)
#     print(f.read())

# SCOPE - LOCAL AND GLOBAL VARIABLES
# a = 10
# def change():
#     global a
#     a = 20
#     return a
# print(a)
# v = change()
# print(v)
# print(a)

# x = 89
# def aakash():
#     x = 20
#     def rohan():
#         global x
#         x = 88
#     print("before calling rohan: ", x)          # 20
#     rohan()
#     print("after calling rohan: ", x)           # 20
# aakash()
# print(x)                    # 88

# *ARGS AND **KWARGS
# def takePara(normal, *li, **ke):
#     print(normal)
#     for i in li:
#         print(i)
#     for k, v in ke.items():
#         print(k, v)
# normal = 10
# li = [1,2,3,4,5,6]
# ke = {"Aakash":"Programmer", "Manish":"Tester"}
# takePara(normal, *li, **ke)

# DECORATORS
# def fun1():
#     print("Subscribe Now!!")
# fun2 = fun1
# del fun1
# fun2()

# def func(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# print(func(1))

# def executor(func):
#     func("This")
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing Now...")
        func1()
        print("Executed")
    return nowexec()
@dec1
def aakash():
    print("Aakash is a programmer...")
# aakash = dec1(aakash)
aakash

# GENERATORS
# def gen(n):
#     for i in range(n):
#         yield i
# g = gen(10)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# h = "Aakash"
# ite = iter(h)
# print(ite.__next__())
# print(ite.__next__())
# print(ite.__next__())
# print(ite.__next__())

# ------------------ MODULES ----------------
# RANDOM
import random
# print(5 * random.random())
# print(random.randint(1, 5))

# DATETIME
import datetime
# print(datetime.datetime.now())

# PLATFORM
import platform
# print(platform.platform())
# print(platform.architecture())
# print(platform.machine())
# print(platform.processor())
# print(platform.python_compiler())

# PYDICTIONARY
from PyDictionary import PyDictionary
# dictionary = PyDictionary()
# inp = input("Enter any word for that you want to get the meaning.....\n")
# v = dictionary.meaning(inp)
# print(v)

# SKLEARN + SYS
import sklearn
import sys
# print(sklearn.__version__)
# print(sys.path)

# TIME
import time
# print(time.asctime(time.localtime(time.time())))

# OS
import os
# print(os.getcwd())
# print(os.listdir())
# print(os.path)

# REQUESTS
import requests
# url = "https://www.github.com/aakashgarg289"
# r = requests.get(url)
# text = r.text
# content = r.content
# print(text)
# print(r.status_code)
# print(content)
# print(r.status_code)

# JSON
import json
# data = '{"Aakash":"Programmer", "Manish":"Tester"}'
# dic = json.loads(data)
# print(type(dic))
# print(type(data))

# data2 = {"cars":['bmw', 'audi'],
#          "programmer":"aakash",
#          "tester":"manish",
#          "isbad": False
# }
# jscomp = json.dumps(data2)
# print(json.dumps(data2, indent=4, sort_keys=True))
# print(jscomp)
# print(type(jscomp))

# PICKLE
import pickle
# li = ["programmer", "developer", "tester", "analyst", "hr", "system-engineer"]
# file = "roles.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(li, fileobj)
# fileobj.close()
# file = "roles.pkl"
# fileobj = open(file, 'rb')
# roles = pickle.load(fileobj)
# print(roles)

# ENUMERATE
# li = ["programmer", "developer", "tester", "hr"]
# for index, item in enumerate(li):
#     if index%2 is not 0:
#         print(item)

# MAP
# numbers = ["3", "34", "54"]
# numbers = list(map(int, numbers))
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers[2] = numbers[2] + 1
# print(numbers[2])

# num = [1,2,3,1,2,3,1]
# # def sq(a):
# #     return a*a
# num = list(map(lambda a:a*a, num))
# print(num)

# sq = lambda x:x*x
# cub = lambda y:y*y*y
# li = [sq, cub]
# for i in range(5):
#     a = list(map(lambda x:x(i), li))
#     print(a)

# FILTER
# num = [1,2,3,4,5,6,7,8,9,32,54,22]
# def is_greater(num):
#     return num > 7

# a = list(filter(is_greater, num))
# print(a)

# REDUCE
from functools import reduce
# from functools import reduce
# list1 = [1,2,3,45,6]
# prod = reduce(lambda x,y:x*y, list1)
# print(prod)
# num = 1
# for i in list1:
#     num = num * i
# print(num)

# COMPREHENSIONS
# ls = []
# for i in range(1, 100):
#     if i%3==0:
#         ls.append(i)
# print(ls)

# ls = [i for i in range(1, 100) if i%3==0]
# print(ls)

# dic1 = {i:f"item {i}" for i in range(1, 100)}
# dic2 = {value:key for key,value in dic1.items()}
# print(dic2)

# dress = {dress for dress in ["dress1", "dress2", "dress1", "dress2"]}
# print(dress)

# evens = (i for i in range(100) if i%2==0)
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# for i in evens:
#     print(i)
# print(type(evens))


# COROUTINES
# def searcher():
#     import time
#     book = "This is a book on aakash and the book is a great one..."
#     time.sleep(4)

#     while True:
#         text = (yield)
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("text is not in the book")

# search = searcher()
# print("Search Started")
# next(search)
# print("Next method run")
# search.send("aakash")
# search.send("aakash")
# search.close()

# LRU CACHE
import time
# from functools import lru_cache
# @lru_cache(maxsize=32)
# def some_work(n):
#     time.sleep(3)
#     return n

# if __name__=='__main__':
#     print("Now Running some work..")
#     some_work(3)
#     some_work(5)
#     some_work(1)
#     some_work(7)
#     print("Done")
#     some_work(3)
#     some_work(3)
#     some_work(3)
#     print("Called Again...")

# REGULAR EXPRESSION
import re
# mystr = """Registered Office Address: Tata Sky Ltd., Unit 301 to 305, 3rd Floor, Windsor Off, C.S.T. Road, Kalina, Santacruz (East), Mumbai 400098.
# Tel: +91-22-66133000 | Fax: +91-22-66133030 | E-mail: contact@tatasky.com
# CIN: U9210MH2001PLC130365
# Tata® Tata Sons Private Limited. All Sky Trademarks, and any intellectual property they contain, are owned by Sky International AG. Used under License by Tata Sky Limited.
# All IPR in and to the Website vests with Tata Sky Limited from 2020 onwards."""
# patt = re.compile(r'from')
# patt = re.compile(r'.')
# patt = re.compile(r'.ted')
# patt = re.compile(r'^Registered')
# patt = re.compile(r'onwards.$')
# patt = re.compile(r'ai*')
# patt = re.compile(r'ai+')
# patt = re.compile(r'ai{1}')
# patt = re.compile(r'(ai){2}')
# patt = re.compile(r'ai{1} | t')
# patt = re.compile(r'\d{2}-\d{2}-\d{8}')
# matches = patt.finditer(mystr)
# for i in matches:
#     print(i)
#     print(type(i))
    # print(i[461:471])
