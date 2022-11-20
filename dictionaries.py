# create a dictionary
'''
# use dict() function

# a = {key:'value',}
# my_dict = {1:'One',2:'Two',3:'Three'}
print(my_dict)
'''

# Insert/Update in a Dictionary
my_dict = {'name':'Sam','age':24}
'''

my_dict['age']  = 35
print(my_dict)
'''
# Traversing a dictionary

def traverseDict(dict):
    for key in dict :
        print(key,dict[key])
    
traverseDict(my_dict)