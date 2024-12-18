def bin_inverse(bin):
    flip = ''.join('1' if bit == '0' else '0' for bit in bin)

    end_num = list(flip)
    carry = 1

    for i in range(len(end_num) - 1, -1, -1):
        if end_num[i] == '0':
            end_num[i] = '1'
            carry = 0
            break
        else:
            end_num[i] = '0'

    if carry:
        end_num.insert(0, '1')

    return ''.join(end_num)


print(bin_inverse("11110100"))
print(bin_inverse("11101011"))
