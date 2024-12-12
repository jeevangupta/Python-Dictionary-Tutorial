#!/usr/local/bin/python3

#
# Lets create a dictionery dict1 
# that will have keys as states and value as Abbreviation
dict1 =  {'Goa': 'GA', 'Karnataka': 'KA', 'Maharashtra': 'MH'}
print("\nOriginal Dictionary -> ",dict1)


# create a dictionery Using Subscription notation
#syntax: Dictionary_Name[New_Key_Name] = New_Key_Value
dict1['Assam'] =  'AS'
dict1['Tamil Nadu'] = 'TN'

print("\nDictionary after adding 2 items -> ",dict1)


#
#change name of key in dictionary
dict1 =  {'Goa': 'GA', 'Karnataka': 'KA', 'Maharashtra': 'MH', 'Assam': 'AS', 'Tamil Nadu': 'TN'}
print("\n\nOriginal Dictionary -> ",dict1)
#way1
dict1['Odisha'] = dict1['Tamil Nadu']
del dict1['Tamil Nadu']
print("\nDictionary after key name change -> ",dict1)

#way2
dict1['Chhattisgarh'] = dict1.pop('Maharashtra')
print("\nDictionary after key name change -> ",dict1)

#way3 change all key name at once
new_key = ['']


#
# updating value in dictionary
dict1 =  {'Goa': 'GA', 'Karnataka': 'KA', 'Assam': 'AS', 'Odisha': 'TN', 'Chhattisgarh': 'MH'}
print("\n\nOriginal Dictionary -> ",dict1)
#using update()
tmp={"Chhattisgarh":"CT"}
dict1.update(tmp)
print("\nDictionary after key value update -> ",dict1)
#OR
dict1.update(Chhattisgarh = "CT")
print("\nDictionary after key value update -> ",dict1)

# updating value in dictionary using subscription notation
dict1["Odisha"] = "OR"
print("\nDictionary after key value update -> ",dict1)


#
# delete/clean/empty a dictionary
dict1 =  {'Goa': 'GA', 'Karnataka': 'KA', 'Maharashtra': 'MH', 'Chhattisgarh': 'CT'}
print("\n\nOriginal Dictionary -> ",dict1)
#using clear method
dict2 = dict1 # dict2 is the Reference of dict1
print("\nReference Dictionary (befor)-> ",dict2)
dict1.clear()
print("Dictionary -> ",dict1)
print("Reference Dictionary (after)-> ",dict2)

#VS

dict1 =  {'Goa': 'GA', 'Karnataka': 'KA', 'Maharashtra': 'MH', 'Chhattisgarh': 'CT'}
dict2 = dict1 # dict2 is the Reference of dict1
print("\nReference Dictionary (befor)-> ",dict2)
dict1 = {}
print("Dictionary  -> ",dict1)
print("Reference Dictionary (after)-> ",dict2)


#
# delete item from dictionry based on key
dict1 =  {'Goa': 'GA', 'Karnataka': 'KA', 'Maharashtra': 'MH', 'Chhattisgarh': 'CT'}
print("\n\nOriginal Dictionary -> ",dict1)
#using pop()
dict1.pop("Maharashtra")
print("\nDictionary  -> ",dict1)
#using del()
del dict1["Chhattisgarh"]
print("\nDictionary  -> ",dict1)
