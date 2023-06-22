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

# def place_into_dict(dict, element):

def my_data_process(arr):
    
    #remove field and assoc data for the field that are not needed
    deleted = delete_fields(arr)   

    # print(deleted)
    #remove header 
    header_line_removal = deleted[0].split(',')
    
    # print(header_line_removal)

    #input header fields into a dict
    header_dict = {key: None for key in header_line_removal}
    # print(header_dict)
    header = deleted.pop(0)
    # print(deleted)
    # print(header_dict)

    # ---------------------------
        #turn multiple values belonging to one key into a list ---> use switch statement
            #aka [male:3, female:2]
        #assign the key to each newly created list of values
    # ---------------------------

    a = {}
    i = 0
    while i < len(deleted):
        #taking each element and splitting into individual strings
        line = deleted[i].split(',')
        j = 0
        #input each element into the dicitionary
        for word in line:
            if word in a:
                a[word] += 1
            else:
                a[word] = 1
        # break
        i += 1
    
    # D = dict(zip(header_line_removal, a))
    print("\n")
    print(a)

my_data_transform = ['Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At', 'Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon', 'Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon', 'Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon', 'Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning', 'Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon']
result = my_data_process(my_data_transform)
# print(result)