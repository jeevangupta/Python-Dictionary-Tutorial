#!/usr/local/bin/python3

#Lets create a dictionery dict1 
# that will have keys as states and value as Abbreviation
dict1 =  {'Goa': 'GA', 'Assam': 'AS', 'Karnataka': 'KA', 'Maharashtra': 'MH', 'Odisha': 'OR'}
print("\nState and its abbreviation Dictionary is -> ",dict1)


# Iterating over keys
print("\n States are :")
for k in dict1:
    print(k)


#Iterating over all values
print("\n Abbreviation are:")
for ab in dict1.values():
    print(ab)



#Iterating through key, value pairs
print("\n States and its Abbreviation are:")
for k,v in dict1.items():
    print(k," : ",v)

