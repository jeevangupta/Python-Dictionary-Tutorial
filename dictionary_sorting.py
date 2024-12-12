#!/usr/local/bin/python3
#Lets create a Dictionary dict1
dict1 =  {'GA':100, 'AS':34, 'KA':150, 'MH':70}
print("\nDictionary is -> ",dict1)

# Python code to sort dictionary by value.
#method 1 - using values() method, keys() method and sorted() function.
# store values of dictionary in list object dict_val
dict_val = list(dict1.values())
# store keys of dictionary in list object dict_keys
dict_keys = list(dict1.keys())

res = {dict_keys[dict_val.index(v)]:v for v in sorted(dict_val)}
print(res)

#method 2 - using lambda and sorted() function.
res = {k:v for k,v in sorted(dict1.items(), key=lambda item: item[1])}
print(res)

#method 3 - using operator module and sorted() function
import operator
res = {k:v for k,v in sorted(dict1.items(), key = operator.itemgetter(1))}
print(res)
