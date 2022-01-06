def remove_elements(the_list):
    the_list.pop(0)
    the_list.pop(-1)
    return the_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
updated_list = remove_elements(my_list)
print(updated_list)
