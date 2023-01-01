#convert single line csv file data to list of lists
def my_csv_parser(param1, param2):
    #split by new line char if present
    if '\n' in param1:
        lst = param1.split('\n')

    i = 0
    #create new empty list
    new_list = []
    while i < len(lst):
        #check if list inside list is empty or an empty string
        # only add list to new list if it is not empty
        if len(lst[i]) != 0:
            result = lst[i].split(param2)
            new_list.append(result)
        i += 1
    print(new_list)

    return new_list

#my_csv_parser("a,b,c,e\n1,2,3,4\n", ',')