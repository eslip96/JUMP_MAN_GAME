def checkout_time(customers, n):
    if not customers:
        return 0

    if n >= len(customers):
        return max(customers)

    registers = [0] * n

    customers.sort(reverse=True)

    for customer in customers:
        min_time_register = min(registers)
        min_time_index = registers.index(min_time_register)

        registers[min_time_index] += customer

    return max(registers)


print(checkout_time([5, 3, 4], 1))
print(checkout_time([10, 2, 3, 3], 2))
print(checkout_time([2, 3, 10], 2))
print(checkout_time([], 1))
print(checkout_time([1, 2, 3, 4], 1))
print(checkout_time([2, 2, 3, 3, 4, 4], 2))
print(checkout_time([1, 2, 3, 4, 5], 100))
