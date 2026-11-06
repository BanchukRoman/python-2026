def list_modify(my_list):
    i = 0
    while i < len(my_list):
        if isinstance(my_list[i], list):
            new_list = my_list[i]
            list_modify(new_list)
            my_list[i:i+1] = new_list
        else:
            i += 1
    return my_list
example_list = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print(list_modify(example_list))