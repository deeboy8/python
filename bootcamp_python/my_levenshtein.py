def my_levenshtein(str1, str2):
    if len(str1) != len(str2):
        return -1
    count = 0
    for x, y in zip(str1, str2):
        if x != y:
            count += 1
    return count


#print(my_levenshtein(str1, str2))