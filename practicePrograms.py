# AGE CALCULATOR
# if __name__=='__main__':
#     isAge = False
#     isYear = False
#     while True:
#         age = input("Please Enter your Age Or Year of birth???\n")
#         new = ""
#         if age.isnumeric():
#             if len(age) == 4:
#                 isYear = True
#             else:
#                 isAge = True

#             if int(age)>2021 or (int(age)<1 and isAge):
#                 print("You are not born yet...")
#                 exit()

#             if (int(age)<1900 and isYear):
#                 print("You seems to be oldest person alive...")
#                 exit()

#             if isAge:
#                 age = 2021 - int(age)

#             print(f"You will be 100 years old in {int(age) + 100}")
#             interestedYear = int(input("Enter the year you want to know your age???"))
#             print(f"You will be {interestedYear-int(age)} years old in {interestedYear}")
#         else:
#             print("Your input is wrong and not a number....Please Enter a number....")

# DISTRIBUTION OF EQUAL APPLES IN MEMBERS
# apples = int(input("Enter the no. of apples: \n"))
# mn = int(input("Enter the minimum no. to check: \n"))
# mx = int(input("Enter the maximum no. to check: \n"))
# for i in range(mn, mx+1):
#     if i%2==0:
#         print(f"Apples can be distributed between {i} members")
#     else:
#         print(f"Apples are not divisible by {i} members")

# PRINTING THE LIST REVERSE
# user_size = int(input("Enter the size of list: \n"))
# user_list = []
# for i in range(user_size):
#     element = int(input("Enter the number of a list one by one: \n"))
#     user_list.append(element)
# print(f"Your list is : {user_list}")

# re1 = user_list[:]
# re1.reverse()
# print(f"Reverse List 1 : {re1}")

# re2 = user_list[::-1]
# print(f"Reverse List 2 : {re2}")

# re3 = user_list[:]
# for i in range(len(re3)//2):
#     re3[i], re3[len(re3) - i -1] = re3[len(re3) - i -1], re3[i]
# print(f"Reverse List 3 : {re3}")

# NEXT PALINDROME
# def next_pali(n):
#     n = n+1
#     while not is_pali(n):
#         n += 1
#     return n

# def is_pali(n):
#     return str(n) == str(n)[::-1]

# user = int(input("How many numbers you want to give: \n"))
# list1 = []
# for i in range(user):
#     numb = int(input("Enter a number one by one to get the next palindrome and value must be greater than 10: "))
#     list1.append(numb)
# print(list1)

# for i in list1:
#     print(f"The Next Palindrome for {i} is {next_pali(i)}")
#     if is_pali(i):
#         print(f"{i} is a palindrome number...")
#     else:
#         print(f"{i} is not a palindrome number...")

# SEARCH ENGINE
# def matchingWords(sentence1, sentence2):
#     words1 = sentence1.split(" ")
#     words2 = sentence2.split(" ")
#     score = 0
#     for i in words1:
#         for j in words2:
#             if i.lower() == j.lower():
#                 score += 1
#     return score
# if __name__ == '__main__':
#     sentences = ["python is a good", "this is a snake", "harry is a good boy", "python is a programming language", "programming"]
#     query = input("Please enter the query string???")
#     scores = [matchingWords(query, sentence) for sentence in sentences]
#     print(scores)
#     sortedSentenceScores = [sentscore for sentscore in sorted(zip(scores, sentences), reverse=True)]
#     print(sortedSentenceScores)
#     for score,item in sortedSentenceScores:
#         if score!=0:
#             print(f"\"{item}\": with a score of {score}")
#         else:
#             sortedSentenceScores.pop(score)
#     print(f"{len(sortedSentenceScores)} results found!!")

# GUESS A NUMBER GAME
import random
# def guess_game(a, b, ran):
#     guesses = 1
#     guess = int(input(f"Guess a number between {a} and {b} \n"))
#     while guess!=ran:
#         if guess>ran:
#             guess = int(input("Enter a smaller number..\n"))
#             guesses +=1
#         else:
#             guess = int(input("Enter a greater number..\n"))
#             guesses += 1
#     print(f"You guess a number in {guesses} guesses...")
#     return guesses

# if __name__ == '__main__':
#     a = int(input("Enter the value of a: \n"))
#     b = int(input("Enter the value of b: \n"))
#     ran = random.randint(a, b)
#     print("Player 1 Turn: ")
#     g1 = guess_game(a, b, ran)
#     print("Player 2 Turn: ")
#     g2 = guess_game(a, b, ran)

#     if g1>g2:
#         print("Player 2 won the match")
#     elif g1<g2:
#         print("Player 1 won the match")
#     else:
#         print("It's a tie...")

# FAULTY TABLE
import random
# def fualtyTable(number):
#     wrong = random.randint(1, 9)
#     table = [i * number for i in range(1, 11)]
#     table[wrong] = table[wrong] + random.randint(0,10)
#     return table

# def isCorrect(table, number):
#     for i in range(1, 11):
#         if table[i-1] != i*number:
#             return i-1
#     return None

# if __name__ == '__main__':
#     user = int(input("Enter a table number you want to get???"))
#     table = fualtyTable(user)
#     print(table)
#     wrongindex = isCorrect(table, user)
#     print(f"The table is wrong at index {wrongindex} and at {wrongindex + 1} position")

# GENERATE FUNNY NAMES
import random
# def jumble_word(first_name, last_name, number):
#     for i in range(number):
#         # Changing the last name
#         jumbled_name = first_name[i] + " " + last_name[random.randint(0, number - 1)]
#         print(jumbled_name)

# if __name__ == "__main__":
#     number = int(input("Enter the number of names:\n"))
#     nameList = []
#     first_name = []
#     last_name = []
#     # Asking the name of the friends
#     for i in range(number):
#         name = input("Enter the names of your friends one by one: \n")
#         # append to the name list
#         nameList.append(name)
#     # Splitting the elements of the name list
#     for ele in nameList:
#         split_name = ele.split(" ")
#         print(split_name)
#         # For the first name
#         first_name.append(split_name[0])
#         # For the second name
#         last_name.append(split_name[1])

#     jumble_word(first_name, last_name, number)

# SNAKE WATER GUN GAME
import random
# print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t Welcome To My Snake | Water | Gun Game")
# print("Please enter some value as Type - S for Snake | W - for Water | G for Gun | Q for Quit....")
# print("Total lives are 10....")
# print("Computer And Users Both Initial Lives are 0...")
# lives = 10
# comp_score = 0
# user_score = 0
# for i in range(1, lives+1):
#     choose = ["s", "w", "g"]
#     comp = random.choice(choose)
#     user = input("Enter the value: \n").lower()
#     if user.isalpha():
#         if (user == "s" and comp == "s") or (user == "w" and comp == "w") or (user == "g" and comp == "g"):         # For Users and Computer Both
#             print(f"There is a Tie!!!!\nComputer chooses {comp} and You chooses {user}.")
#             comp_score = comp_score + 1
#             user_score = user_score + 1
#             print("Computer Score: ", comp_score)
#             print("Your Score: ", user_score)
#             print("Total lives are left: ", lives-i)
#         elif (user == "s" and comp == "w") or (user == "w" and comp == "g") or (user == "g" and comp == "s"):        # For Users
#             print(f"User has Won!!!\nComputer chooses {comp} and You chooses {user}.")
#             user_score = user_score + 1
#             print("Computer Score: ", comp_score)
#             print("Your Score: ", user_score)
#             print("Total lives are left: ", lives - i)
#         elif (user == "s" and comp == "g") or (user == "w" and comp == "s") or (user == "g" and comp == "w"):           # For Computer
#             print(f"Computer has Won!!!!\nComputer chooses {comp} and You chooses {user}.")
#             comp_score = comp_score + 1
#             print("Computer Score: ", comp_score)
#             print("Your Score: ", user_score)
#             print("Total lives are left: ", lives - i)
#         elif user == "q":
#             quit()
#         else:
#             print("Try Again!! You entered wrong input...")
#         if (lives - i) <= 0:
#             print("Game is over!!!")
#             print("Computer Score: ", comp_score)
#             print("Your Score: ", user_score)
#             if user_score > comp_score:
#                 print("You Won this game...")
#             else:
#                 print("Computer won this game....")
#     else:
#         print("Try Again!! You entered wrong input...")

# PATTERN PRINTING
# rows = int(input("How many rows you want to print: \n"))
# inpu = int(input("Type 1 for printing pattern in increasing order or 0 for decreasing order: \n"))
# correct = bool(inpu)

# if correct == True:
#     for i in range(1, rows+1):
#         for j in range(1, i+1):
#             print("*", end="")
#         print()
# elif correct == False:
#     for i in range(rows, 0, -1):
#         for j in range(1, i+1):
#             print("*", end="")
#         print()

# if correct == True:
#     for i in range(1, rows+1):
#         print("*" * i)
# if correct == False:
#     for i in range(rows, 0, -1):
#         print("*" * i)

# LIBRARY MANAGEMENT SYSTEM
import datetime
# class Library:
#     def __init__(self, li, name):
#         self.booklist = li
#         self.name = name
#         self.lenddict = {}
#     def displayBook(self):
#         print(f"We have following books in our library: {self.name}")
#         for book in self.booklist:
#             print(book)
#     def addBook(self, book):
#         self.booklist.append(book)
#         print("Book has been added to the list")
#     def lendBook(self, user, book):
#         if book not in self.lenddict.keys():
#             self.lenddict.update({book:user})
#             print("Book dictionary has been updated.. You can take the book now!!!")
#             with open("librarystore.txt", "a") as f:
#                 f.write(f"{str(self.lenddict)} : {str(datetime.datetime.now())} \n")
#         else:
#             print(f"Book is already being used by {self.lenddict[book]}")
#     def returnBook(self, book):
#         self.lenddict.pop(book)

# if __name__ == '__main__':
#     aakash = Library(["Python Programming", "HeadFirstJava", "Python", "SeleniumWithPython"], "Aakash's Library")
#     while True:
#         print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Hi, Welcome To The {aakash.name}...")
#         user = input("Enter your name: \n")
#         print(f"Hi, {user} \n Type-1 For Lend The Books\n Type-2 For Return The Books\n Type-3 For Display the Books\n Type-4 For Adding a Book\n")
#         user_input = int(input())
#         if user_input == 1:
#             book = input("Enter the name of the book you want to lend??")
#             user = user
#             aakash.lendBook(user, book)
#         elif user_input == 2:
#             book = input("Enter the name of the book you want to return???")
#             aakash.returnBook(book)
#         elif user_input == 3:
#             aakash.displayBook()
#         elif user_input == 4:
#             book = input("Enter the name of the book you want to add???")
#             aakash.addBook(book)
#         else:
#             print("Not a valid option!!!")
#         print("Press c to Continue and q to Quit")
#         user_input2 = ""
#         while (user_input2!="c" and user_input2!="q"):
#             user_input2 = input()
#             if user_input2 == "q":
#                 exit()
#             elif user_input2 == "c":
#                 continue

# REAL TIME NEWS READER - BASED ON YOUR CHOICE
import requests
import json
# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(str)

# if __name__ == '__main__':
#     speak("Hi, I am your news teller. Welcome To Listen All The Latest News Of Today")
#     speak("Please Enter, What type of news you want to listen?? 1. Related to Technology, 2. Related to Sports, 3. Related to Science")
#     inp = input("Enter here: \n").lower()
#     if inp == "technology":
#         url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=a1a20bc8d8d049a49e54568159f96d26"
#         r = requests.get(url).text
#         print(r)
#         news = json.loads(r)
#         title = news["articles"][:5]
#         print(len(title))
#         j = 0
#         for i in title:
#             print(i['title'])
#             speak(i['title'])
#             if j<(len(title)-1):
#                 speak("Moving to the next")
#                 j += 1
#             else:
#                 speak("Thanks for listening....")
                    
#     elif inp == "science":
#         url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=a1a20bc8d8d049a49e54568159f96d26"
#         r = requests.get(url).text
#         print(r)
#         news = json.loads(r)
#         title = news["articles"][:5]
#         j = 0
#         for i in title:
#             print(i['title'])
#             speak(i['title'])
#             if j<(len(title)-1):
#                 speak("Moving to the next")
#                 j += 1
#             else:
#                 speak("Thanks for listening....")
            
#     elif inp == "sports":
#         url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=a1a20bc8d8d049a49e54568159f96d26"
#         r = requests.get(url).text
#         print(r)
#         news = json.loads(r)
#         title = news["articles"][:5]
#         j = 0
#         for i in title:
#             print(i['title'])
#             speak(i['title'])
#             if j<(len(title)-1):
#                 speak("Moving to the next")
#                 j += 1
#             else:
#                 speak("Thanks for listening....")

#     elif inp == "quit":
#         quit()
#     else:
#         print("Please provide correct details...")
#         speak("Please provide correct details...")

# Pickling Iris - UCI ML REPOSITORY
import requests
import pickle
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# req = requests.get(url).text
# print(req)
# l1 = req.split("\n")
# print(l1)
# l2 = [item.split(",") for item in l1 if len(item)!=0]
# print(l2)
# with open("myiris.pkl", "wb") as f:
#     pickle.dump(l2, f)
# with open("myiris.pkl", "rb") as f:
#     print(pickle.load(f))

# PICKLING ADULT - UCI ML REPOSITORY
import requests
import pickle
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
# r = requests.get(url).text
# print(r)
# print(type(r))
# re = r.split("\n")
# print(re)
# print(type(re))
# li = [i.split(',') for i in re if i!=0]
# print(li)
# with open("myadultdata", "wb") as f:
#     pickle.dump(re, f)
# with open("myadultdata", "rb") as f:
#     pickle.load(f)

# PICKLING WINE - UCI ML REPOSITORY
import requests
import pickle
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
# r = requests.get(url).text
# print(r)
# print(type(r))
# re = r.split("\n")
# print(re)
# # print(type(re))
# li = [i.split(',') for i in re if i!=0]
# print(li)
# with open("wine.pkl", "wb") as f:
#     pickle.dump(re, f)
# with open("wine.pkl", "rb") as f:
#     pickle.load(f)

# CALCULATOR
# print("\t\t\t\t\t\t\t\t\t\t\t Welcome To My Calculator")
# while True:
#     num1 = input("Enter the number1: ")
#     num2 = input("Enter the number2: ")
#     if num1.isnumeric() and num2.isnumeric():
#         print("What Operation you want to perform:  + | - | * | / | %")
#         operator = input("Enter the operator: ")
#         if operator == '+':
#             user = input("You want the value in decimals or integers.... Type i for int and d for decimals: \n")
#             if user=="i":
#                 print(int(num1) + int(num2))
#             else:
#                 print(float(num1) + float(num2))
#         elif operator == '-':
#             user = input("You want the value in decimals or integers.... Type i for int and d for decimals: \n")
#             if user == "i":
#                 print(int(num1) - int(num2))
#             else:
#                 print(float(num1) - float(num2))
#         elif operator == '*':
#             user = input("You want the value in decimals or integers.... Type i for int and d for decimals: \n")
#             if user == "i":
#                 print(int(num1) * int(num2))
#             else:
#                 print(float(num1) * float(num2))
#         elif operator == '/':
#             user = input("You want the value in decimals or integers.... Type i for int and d for decimals: \n")
#             if user == "i":
#                 print(int(num1) / int(num2))
#             else:
#                 print(float(num1) / float(num2))
#         elif operator == '%':
#             user = input("You want the value in decimals or integers.... Type i for int and d for decimals: \n")
#             if user == "i":
#                 print(int(num1) % int(num2))
#             else:
#                 print(float(num1) % float(num2))
#         else:
#             print("You entered the wrong operator")
#     elif num1=="q" or num2 == "q":
#         break
#     else:
#         print("You entered wrong input. Enter the numbers only!!")
# print("\t\t\t\t\t\t\t\t\t\t\t Thanks For Using My Calculator")

# FAULTY CALCULATOR - 45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
# print("\t\t\t\t\t\t\t\t\t\t\t Welcome To My Faulty Calculator Specially Designed For Cheaters....")
# while True:
#     num1 = input("Enter the number1: ")
#     num2 = input("Enter the number2: ")
#     if num1.isnumeric() and num2.isnumeric():
#         print("What Operation you want to perform:  + | - | * | / | %")
#         operator = input("Enter the operator: ")
#         if operator == '+':
#             if num1=="56" and num2=="9":
#                 print("77")
#             else:
#                 user = input("You want the value in decimals or integers.... Type i for int and d for decimals: \n")
#                 if user=="i":
#                     print(int(num1) + int(num2))
#                 else:
#                     print(float(num1) + float(num2))
#         elif operator == '-':
#             user = input("You want the value in decimals or integers.... Type i for int and d for decimals: \n")
#             if user == "i":
#                 print(int(num1) - int(num2))
#             else:
#                 print(float(num1) - float(num2))
#         elif operator == '*':
#             if num1=="45" and num2=="3":
#                 print("555")
#             else:
#                 user = input("You want the value in decimals or integers.... Type i for int and d for decimals: \n")
#                 if user == "i":
#                     print(int(num1) * int(num2))
#                 else:
#                     print(float(num1) * float(num2))
#         elif operator == '/':
#             if num1=="56" and num2=="6":
#                 print("4")
#             else:
#                 user = input("You want the value in decimals or integers.... Type i for int and d for decimals: \n")
#                 if user == "i":
#                     print(int(num1) / int(num2))
#                 else:
#                     print(float(num1) / float(num2))
#         elif operator == '%':
#             user = input("You want the value in decimals or integers.... Type i for int and d for decimals: \n")
#             if user == "i":
#                 print(int(num1) % int(num2))
#             else:
#                 print(float(num1) % float(num2))
#         else:
#             print("You entered the wrong operator")
#     elif num1=="q" or num2 == "q":
#         break
#     else:
#         print("You entered wrong input. Enter the numbers only!!")
# print("\t\t\t\t\t\t\t\t\t\t\t Thanks For Using My Calculator")

# GUESSING A NUMBER GAME
# def play_again():
#     print("Thanks For playing the game...")
#     user = input("You want to play again??? Type 'y' for yes and 'n' for no \n").lower()
#     if user == "y":
#         start(30, 5)
#     else:
#         print("Thanks For playing the game...")
#         quit()

# def start(guess_number, no_of_guesses):
#     print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t Welcome To My Guess The Number Game....")
#     print("Please Enter the number between 1 and 50....")
#     print("Total number of gueeses are :",no_of_guesses)
#     for i in range(1, no_of_guesses+1):
#         user_number = input("Enter the number or your guess: \n")
#         if user_number.isnumeric():
#             if int(user_number) == guess_number:
#                 print("Hey, You won the game!!!")
#                 print("No of guesses left: ", no_of_guesses - i)
#                 print("No of guesses you took to finish the game: ", no_of_guesses-(no_of_guesses-i))
#                 play_again()
#             elif int(user_number) < guess_number:
#                 print("Oh! Your guess number is less than the correct number")
#                 print("No of guesses left: ", no_of_guesses-i)
#                 if (no_of_guesses-i)<=0:
#                     print("Sorry, You lose the game..")
#                     play_again()
#             else:
#                 print("Oh! Your guess number is greater than the correct number")
#                 print("No of guesses left: ", no_of_guesses - i)
#                 if (no_of_guesses - i) <= 0:
#                     print("Sorry, You lose the game..")
#                     play_again()
#         elif user_number == "q":
#             play_again()
#         else:
#             print("Try Again...")

# if __name__ == '__main__':
#     start(30, 5)

# HEALTH MANAGEMENT SYSTEM
# def getdate():
#     import datetime
#     return datetime.datetime.now()

# def aakash(client_name):
#     if client_name.isalpha() and client_name == 'aakash':
#         print("Hi", client_name)
#         print("You want to lock the data or retrieve the data...\t\t Type - 1 for Lock and Type - 2 for Retrieve")
#         query = int(input("Type: "))
#         if query == 1:
#             print("What do you want to lock....\t Type - 1 for Aakash Exercise and Type - 2 for Aakash Diet")
#             lock = int(input(""))
#             if lock == 1:
#                 with open("aakashexercise.txt", "a") as f:
#                     inpu = input("Enter: \n")
#                     f.write(str(getdate()) + " " + inpu + "\n")
#                     print("Success")
#             else:
#                 with open("aakashdiet.txt", "a") as f:
#                     inpu = input("Enter: \n")
#                     f.write(str(getdate()) + " " + inpu + "\n")
#                     print("Success")
#         else:
#             print("What do you want to retrieve.... Type 1 for Aakash Exercise and Type 2 for Aakash Diet")
#             retrieve = int(input(""))
#             if retrieve == 1:
#                 with open("aakashexercise.txt", "r") as f:
#                     print(f.read())
#             else:
#                 with open("aakashdiet.txt") as f:
#                     print(f.read())
#     elif client_name.isalpha() and client_name == 'harry':
#         print("Hi", client_name)
#         print("You want to lock the data or retrieve the data...\t\t Type - 1 for Lock and Type - 2 for Retrieve")
#         query = int(input("Type: "))
#         if query == 1:
#             print("What do you want to lock....\t Type - 1 for Exercise and Type - 2 for Diet")
#             lock = int(input(""))
#             if lock == 1:
#                 with open("harryexercise.txt", "a") as f:
#                     inpu = input("Enter: \n")
#                     f.write(str(getdate()) + " " + inpu + "\n")
#                     print("Success")
#             else:
#                 with open("harrydiet.txt", "a") as f:
#                     inpu = input("Enter: \n")
#                     f.write(str(getdate()) + " " + inpu + "\n")
#                     print("Success")
#         else:
#             print("What do you want to retrieve.... Type 1 for Exercise and Type 2 for Diet")
#             retrieve = int(input(""))
#             if retrieve == 1:
#                 with open("harryexercise.txt", "r") as f:
#                     print(f.read())
#             else:
#                 with open("harrydiet.txt") as f:
#                     print(f.read())
#     elif client_name.isalpha() and client_name == 'rohan':
#         print("Hi", client_name)
#         print("You want to lock the data or retrieve the data...\t\t Type - 1 for Lock and Type - 2 for Retrieve")
#         query = int(input("Type: "))
#         if query == 1:
#             print("What do you want to lock....\t Type - 1 for Exercise and Type - 2 for Diet")
#             lock = int(input(""))
#             if lock == 1:
#                 with open("rohanexercise.txt", "a") as f:
#                     inpu = input("Enter: \n")
#                     f.write(str(getdate()) + " " + inpu + "\n")
#                     print("Success")
#             else:
#                 with open("rohandiet.txt", "a") as f:
#                     inpu = input("Enter: \n")
#                     f.write(str(getdate()) + " " + inpu + "\n")
#                     print("Success")
#         else:
#             print("What do you want to retrieve.... Type 1 for Exercise and Type 2 for Diet")
#             retrieve = int(input(""))
#             if retrieve == 1:
#                 with open("rohanexercise.txt", "r") as f:
#                     print(f.read())
#             else:
#                 with open("rohandiet.txt") as f:
#                     print(f.read())
#     elif client_name == "q":
#         quit()
#     else:
#         print("Try Again!! You entered the wrong input..")

# while True:
#     def start():
#         print("\t\t\t\t\t\t\t\t\t\t\t\t\t Welcome To My Health Management System")
#         print("Hi, For what client you want to lock or retrieve the data...\t Type - [Aakash] for Aakash.\t Type - [Harry] for Harry. \t Type - [Rohan] for Rohan")
#         client_name = input("Enter Your Name: \n").lower()
#         aakash(client_name)

#     if __name__=='__main__':
#         start()

# HEALTHY PROGRAMMER
# Water - water.mp3 - 3.5L - Drank - log -> Time
# Eyes - eyes.mp3 - 30 min - Done - log -> Time
# Physical Activity - physical.mp3 - 45 min - Done - log -> Time
from pygame import mixer
from datetime import datetime
from time import time
# def musiconloop(file, stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#     while True:
#         a = input()
#         if a == stopper:
#             mixer.music.stop()
#             break
# def log_now(msg):
#     with open("mylogs.txt", "a") as f:
#         f.write(f"{msg} {datetime.now()}\n")

# if __name__=='__main__':
#     init_water = time()
#     init_eyes = time()
#     init_exer = time()
#     watersecs = 5
#     eyessecs = 10
#     exersecs = 20

#     while True:
#         if time() - init_water > watersecs:
#             print("Water Drinking Time... Enter drank to stop the alarm")
#             musiconloop("Water Sound.mp3", "drank")
#             init_water = time()
#             log_now("Water Drank at: ")
#         if time() - init_eyes > eyessecs:
#             print("Eyes Resting Time... Enter eyes to stop the alarm")
#             musiconloop("Rest.mp3", "eyes")
#             init_eyes = time()
#             log_now("Eyes Rest at: ")
#         if time() - init_exer > exersecs:
#             print("Exercise Time... Enter ex to stop the alarm")
#             musiconloop("Exercise.mp3", "ex")
#             init_exer = time()
#             log_now("Done Exercise at: ")