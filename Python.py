# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == 'K':
#     print(f'You are {weight / 0.45} pounds')
# elif unit.upper() == 'L':
#     print(f'You are {weight * 0.45} kilos')


# secret_number = 9
# i = 0
# while i < 3:
#     guess_number = int(input('Guess: '))
#     i += 1
#     if guess_number == secret_number:
#         print('You Won!')
#         break
# else:
#     print('You Failed!')


# command = ''
# started = False
# while True:
#     command = input('> ').lower()
#     if command == 'help':
#         print('''start - to start the car
# stop - to stop the car
# quit - to exit''')
#     elif command == 'start':
#         if started:
#             print('Car is already started')
#         else:
#             print('Car started...Ready to go!')
#             started = True
#     elif command == 'stop':
#         if not started:
#             print('Car is already stopped')
#         else:
#             print('Car stopped.')
#             started = False
#     elif command == 'quit':
#         break
#     else:
#         print("I don't understand that...")


# numbers = [1, 1, 1, 1, 5]
# for n in numbers:
#     output = ''
#     for x in range(n):
#         output += 'x'
#     print(output)


# list = [1, 2, 3, 2, 4, 5, 1]
# list2 = []
# for i in list:
#     if i in list2:
#         list.remove(i)
#     else:
#         list2.append(i)
# print(list)


# numbers = {
#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four',
#     '5': 'Five',
#     '6': 'Six'
# }
# phone = input('Phone: ')
# words = ''
# for ch in phone:
#     words += numbers.get(ch, '###') + ' '
# print(words)


# message = input("> ")
# words = message.split(' ')
# emojis = {
#     ":)": "Happy",
#     ":(": "Sad"
# }
# output = ''
# for word in words:
#     output += emojis.get(word, word) + ' '
# print(output)


# Exceptions:

# try:
#     age = int(input('Age: '))
#     print(f'Your Age: {age}')
#     print(2000 / age)
# except ValueError:
#     print("Age must be integer.")
# except ZeroDivisionError:
#     print("Age cannot be 0.")


# modules

# import utils
# import convertors
# from convertors import kg_to_lbs

# convertors.lbs_to_kg(124)
# kg_to_lbs(56)


# list = [54, 846, 855, -98, 5, -26, 0, 4, 98]
# print(f'Max Number: {utils.find_max(list)}')
# print(f'Min Number: {utils.find_min(list)}')

# -----------------------------
# packages

# from ecommerce.shipping import calc_shipping

# calc_shipping()

# Random

import random

# print(random.random())
# print(random.randint(1, 20))
# members = ['khalid', 'omer', 'salem', 'ali']
# print(f'Leader: {random.choice(members)}')

# class Dice:
#     def roll(self):
#         x = random.randint(1, 6)
#         y = random.randint(1, 6)
#         return x, y # python automatically return x ,y as a tuple

# dice = Dice()
# print(dice.roll())



# str1 = '123456789'
# rev_upper = lambda string: string.upper()[::-1]
# print(rev_upper(str1))


# [print(i) for i in range(1,101) if i % 2 == 0]


# Max = lambda a, b : a if(a > b) else b
# print(Max(1, 2))


# li = [5, 7, 22, 18, 10, 15, 30, 23, 20, 33]

# final_list = list(filter(lambda x: (x % 2 != 0), li))
# print(final_list)
# # the same ↓
# [print(i) for i in filter(lambda x : x % 2 != 0, li)]
# print("larger than 18:")
# [print(i) for i in filter(lambda x : x > 18, li)]


# multiplier = list(map(lambda x: x*2, li))
# print(multiplier)


# animals = ['dog', 'cat', 'parrot', 'rabbit']
# uppered_animals = list(map(lambda animal: animal.upper(), animals))
# print(uppered_animals)


from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print(sum)


# numbers = [2, 4, 6, 8, 10]
# square = list(map(lambda x : x * x, numbers))
# print(square)


# num1 = [4, 5, 6]
# num2 = [5, 6, 7]
# result = list(map(lambda n1, n2: n1+n2, num1, num2))
# print(result)


# a = ['khalid']
# b = ['omer']
# c = ['ali']
# d = ['ahmed']
# e = ['salem']
# names = a+b+c+d+e
# print(names)


# l = ['sat', 'bat', 'cat', 'mat']
# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)   # list == lambda x : list(x)


# tupley = ('python', 'ruby', 'php', 'c#')
# lang_len = list(map(lambda x : len(x), tupley))
# print(lang_len)


# strs = ['apple', 'and', 'a', 'donut']
# print(list(filter(lambda s: len(s) > 3, strs)))


# sum = lambda x, y : x + y
# print(sum(4,4))


def extraLongFactorials(n):
    return reduce(lambda x, y : x * y, range(1, n+1))
print(extraLongFactorials(25))
