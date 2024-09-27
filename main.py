# import random


# def roll_ball():
#     rand_roll = random.randint(1, 8)

#     if rand_roll == 1:
#         return "Outlook good"
#     elif rand_roll == 2:
#         return "You may rely on it"
#     elif rand_roll == 3:
#         return "Ask again later"
#     elif rand_roll == 4:
#         return "Concentrate and ask again"
#     elif rand_roll == 5:
#         return "Reply hazy, try again"
#     elif rand_roll == 6:
#         return "It is certain"
#     elif rand_roll == 7:
#         return "My reply is no"
#     elif rand_roll == 8:
#         return "My sources say no"


# while True:
#     input("Ask Me A Query Traveler:")
#     print(roll_ball())

#     play_again = input("would you like to roll again? type 'y' to roll again or click the 'Enter' key to quit: ")
#     if play_again.lower() != 'y':
#         print("Goodbye Traveler MUAHAHAH")
#         break

# for x in range(1, 10):
#     print(x)

# for i in range(2, 100, 2):
#     print(i)

# phrase = 'The quick brown fox jumps over the lazy dog'¡

# for i in phrase:
#     if i not in ['a', 'e', 'i', 'o', 'u', ' ']:
#         print(i)

# range_list = []

# for i in range(1, 101):
#     if i % 3 == 0:
#         range_list.append('Fizz')
#     if i % 5 == 0:
#         range_list.append('Buzz')
#     if i % 3 == 0 and i % 5 == 0:
#         range_list.append("FizzBuzz")
#     else:
#         range_list.append(i)

# print(range_list)


# list = [1, 2, 3, 5, 6, 7, 8, 9, 10]

# list.insert(list.index(5), 4)
# print(list)


# x = 1

# while x < 6:
#     print(x)
#     x += 1

# while True:
#     color_question = input("What is your favorite color?('quit' to end)")

#     if color_question.lower() == 'quit':
#         print('BYEEE')
#         break
#     else:
#         print(f'{color_question} is nice!')


# for i in range(1, 10):
#     if i > 1 and i < 8:
#         print(i)


# height = int(input('Hello! how high would you like your tree?'))

# row = 1

# while row <= height:
#     spaces = " " * (height - row)
#     stars = "*" * (2 * row - 1)
#     print(spaces + stars)
#     row += 1


# tree_row_one = '    *   '
# tree_row_two = '    * *  '
# tree_row_three = '  * * * '
# tree_row_four = ' * * * *'
# tree_row_five = '* * * * *'


# height = int(input('Hello! How tall would you like your christmas tree friend?'))
# star = '* '

# for i in range(1, height + 1):
#     spaces = ' ' * (height - i)
#     stars = star * i
#     print(f"{spaces}{stars}")


# trunk_row = '   * * *  '
# trunk = (trunk_row + '\n') * height

# print(trunk)


# for num in range(1, 21):
#     print(num)
#     if num == 15:
#         break


# input_string = "1111111devpipeline2222222"
# output_string = ""


# for char in input_string:
#     if char.isdigit():
#         continue
#     output_string += char

#     if output_string == "devpipeline":
#         break

# print(output_string)

# import random
# real_num = random.randint(1, 100)

# tries = 0

# print("I'm thinking of a number between 1 and 100.")

# while True:
#     guess = int(input("What is your guess? "))

#     tries += 1

#     if guess < real_num:
#         print(f"{guess} is too low")
#     elif guess > real_num:
#         print(f"{guess} is too high")
#     else:
#         print(f"That's correct!!!! {guess} is the right number!!! It only took you {tries} tries")

#         if tries > 10:
#             print("You should guess better next time!")
#         elif tries == 1:
#             print("You did it your first try!!!")
#         elif tries > 1 and tries < 6:
#             print(f"Close to perfect you did it under {tries} tries")
#         else:
#             tries < 10
#             print("Extra points for using less tries than the last person!")
#             break


# print("**LEAP YEAR MACHINE**")

# while True:
#     guess = int(input("Please enter a leap year after 1752: "))

#     if guess < 1752:
#         print('Please pick a year after 1752')
#     elif (guess % 4 == 0 and guess % 100 != 0) or (guess % 400 == 0):
#         print(f'{guess} is a Leap Year!')
#     else:
#         print(f'{guess} is not a leap year :( try again')


# month = (' ' * 6)+'September 2021\n'

# days_of_the_week = (' '*2)+"S" + (' '*2)+"M" + (' '*2)+"T"+(' '*2) + "W" + (' '*2)+"T" + (' '*2) + "F" + (' '*2) + "S\n"


# print(month)
# print(days_of_the_week)

# print(" "*9, end='')

# for i in range(1, 31):
#     print(f"{i:3}", end='')

#     if (i + 3) % 7 == 0:
#         print("\n")

# 1
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2
# your_list = []

# for x in range(1, 100):
#     your_list.append(x)

#     print(your_list)

# 3
# new_list = ["a", "b", "c", "d", "b", "a", "e"]
# vowels = ["a", "e", "i", "o", "u"]
# fixed_list = []

# for x in new_list:
#     if x in vowels:
#         fixed_list.append(x)

# print(fixed_list)

# 4
# a_list = [1, 5, 8, 2, 4, 8, 1, 3, 5, 9]
# b_list = []


# even_list = []
# odd_list = []


# for x in a_list:
#     if x % 2 == 0:
#         even_list.append(x)
#     else:
#         odd_list.append(x)

# b_list = odd_list + even_list

# print(b_list)

# 5

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# reverse_list = []

# for x in my_list:
#     reverse_list.insert(0, x)

# print(reverse_list)

# my_list = [1, 2, 3, 4, 1, 1]
# my_list.remove(1)

# print(my_list)
# What is printed?

# nba_teams = {
#     'LAL': 'Los Angeles Lakers',
#     'CHI': 'Chicago Bulls',
#     'GSW': 'Golden State Warriors',
#     'BOS': 'Boston Celtics',
#     'PHX': 'Phoenix Suns',
#     'HOU': 'Houston Rockets',
#     'DAL': 'Dallas Mavericks',
#     'DEN': 'Denver Nuggets'
# }


# teams = {
#     "LA": "Lakers",
#     "NYC": "Yankees",
#     "CHI": "Bulls",
#     "SAC": "kings",
#     "SAN": "Spurs"
# }


# while True:
#     print()
#     print("*"*50)
#     print(("*" * 5)+" WELCOME TO THE NBA ROSTER MACHINE " + ("*" * 5))
#     print("*"*50)
#     print()
#     print("\nCurrent Teams:")
#     for location, mascot in teams.items():
#         print(f"{location}: {mascot}")

#     print()
#     print(("*" * 3)+" IF YOU DONT BEILIEVE IN YOURSELF NOBODY ELSE WILL " + ("*" * 3))
#     print((" " * 18) + "-KOBE BRYANT")
#     print("*"*57)
#     teams_edit = input("\nWhat would you like to do next? (A)dd, (R)emove, (Q)uit: ").upper()

#     if teams_edit == 'Q':
#         print("Goodbye!")
#         break
#     elif teams_edit == 'A':

#         location = input("Enter the location of the team (please abbreviete location): ").upper()
#         mascot = input("Enter team mascot: ")
#         teams[location] = mascot
#         print(f"Added team: {location} {mascot}")
#     elif teams_edit == 'R':

#         location = input("Enter team location: ").upper()
#         if location in teams:
#             del teams[location]
#             print(f"Removed team: {location}")
#         else:
#             print(f"No team found at location: {location}")
#     else:
#         print("Invalid choice. Please choose the following A, R, or Q.")


# def times_and_log(a, b, c):
#     total = a * b + c
#     print(f"{a} times {b} + {c} is {total}")


# times_and_log(4, 3, 5)

def max_funct(numbers):
    return max(numbers)


result = max_funct([5, 8, 2, 3])

print(result)


def max_value(numbers):

    max_value = numbers[0]

    for number in numbers:

        if number > max_value:
            max_value = number

    return max_value


result = max_value([5, 8, 2, 3])

print(result)
