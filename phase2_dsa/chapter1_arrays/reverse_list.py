def reverse_list(lst):
    new_lst = []
    for i in range(len(lst) - 1, -1, -1):
        new_lst.append(lst[i])

    return new_lst

lst = [12, 56, 78, 47, 6, 23, 15, 5,6]

print(reverse_list(lst) )