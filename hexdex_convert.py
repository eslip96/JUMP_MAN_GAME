def hex_to_dec(hex):
    hex = hex.upper()
    hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    dec_val = 0

    for i, char in enumerate(reversed(hex)):
        if char not in hex_map:
            print("Invalid Hexidecimal")
            return
        dec_val += hex_map[char] * (16 ** i)

    return dec_val


def dec_to_hex(dec_num):
    if dec_num == 0:
        return "0"

    hex_map = "0123456789ABCDEF"
    hex = ""
    neg = dec_num < 0

    dec_num = abs(dec_num)
    while dec_num > 0:
        remain = dec_num % 16
        hex = hex_map[remain] + hex
        dec_num //= 16

    if neg:
        hex = "-" + hex

    return hex


print(hex_to_dec("1A"))
print(dec_to_hex(26))
