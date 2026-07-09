def two_sum(lst, target):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            elif sum([lst[i], lst[j]]) == target:
                return i, j
            else:
                continue
    print("No indices")


lst = [12, 56, 78, 47, 6, 23, 15, 5,6]
print(two_sum(lst, 12))