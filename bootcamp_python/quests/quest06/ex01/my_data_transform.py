from datetime import *

'''
Pseudocode
    - turn CSV file into a list of lists using my_csv_parser.py ---> create iterable
    - identify each index with data to be manipulated
        - create a function for each 
        - email ---> 4th index 
            - remove unique identifier and '@' to hold only provider (hotmail.com)
        - age -----> 5th index
            - [1->20] - [21->40] - [41->65] - [66->99]
        - order ---> 9th index
            - [morning => 06:00am -> 11:59am] - [afternoon => 12:00pm -> 5:59pm] - [evening => 6:00pm -> 11:59pm]
            - example input: 2020-03-05 15:19:48
                - only need the hr. 
                - change format from 12 hr to 24 hrs for set times
                    if (time >= 6 and time < 12)...etc.
    - 
'''

def get_hour(time):
    hr_result = time.split(':')
    hour = hr_result[0]
    return hour

def set_coffee_order_time(time_of_day):
    time_lst = time_of_day.split()
    # get hour of order """
    hour = int(get_hour(time_lst[1]))
    # print(hour)

    if hour >= 6 and hour < 12:
        time_of_day = 'morning'
    elif hour >= 12 and hour < 18:
        time_of_day = 'afternoon'
    else:
        time_of_day = 'evening'

    return time_of_day

def get_email_provider(email):
    result = email.split('@')
    # print(result[1])
    return result[1]

def modify_age(age):  
    a = int(age) 
    if a >= 1 and a <= 20:
        age_group = '1->20'
    elif a >= 21 and a <= 40: 
        age_group = '21->40'
    elif age >= 41 and age <= 65: 
        age_group = '41->65'
    else:
        age_group = '66->99'

    return age_group

def my_csv_parser(param1):
    #split by new line char if present ---> single list 
    if '\n' in param1:
        lst = param1.split('\n')

    # create empty list and append header 
    new_list = []
    new_list.append(lst[0])
    
    i = 1
    while i < len(lst):
        # check if list is empty or an empty string
        # only add list to new_list if it is not empty
        if len(lst[i]) != 0:
            result = lst[i].split(',') #XXXXXXXXXX
            # print(result)
            # modify 'order at' data
            # print(result[3])
            modified_coffee_order = set_coffee_order_time(result[9])
            result[9] = modified_coffee_order
            # modify email data
            modified_email = get_email_provider(result[4])
            result[4] = modified_email
            # print(result)
            # modify age
            age = int(result[5])
            modified_age = modify_age(age)
            result[5] = modified_age
            # print(result)
            # append to new_list
            new_list.append(result)
            # new_list.extend(result)
            # print(new_list)
            # print('\n')
        i += 1
    # print(new_list)
    # final_result = (",".join(new_list))
    # print(type(final_result))
    # print('\n')
    # print(final_result)
    return new_list
  

def my_data_transform(param1):
    new_list = my_csv_parser(param1)

    lst = []
    lst.append(new_list[0])
    # print(lst)
    
    i = 1
    # convert list of individual strings to a single string --> .join
    # append to the end of new_list
    while i < len(new_list):
        result = ','.join(new_list[i])
        lst.append(result)
        i += 1

    print(lst)
    return lst

csv_list = "Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At\nMale,Carl,Wilderman,carl,wilderman_carl@yahoo.com,29,Seattle,Safari iPhone,2,2020-03-06 16:37:56\nMale,Marvin,Lind,marvin,marvin_lind@hotmail.com,77,Detroit,Chrome Android,2,2020-03-02 13:55:51\nFemale,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21,Las Vegas,Chrome,1,2020-03-05 17:53:05\nFemale,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,81,Seattle,Chrome,2,2020-03-04 10:33:53\nMale,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,47,Chicago,Chrome Android,1,2020-03-05 15:19:48\n"
my_data_transform(csv_list)
# time = set_coffee_order_time(result[1][9])