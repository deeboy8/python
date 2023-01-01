def my_is_sort(param_1):
    # : copies everything from param_1 to newly formed list list1
    list1 = param_1[:]
    # print(param_1)
    # print(list1)
    # sorts newly created list list1
    list1.sort()
    # print(list1)
    if list1 == param_1:
        return True
    else:
        return False


# my_is_sort([10, 4, 5, 8, 10])
# my_is_sort([10, 40, 95, 188, 910])
    