def bin_to_dec(bin_str):
    decimal = 0
    for i in range(len(bin_str)):
        bit = int(bin_str[i])
        pow = len(bin_str) - 1 - i
        dec += bit * (2 ** pow)

    return decimal


print(bin_to_dec("11111111"))
print(bin_to_dec("00011001"))
print(bin_to_dec("00000000"))
