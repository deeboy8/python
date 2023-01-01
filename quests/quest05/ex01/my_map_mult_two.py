def my_map_mult_two(param_1):
    result = []
    index = 0

    while index < len(param_1):
        element = param_1[index] * 2
        result.append(element)
        index +=1
    return result

# my_map_mult_two([1, 3, 5, 7])