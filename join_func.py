def list_join(it_obj, separator):
    str_list = [str(item) for item in it_obj]
    new_list = str_list[0]
    for item in str_list[1:]:
        new_list += separator + item
    return new_list


print(list_join(["Apple", "Banana", 15, 17.6, "Orange"], ','))
