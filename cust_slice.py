def slice(iter_obj, start=1, stop=None, step=1):
    main_list = list(iter_obj)
    length = len(main_list)

    if stop is None:
        stop = length if step > 0 else -1

    if start < 0:
        start += length
    if stop < 0:
        stop += length

    end_list = []

    index = start
    while (step > 0 and index < stop) or (step < 0 and index > stop):
        end_list.append(main_list[index])
        index += step

    return end_list


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[1:-2:-1])
print(slice(nums, 1, -2, -1))

output = slice(nums, 0, 9, 3)
print(output)
