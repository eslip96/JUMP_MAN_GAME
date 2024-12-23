# 2


# with open('quotes.txt', 'r') as file:

#     line = file.readline()
#     while line:
#         print(line.strip())
#         line = file.readline()


# 3

# with open('quotes.txt', 'r') as file:

#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())


# 4

# with open('quotes.txt', 'r') as file:
#     for line in file:
#         print(line.strip())


# with open("test.txt", 'w') as file:
#     file.write("Hello my name is Enoka!!!!")

# with open("test.txt", 'r') as file:
#     print(file.read())


# 1

# with open("test.txt", "w") as myfile:
#     myfile.write("Apple\n")
#     myfile.write("Banana\n")
#     myfile.write("Orange\n")
#     myfile.write("Apricot\n")
#     myfile.write("Grape\n")

# with open("test.txt", "r") as myfile:
#     print(myfile.read())


# with open("test.txt", 'a') as case:
#     case.write("Pineapple (Not cooked or on a pizza)")

# with open("test.txt", 'r') as file:
#     print(file.read())


# 2

# with open("car_brands.txt", "w") as case:
#     case.write("Honda\n")
#     case.write("Toyota\n")
#     case.write("Chevorlet\n")
#     case.write("Ford\n")
#     case.write("Volkswagon\n")
#     case.write("Tesla\n")

# with open("car_brands.txt", 'r') as file:
#     print(file.read())


# with open("car_brands.txt", "w") as new_file:
#     new_file.write("Addidas\n")
#     new_file.write("Nike\n")
#     new_file.write("Reebok\n")
#     new_file.write("New Balance\n")

# with open("car_brands.txt", 'r') as new_file:
#     print(new_file.read())


# with open("numb_loop.txt", 'w') as num_file:
#     for x in range(1, 11):
#         num_file.write(f'{x}\n')


# with open('numb_loop.txt', 'r') as num_files:
#     print(num_files.read())


def print_menu():
    print("\n(P)rint the shopping list\n(A)dd an item\n(C)lear the list\n(Q)uit")


def print_list():
    try:
        items = open("list.txt").readlines()
        if items:
            print("\nYour shopping list:") or print(*items, sep='')
        else:
            print("\nThere are 0 items in your shopping list")
    except:
        print("\nThere are 0 items in your shopping list")


def add_item():
    while (item := input("\nAdd item ('Return' to menu): ").strip()) != "":
        open("list.txt", "a").write(item + "\n"), print(f'"{item}" added')


def clear_list():
    open("list.txt", "w").close(), print("\nYour shopping list has been cleared")


try:
    open("list.txt").close()
except:
    open("list.txt", "w").close()

print("Welcome to your shopping list program!")
print(print_menu())
while (choice := input("\n" or print_menu() or "Choose: ").lower()) != "q":
    {"p": print_list, "a": add_item, "c": clear_list}.get(choice, lambda: print("\nInvalid option"))()

print("\nExiting, your shopping list is saved.")
