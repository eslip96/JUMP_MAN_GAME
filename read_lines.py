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


with open("numb_loop.txt", 'w') as num_file:
    for x in range(1, 11):
        num_file.write(f'{x}\n')


with open('numb_loop.txt', 'r') as num_files:
    print(num_files.read())
