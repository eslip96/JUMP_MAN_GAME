
def Binary_to_Decimal():
    binary = input("Enter a binary number to convert to decimal: ")
    try:
        decimal = int(binary, 2)
        print(f"The decimal value of {binary} is {decimal}")
    except:
        print("Invalid binary number. Please try again.")


def Decimal_to_Binary():
    decimal = input("Enter a decimal number to convert to binary: ")
    try:
        decimal = int(decimal)
        binary = bin(decimal)[2:]
        print(f"The binary value of {decimal} is {binary}")
    except:
        print("Invalid decimal number. Please try again.")


def Add_bin_sum():
    bin1 = input("Enter the first binary number: ")
    bin2 = input("Enter The binary number youd to add: ")

    try:
        dec1 = int(bin1, 2)
        dec2 = int(bin2, 2)
        sum_decimal = dec1 + dec2
        result = bin(sum_decimal)[2:]
        print(f"The sum of {bin1} and {bin2} is {result}")
    except:
        print("Invalid binary number(s). Please try again.")


def Sub_bin_sum():
    bin1 = input("Enter the first binary number: ")
    bin2 = input("Enter the binary number youd like to subtract: ")

    try:
        dec1 = int(bin1, 2)
        dec2 = int(bin2, 2)
        diff_decimal = dec1 - dec2
        if diff_decimal < 0:
            print("Result is negative, which cannot be represented in unsigned binary.")
        else:
            result = bin(diff_decimal)[2:]
            print(f"The difference of {bin1} and {bin2} is {result}")
    except:
        print("Invalid binary number(s). Please try again.")


def multiply_bin_sum():
    bin1 = input("Enter the first binary number: ")
    bin2 = input("Enter the binary number youd like to multiply: ")

    try:
        dec1 = int(bin1, 2)
        dec2 = int(bin2, 2)
        product_decimal = dec1 * dec2
        result = bin(product_decimal)[2:]
        print(f"The product of {bin1} and {bin2} is {result}")
    except:
        print("Invalid binary number(s). Please try again.")


def divide_bin_sum():
    bin1 = input("Enter the first binary number: ")
    bin2 = input("Enter the binary number youd like to divide: ")

    try:
        dec1 = int(bin1, 2)
        dec2 = int(bin2, 2)
        if dec2 == 0:
            print("Error: Division by zero is undefined.")
        else:
            quotient_decimal = dec1 // dec2
            result = bin(quotient_decimal)[2:]
            print(f"The quotient of {bin1} divided by {bin2} is {result}")
    except:
        print("Invalid binary number(s). Please try again.")


while True:
    print()
    choice = input("""BINARY CALCULATER \n\n
                   (B)inary to Decimal Conversion \n
                   (D)ecimal to Binary Conversion\n
                   (A)dd two Binary Numbers\n
                   (S)ubtract two Binary Numbers\n
                   (M)ultiply two Binary Numbers\n
                   D(i)vide two Binary Numbers\n
                   (Q)uit""").upper()

    if choice == "B":
        Binary_to_Decimal()
    elif choice == "D":
        Decimal_to_Binary()
    elif choice == "A":
        Add_bin_sum()
    elif choice == "S":
        Sub_bin_sum()
    elif choice == "M":
        multiply_bin_sum()
    elif choice == "i":
        divide_bin_sum()
    elif choice == "Q":
        print("Thank you for using Binary calculater! trademark pending")
    else:
        print("Invalid Choice Try again")
