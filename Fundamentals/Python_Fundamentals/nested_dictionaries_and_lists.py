# # 1. Update values in dictionaries and lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15

# students[1]["last_name"] = "Bryant"

# sports_directory["soccer"][0]= "Andres"

# z[0]["x"] = 20

# 2. Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# def iterateDictionary(students):
#     for i in range(len(students)):
#         first = students[i]["first_name"]
#         last = students[i]["last_name"]
#         print(f"first_name - {first}, last_name - {last}")

# def iterateDictionary2(students):
#     for i in range(len(students)):
#         for j,k in students[i].items():
#             print(j, "-", k)

# iterateDictionary2(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# # 3. Get Values from a List of Dictionaries
# def iterateDictionary2(key_name, some_list):
#     for i in range(len(some_list)):
#         print(some_list[i][key_name])

# iterateDictionary2("first_name", students)

# 4. Iterate through a dictionary with list values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(my_dict):
    for key in my_dict:
        print(len(my_dict[key]), key.upper())
        for i in range(len(my_dict[key])):
            print(my_dict[key][i])


printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

