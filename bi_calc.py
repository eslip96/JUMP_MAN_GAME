def Bin_to_dec():
    bin_str = input("Enter a binary number: ")
    decimal = 0
    for i in range(len(bin_str)):
        bit = int(bin_str[i])
        pow = len(bin_str) - 1 - i
        decimal += bit * (2 ** pow)
    print(f"{bin_str} is now {decimal}")


def Dec_to_bin():
    dec_num = int(input("Enter a decimal number: "))
    binary = ""

    if dec_num == 0:
        print("0 is 0")
        return

    while dec_num > 0:
        binary = str(dec_num % 2) + binary
        dec_num //= 2

    print(f"your {dec_num} is now {binary}")


def Add_bin():
    bin_str_1 = input("Enter the first binary number: ")
    bin_str_2 = input("Enter the second binary number: ")

    max_len = max(len(bin_str_1), len(bin_str_2))
    bin_1 = bin_str_1.zfill(max_len)
    bin_2 = bin_str_2.zfill(max_len)

    carry = 0
    end_num = ""

    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin_1[i])
        bit2 = int(bin_2[i])

        total = bit1 + bit2 + carry
        if total == 0:
            end_num = "0" + end_num
            carry = 0
        elif total == 1:
            end_num = "1" + end_num
            carry = 0
        elif total == 2:
            end_num = "0" + end_num
            carry = 1
        else:
            end_num = "1" + end_num
            carry = 1

    if carry:
        end_num = "1" + end_num

    print(f"{bin_str_1} plus {bin_str_2} is {end_num}")


def Sub_bin():
    bin_str_1 = input("Enter the first binary number: ")
    bin_str_2 = input("Enter the second binary number: ")

    max_len = max(len(bin_str_1), len(bin_str_2))
    bin_1 = bin_str_1.zfill(max_len)
    bin_2 = bin_str_2.zfill(max_len)

    borrow = 0
    end_num = ""
    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin_1[i]) - borrow
        bit2 = int(bin_2[i])

        if bit1 < bit2:
            result = str(bit1 + 2 - bit2) + end_num
            borrow = 1
        else:
            result = str(bit1 - bit2) + end_num
            borrow = 0

    if result.startswith('1'):
        print("Negative")
    else:
        print(f"{bin_str_1} minus {bin_str_2} is {result.lstrip('0') or '0'}")
    print()
    return result.lstrip('0') or "0"


def Mult_bin():
    bin_str_1 = input("Enter the first binary number: ")
    bin_str_2 = input("Enter the second binary number: ")

    result = "0"

    for i in range(len(bin_str_2) - 1, -1, -1):
        if bin_str_2[i] == "1":
            mid_bin = bin_str_1 + "0" * (len(bin_str_2) - 1 - i)

            max_len = max(len(result), len(mid_bin))
            result = result.zfill(max_len)
            mid_bin = mid_bin.zfill(max_len)

            carry = 0
            new_num = ""

            for j in range(max_len - 1, -1, -1):
                bit1 = int(result[j])
                bit2 = int(mid_bin[j])

                total = bit1 + bit2 + carry
                if total == 0:
                    new_num = "0" + new_num
                    carry = 0
                elif total == 1:
                    new_num = "1" + new_num
                    carry = 0
                elif total == 2:
                    new_num = "0" + new_num
                    carry = 1
                else:
                    new_num = "1" + new_num
                    carry = 1

            if carry:
                new_num = "1" + new_num

            end_num = new_num

    print(f"{bin_str_1} multiplied by {bin_str_2} is {end_num.lstrip('0') or '0'}")

    return result


def Div_bin():
    bin_1 = input("Enter binary dividend: ")
    bin_2 = input("Enter binary divisor: ")

    if bin_2 == "0":
        print("Error: Division by 0")
        return

    end_num = "0"
    remainder = bin_1

    while len(remainder) >= len(bin_2):
        if bin_2 <= remainder:
            temp_num = ""
            borrow = 0
            for i in range(len(remainder) - 1, -1, -1):
                bit1 = int(remainder[i]) - borrow
                bit2 = int(bin_2[i]) if i < len(bin_2) else 0

                if bit1 < bit2:
                    temp_num = str(bit1 + 2 - bit2) + temp_num
                    borrow = 1
                else:
                    temp_num = str(bit1 - bit2) + temp_num
                    borrow = 0

            remainder = temp_num[1:].lstrip('0') or "0"
            end_num = end_num + "1"
        else:
            end_num = end_num + "0"

        remainder = remainder[1:].lstrip('0') or "0"

    print(f"End Number: {end_num.lstrip('0') or '0'}, Remainder: {remainder}")


while True:
    print()
    choice = input("""BINARY CALCULATOR \n\n
                   (B)inary to Decimal Conversion \n
                   (D)ecimal to Binary Conversion\n
                   (A)dd two Binary Numbers\n
                   (S)ubtract two Binary Numbers\n
                   (M)ultiply two Binary Numbers\n
                   D(i)vide two Binary Numbers\n
                   (Q)uit\n
                   :""").upper()

    if choice == "B":
        Bin_to_dec()
    elif choice == "D":
        Dec_to_bin()
    elif choice == "A":
        Add_bin()
    elif choice == "S":
        Sub_bin()
    elif choice == "M":
        Mult_bin()
    elif choice == "I":
        Div_bin()
    elif choice == "Q":
        print("Thank you for using Binary Calculator!!!")
        break
    else:
        print("Not a Valid Choice. Try again.")
