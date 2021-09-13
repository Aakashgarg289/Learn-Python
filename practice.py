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
def matchingWords(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for i in words1:
        for j in words2:
            if i.lower() == j.lower():
                score += 1
    return score
if __name__ == '__main__':
    sentences = ["python is a good", "this is a snake", "harry is a good boy", "python is a programming language", "programming"]
    query = input("Please enter the query string???")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    print(scores)
    sortedSentenceScores = [sentscore for sentscore in sorted(zip(scores, sentences), reverse=True)]
    print(sortedSentenceScores)
    for score,item in sortedSentenceScores:
        if score!=0:
            print(f"\"{item}\": with a score of {score}")
        else:
            sortedSentenceScores.pop(score)
print(f"{len(sortedSentenceScores)} results found!!")
