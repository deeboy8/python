def my_string_index(param_1, param_2):
    if param_2 in param_1:
        print(param_1.index(param_2))
        return param_1.index(param_2)
    else:
        print(-1)
        return -1
    # index = 0

    # while index < len(param_1):
    #     if param_1[index] == param_2:
    #         # print(index)
    #         return index
    #     index += 1
    
    # return (print(-1))

        index = 0

my_string_index("hello", "l")
my_string_index("aaaaa", "b")