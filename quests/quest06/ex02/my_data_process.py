def convert_to_strings(arr):
    result = arr.split(",")
    
    return result

def delete_fields(arr):
    lst = []

    i = j = 0
    # turn each list into a list of strings
    # delete catagories and corresponding customer entries from list to reduce down to needed information
    while i < len(arr):
        result = arr[i].split(',')
        del result[1:4]; del result[5]
        lst.append(result)
        i += 1
    

    # return list of strings into a single list of string
    new_list = []
    while j < len(lst):
        result = ','.join(lst[j])
        new_list.append(result)
        j += 1
    
    return new_list

def my_data_process(arr):
    # print(arr)
    
    # remove elements that are not needed
    deleted = delete_fields(arr)
    customer_data = {}

    # place column headers as dicts
    words = deleted[0].split(',')
    # print(words)
    for i in words:
        customer_data[i] = {}
    
    for item in deleted:

    
    print(customer_data)










my_data_transform = ['Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At', 'Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon', 'Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon', 'Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon', 'Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning', 'Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon']
result = my_data_process(my_data_transform)
# print(result)