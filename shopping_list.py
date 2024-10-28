# print("* * * SHOPPING LIST * * *")


# shopping_list = []


# def print_recipt():
#     global shopping_list

#     if not shopping_list:
#         print("No items in shopping list")
#     else:
#         print("SHOPPING LIST:")
#         for item in shopping_list:
#             print(item)


# def add_item():
#     global shopping_list

#     add_answer = input("What would you like to add?: ")

#     if add_answer:
#         shopping_list.append(add_answer)
#         print("Item Added!")
#     else:
#         print("Item must be shoppable")


# while True:

#     user_input = input("\nWhat would you like to do?\n\n(P)rint shopping list\n(A)dd item\n(C)lear shopping list\n(Q)uit\n").upper()

#     if user_input == 'P':
#         print_recipt()
#     elif user_input == 'A':
#         add_item()
#     elif user_input == 'C':
#         shopping_list.clear()
#         print("Shopping list cleared!")
#     elif user_input == 'Q':
#         with open("Shopping_list.txt", 'w') as file:
#             file.write("\n".join(shopping_list))
#         print("Exiting the program.\nYour shopping list has been saved in 'shopping_list.txt'")
#         break
#     else:
#         print("!!!Invalid Choice Try again!!!")
