def my_array_uniq(param_1):
    res = []
    [res.append(x) for x in param_1 if x not in res]

    return print(res)
        

# my_array_uniq([1, 3, 5, 6, 3, 5, 6, 1])