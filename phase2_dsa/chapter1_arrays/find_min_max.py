def find_max(values):
    max = values[0]
    for i in range(len(values)):
        if max > values[i]:
            continue
        else:
            max, values[i] = values[i], max
    
    return max

def find_min(values):
    min = values[0]
    for i in range(len(values)):
        if min < values[i]:
            continue
        else:
            min, values[i] = values[i], min
    
    return min

values = [12, 56,89, 100, 4, 20, 69]

print('max: ', find_max(values) )
print('min: ', find_min(values) )