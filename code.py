# Python code to demonstrate
# removal of dict. pair
# using pop()

# Initializing dictionary
test_dict = {"Nesla" : 22, "Nasil" : 21, "Nesrin" : 21, "Neslin" : 21}

# Printing dictionary before removal
print ("The dictionary before performing remove is : " + str(test_dict))

# Using pop() to remove a dict. pair
# removes Nesla  
removed_value = test_dict.pop('Nesla')

# Printing dictionary after removal
print ("The dictionary after remove is : " + str(test_dict))
print ("The removed key's value is : " + str(removed_value))

print ('\r')

# Using pop() to remove a dict. pair
# doesn't raise exception
# assigns 'No Key found' to removed_value
removed_value = test_dict.pop('Manjeet', 'No Key found')

# Printing dictionary after removal
print ("The dictionary after remove is : " + str(test_dict))
print ("The removed key's value is : " + str(removed_value))
