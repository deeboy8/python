def convert_to_strings(arr):
    result = arr.split(",")
    
    return result
    

def my_data_process(arr):
    result = {}

    # remove header list (arr[0]) and send to convert_to_strings
    # returns iterable of strings
    first = arr.pop(0)
    join = convert_to_strings(first)
   
    # create nested dicts
    for item in join:
        result[item] = {}
    
    for item in arr:
        value = convert_to_strings(item)
        
        
            
             
    
    

    print(result)






my_data_transform = ['Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At', 'Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon', 'Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon', 'Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon', 'Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning', 'Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon']
result = my_data_process(my_data_transform)
# print(result)