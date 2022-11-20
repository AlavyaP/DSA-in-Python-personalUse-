# create a dictionary
'''
# use dict() function

# a = {key:'value',}
# my_dict = {1:'One',2:'Two',3:'Three'}
print(my_dict)
'''

# Insert/Update in a Dictionary
my_dict = {'name':'Sam','age':24,'address':'London'}
'''

my_dict['age']  = 35
print(my_dict)
'''
# Traversing a dictionary
'''
def traverseDict(dict):
    for key in dict :
        print(key,dict[key])
    
traverseDict(my_dict)
'''
# Search in dictionary
'''
def searchDict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key,value
    return('Does Not Exist')
            
print(searchDict(my_dict,24)) 
'''

# Delete method in a dictionary
# pop method
'''
my_dict.pop('name') 
print(my_dict)
'''
# for random key:value to remove
'''
my_dict.popitem()
print(my_dict)
'''

# remove the entire dictionary
'''
my_dict.clear()
print(my_dict)
'''

# delete a dictionary
'''
del my_dict['age']
print(my_dict)
'''

# copy method in dictionary
'''
my = my_dict.copy
print(my)
print(my_dict)
'''
# from keys method  
'''
new_dict = {}.fromkeys([1,2,3],0)
print(new_dict)
'''
# get method
'''
print(my_dict.get('age',69))
'''
# items method
'''
print(my_dict.items())
'''

# key method
'''
print(my_dict.keys())
'''
# set default method 
'''
print(my_dict.setdefault('age','added'))
'''


# values method 
'''
print(my_dict.values())
'''

# udpate method 
'''
new_dict = {'a':1,'b':2,'c':3}
my_dict.update(new_dict)
print(my_dict)

'''

# Dictionary Built in operators
# in operators
'''
print('age' in my_dict)
'''
# for operator
'''
for key in my_dict:
    print(key)
'''

# all method -->> it returns True or False only if Empty -->True
# any method -->> it returns True if any key is True, else False if all is False or Empty
# len method -->> length of the dictionary(total keys)
# sorted method -->> sort the dictionary with ascending key in order 