#!/usr/local/bin/python3

# Example to demonstrate ways of filtering dictionary
# Lets create a dictionary named as smart_phone_dict
# which contain smartphone name and its battery capacity
smart_phone_dict =  {'Samsung Galaxy F22': 5500, 'Realme X7 Max': 4000, 
                     'Moto G10 Power': 3000, 'OnePlus 8 Pro':5000, 'Samsung Galaxy M32': 3500}
print("\nOriginal Dictionary -> ",smart_phone_dict)


# filter dictionary base on Value
# get item i.e key:value from dcitionry where mAh is >= 3500
# Way 1
result = {}
for key in smart_phone_dict:
    value = smart_phone_dict[key]
    if value >= 3500:
        tmp = {key:value}
        result.update(tmp)
print("Way 1 : ",result)

# Way 2 (optimised)
result = {key:value for (key, value) in smart_phone_dict.items() if value >= 3500}
print("Way 2 : ",result)



#
# filter dictionary base on Key
# get item i.e key:value from dcitionry where smartphone name is  "OnePlus 8 Pro"
result = {key:value for (key, value) in smart_phone_dict.items() if key == "OnePlus 8 Pro"}
print("\nsmartphone name filter result : ",result)

# get item i.e key:value from dcitionry where smartphone brand name is  "Samsung"
result = {key:value for (key, value) in smart_phone_dict.items() if "Samsung" in key}
print("smartphone brand filter result : ",result)
