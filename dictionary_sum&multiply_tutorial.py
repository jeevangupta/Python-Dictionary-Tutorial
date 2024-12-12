#!/usr/local/bin/python3

# Example to demonstrate ways of concatenating dictionary
# Lets create a dictionary named as smart_phone_dict
# Which contain smartphone name and its battery capacity
smart_phone_dict =  {'Samsung Galaxy F22': 5500, 'Realme X7 Max': 4000, 'Moto G10 Power': 3000, 'OnePlus 8 Pro':5000, 'Samsung Galaxy M32': 3500}
print("\nOriginal Dictionary 1 -> ",smart_phone_dict)


#
# Example to demonstrate ways of summing up dictionary values
# Lets create a dictionary named as smart_phone_dict
# which contain smartphone name and its battery capacity
smart_phone_dict =  {'Samsung Galaxy F22': 5500, 'Realme X7 Max': 4000, 'Moto G10 Power': 3000, 'OnePlus 8 Pro':5000, 'Samsung Galaxy M32': 3500}
print("\nOriginal Dictionary -> ",smart_phone_dict)

# approch1 : sum()
mAh_list = []
for i in smart_phone_dict:
    mAh_list.append(smart_phone_dict[i])

mAh_sum = sum(mAh_list)
print("Approach 1 mAh_sum : ",mAh_sum)


# Approach 2 : Using For loop to iterate through values using values() funtion
mAh_sum = 0
for i in smart_phone_dict.values():
    mAh_sum = mAh_sum + i

print("Approach 2 mAh_sum : ",mAh_sum)


# Approach 3 : Using For loop to iterate through items of dictionary
mAh_sum = 0
for i in smart_phone_dict:
    mAh_sum = mAh_sum + smart_phone_dict[i]

print("Approach 3 mAh_sum : ",mAh_sum)


#
# example to demonstrate ways of multipling dictionary values
# Lets create a dictionary named as smart_phone_dict
# which contain smartphone name and its battery capacity
smart_phone_dict =  {'Samsung Galaxy F22': 5500, 'Realme X7 Max': 4000, 'Moto G10 Power': 3000, 'OnePlus 8 Pro':5000, 'Samsung Galaxy M32': 3500}
print("\nOriginal Dictionary -> ",smart_phone_dict)

# Approch1 : numpy.prod() to get the multiplications
import numpy
mAh_list = []
for i in smart_phone_dict:
    mAh_list.append(smart_phone_dict[i])

mAh_mul = numpy.prod(mAh_list)
print("Approach 1 mAh_mul : ",mAh_mul)


# Approach 2 : Using For loop to iterate through values using values() funtion
mAh_mul = 1
for i in smart_phone_dict.values():
    mAh_mul = mAh_mul * i

print("Approach 2 mAh_mul : ",mAh_mul)


# Approach 3 : Using For loop to iterate through items of dictionary
mAh_mul = 1
for i in smart_phone_dict:
    mAh_mul = mAh_mul * smart_phone_dict[i]

print("Approach 3 mAh_mul : ",mAh_mul)
