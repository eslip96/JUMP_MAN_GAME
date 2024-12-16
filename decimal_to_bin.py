def dec_to_bin(dec_num):
    binary = ""

    for i in range(8):
        binary = str(dec_num % 2) + binary
        dec_num //= 2

    return binary


print(dec_to_bin(25))
print(dec_to_bin(0))
print(dec_to_bin(254))
