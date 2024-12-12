#!/usr/local/bin/python3

# Example to demonstrate ways of conversting dictionary to string and ways to print
# Lets create a dictionary named as india_state_dict
# that will have keys as states and value as Abbreviation
india_state_dict =  {'Goa': 'GA', 'Karnataka': 'KA', 'Maharashtra': 'MH', 'Chhattisgarh': 'CT'}
print("\nOriginal Dictionary -> ",india_state_dict)

#approch1 : using str() function
string_version_dict = str(india_state_dict)
print ("\nData type : ", type(string_version_dict))
print ("Result string : ", string_version_dict)

#approch2 : using json.dumps() function
import json
string_version_dict = json.dumps(india_state_dict)
print ("\nData type : ", type(string_version_dict))
print ("Result string : ", string_version_dict)


#
#Lets create a dictionary named as india_state_dict
# that will have keys as states and value as Abbreviation
india_state_dict =  {'Goa': 'GA', 'Karnataka': 'KA', 'Maharashtra': 'MH', 'Chhattisgarh': 'CT'}
print("\nDirect print of Original Dictionary -> ",india_state_dict)

# line by line print dictionry item using list comprehension
[print(key,':',value) for key, value in india_state_dict.items()]

print("\n")
# line by line print of dictionary by iterating over keys
for key in india_state_dict:
    print(key," : ",india_state_dict[key])

# print dictionry as table
print("\n{:<8} {:<15}".format('State','Abbrevation'))
for k, v in india_state_dict.items():
    print("{:<8} {:<15}".format(k, v))

    