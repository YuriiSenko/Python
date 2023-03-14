# def add(num1: int, num2: int):
#     return num1 + num2
#
#
# result = add(int(input()), int(input()))
# # result2 = add(result, 6)
# # result3 = add(result2, 10)
# print(result)

# def custom_reverse(text: str) -> str:
#     temp_text = ''
#     i = len(text) - 1  # значення по якому ми можем пройтись (довжина стрічки - 1)
#     while i >= 0:
#         temp_text += text[i]
#         i -= 1
#     return temp_text
#
#
# resultik = custom_reverse(text='demo text')
# print(resultik)

# just for fun
# text = input()[::-1]
# txt = []
# for j in text:
#     txt.append(j)
# print(txt)


# stepin = 4
#
# if stepin == 1:
#     def to_pow(n):
#         return n
#
# else:
#     def to_pow(n):
#         return n**stepin
#
# result = to_pow(3)
# print(result)


# def make_pizza(*ingridients):
#     for el in ingridients:
#         print(el)
#
#
# make_pizza("cheese")
# make_pizza("chesese", "tomato")
# make_pizza("chesese", "tomato", "peperoni")

# def build_profile(**user_info):
#     for key, value in user_info.items():
#         print(f"{key}: {value}")
#
#
# build_profile(user_name="Mariia", last_name="Levytska")
# build_profile(user_name="Mariia", last_name="Levytska", age=23)


# ---------------------------------------------------------------------------------------------------------
# def isPalindrome(inputString: str) -> bool:
#     if inputString == inputString[::-1]:
#         return True
#     return False
# #
#
# text = input("Enter text: ")
#
# inputik = isPalindrome(text)
# if inputik:
#     print("Is palindrome")
# else:
#     print("Is not palindrome")
# читается ли наше слово одинаково со всех сторон

# Также можно напрямую если знаем что inputik = isPalindrome(text) больше не понадобится
# text = input("Enter text: ")

# if isPalindrome(text):
#     print("Is palindrome")
# else:
#     print("Is not palindrome")
# ------------------------------------------------------------------------------------------------------------

# n_1 = float(input('enter number: '))
# n_2 = float(input('enter number: '))
# operation = input('enter a sign ')
#
#
# def summa(a, b):
#     return a + b
#
#
# def minus(a, b):
#     return a - b
#
#
# def divide(a, b):
#     return a / b
#
#
# def multiple(a, b):
#     return a * b
#
#
# if operation == '+':
#     print(summa(n_1, n_2))
# elif operation == '-':
#     print(minus(n_1, n_2))
# elif operation == '/':
#     if n_2 == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(divide(n_1, n_2))
# elif operation == '*':
#     print(multiple(n_1, n_2))
# else:
#     print('Неверная операция')

# def factorial_recursive(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial_recursive(n-1)
#
# print(factorial_recursive(4))
# обьяснение в тетрадке с собакой

# Чи потрапляє число в заданий діапазон
# def isIndiapason(from1, to, isValue) -> bool:
#     if to >= isValue >= from1:
#         return True
#     return False
#
#
# from2 = int(input())
# tO = int(input())
# isVaLue = int(input())
#
# if isIndiapason(from2, tO, isVaLue):
#     print('In')
# else:
#     print('No')



# 6. Написати лямду функцію які значення в списку паліндромом
# list_1 = ['Java', 'php', 'Python', 'afa']
# polindrom = list(filter(lambda x: x == x[:: -1], list_1))
# print(polindrom)

# def isRectangle(side_a, side_b, side_c, side_d) -> bool:
#     if side_a ** 2 + side_b ** 2 == side_c ** 2 + side_d ** 2:
#         return True
#     return False
#
#
# def rectangle_square(side_a, side_b) -> bool:
#     result = side_a * side_b
#     return result
#
#
# def isSquare(side_a, side_b, side_c, side_d) -> bool:
#     if side_a == side_b == side_c == side_d:
#         return True
#     return False
#
#
#
# side_1 = bool(input())
# side_2 = bool(input())
# side_3 = bool(input())
# side_4 = bool(input())
#
#
# if isRectangle(side_1, side_2, side_3, side_4):
#     s = rectangle_square(side_1, side_2)
#     print(s)
# elif isSquare(side_1, side_2, side_3, side_4):
#     print('Square')
# else:
#     print('No')


# Task 0

# student_list = {
#     1: 'Mike',
#     2: 'Joe',
#     3: 'Pierre',
#     4: 'Joa'
# }
#
# number = int(input('Do it: '))
# if number in student_list:
#     print(student_list.get(number), 'welcome')
# else:
#     print('You are not a student')

# Task 5.1. Print all words and their frequency in the text (by Counter)

from collections import Counter

text = "one two three one four five seven ten seven one"
text = text.split()
words_frequency = Counter(text)
print(words_frequency)

# Task 5.2. Print all words and their frequency in the text (by dictionary and loop)

text = "one two three one four five seven ten seven one"
text = text.split()
words = {}
for i in text:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1
print(words)




