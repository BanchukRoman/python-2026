def unique_list_modify(my_list):
    i = 0
    while i < len(my_list):
        if isinstance(my_list[i], list):
            new_list = my_list[i]
            unique_list_modify(new_list)
            new_list = [value for value in new_list if value not in my_list]
            my_list[i:i+1] = new_list
        else:
            i += 1
    return my_list
list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
print(unique_list_modify(list_a))