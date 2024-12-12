#!/usr/local/bin/python3

# Example to demonstrate ways of concatenating dictionary
# Lets create a dictionary named as smart_phone_dict
# Which contain smartphone name and its battery capacity
smart_phone_dict =  {'Samsung Galaxy F22': 5500, 'Realme X7 Max': 4000, 'Moto G10 Power': 3000, 'OnePlus 8 Pro':5000, 'Samsung Galaxy M32': 3500}
print("\nOriginal Dictionary 1 -> ",smart_phone_dict)

# Lets create another dictionary named as smart_phone_dict2
# which contain smartphone name and its battery capacity
smart_phone_dict2 =  {'iPhone 13 Pro Max': 4373, 'iPhone 12 Pro Max': 3733}
print("Original Dictionary 2 -> ",smart_phone_dict2)

# dictionry concatenation using python update() function
smart_phone_dict.update(smart_phone_dict2)
print("\nWay 1 Concatenate_dict : ",smart_phone_dict)

# dictionry concatenation using ** [double star] i.e single expression
concatenate_dict = {**smart_phone_dict, **smart_phone_dict2}
print("\nWay 2 Concatenate_dict : ",concatenate_dict)

# #dictionry concatenation using | operator
concatenate_dict = smart_phone_dict | smart_phone_dict2
print("\nWay 3 Concatenate_dict : ",concatenate_dict)