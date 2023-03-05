def my_count_on_it(param_1):
    index = 0
    array_count = []

    while index < len(param_1):
        array_count.append(len(param_1[index]))
        print(array_count[index])
        index += 1

#my_count_on_it(["hello", "today", "is", "tuesday"])