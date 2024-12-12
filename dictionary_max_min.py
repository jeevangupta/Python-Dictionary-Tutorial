#!/usr/local/bin/python3
#Lets create a Dictionary dict1
dict =  {'GA':100, 'AS':34, 'KA':150, 'MH':70}
print("\nDictionary is -> ",dict)

# Python code to find key with Maximum value in Dictionary
#method1 - using keys() method, values() methods and max() funtion
# store values of dictionary in list object dict_val
dict_val = list(dict.values())
# store keys of dictionary in list object dict_keys
dict_keys = list(dict.keys())
 
print(dict_keys[dict_val.index(max(dict_val))])

#method 2 - using lambda and max() function.
res = max(dict, key= lambda x: dict[x])
print(res)


#method 3 - using operator module and max() function
import operator
res = max(dict.items(), key = operator.itemgetter(1))[0]
print(res)



#Lets create a Dictionary dict1
dict =  {'GA':100, 'AS':34, 'KA':150, 'MH':70}
print("\nDictionary is -> ",dict)

# Python code to find key with Maximum value in Dictionary
#method1 - using keys() method, values() methods and max() funtion
# store values of dictionary in list object dict_val
dict_val = list(dict.values())
# store keys of dictionary in list object dict_keys
dict_keys = list(dict.keys())

print(dict_keys[dict_val.index(min(dict_val))])

#method 2 - using lambda and min() function.
res = min(dict, key= lambda x: dict[x])
print(res)

#method 3 - using operator module and min() function
import operator
res = min(dict.items(), key = operator.itemgetter(1))[0]
print(res)