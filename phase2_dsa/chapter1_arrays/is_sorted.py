def is_sorted(lst):
    if len(lst) == 0:
        return "the list is empty"
    elif len(lst) == 1:
        return f"The list contain a single value {lst[0]}"
    list = lst.copy()
    lst.sort() 
    
    if list == lst:
        print('final')
        return True
    return False
    
lst = [12, 20, 50]
print(is_sorted(lst))