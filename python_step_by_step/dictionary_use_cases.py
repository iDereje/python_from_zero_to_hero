#Dictionary  data type on python an its use cases
#Dictionary is a data type that is used to store a collection of data.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. and the key is unique


#all possible use cases of dictionary data type +examples
#1. Create a dictionary
#Create a dictionary of numbers
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
print(my_dictionary)

#Create a dictionary of strings
my_dictionary = {"Gad":"Gad","Reuven":"Reuven","Yossef":"Yossef"}
print(my_dictionary)

#Create a dictionary of mixed data types

my_dictionary = {1:"Gad",2:True,3:1.1}
print(my_dictionary)

#Create a dictionary of dictionaries
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
print(my_dictionary)

#2. Access dictionary items
#Access the first item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
print(my_dictionary[1])

#Access the second item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
print(my_dictionary[2])

#Access the last item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
print(my_dictionary[5])

#Access the second last item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
print(my_dictionary[4])

#Access the first item in the first dictionary
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
print(my_dictionary[1][1])

#Access the second item in the second dictionary
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
print(my_dictionary[2][2])

#3. Change dictionary items
#Change the first item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
my_dictionary[1] = 10
print(my_dictionary)

#Change the second item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
my_dictionary[2] = 10
print(my_dictionary)

#Change the last item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
my_dictionary[5] = 10
print(my_dictionary)

#Change the second last item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
my_dictionary[4] = 10
print(my_dictionary)

#Change the first item in the first dictionary
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
my_dictionary[1][1] = 10
print(my_dictionary)

#Change the second item in the second dictionary
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
my_dictionary[2][2] = 10
print(my_dictionary)

#4. Loop through a dictionary
#Loop through a dictionary and print all keys
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
for x in my_dictionary:
    print(x)

#Loop through a dictionary and print all values
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
for x in my_dictionary:
    print(my_dictionary[x])

#Loop through a dictionary and print all keys and values
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
for x in my_dictionary:
    print(x,my_dictionary[x])

#5. Check if key exists
#Check if the key 1 exists
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
if 1 in my_dictionary:
    print("Yes, 1 is one of the keys in the dictionary")

#Check if the key 6 exists
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
if 6 in my_dictionary:
    print("Yes, 6 is one of the keys in the dictionary")
else:
    print("No, 6 is not one of the keys in the dictionary")

#6. Dictionary length
#Print the number of items in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
print(len(my_dictionary))

#7. Adding items
#Add an item to the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
my_dictionary[6] = 6
print(my_dictionary)

#8. Removing items
#Remove the first item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
my_dictionary.pop(1)
print(my_dictionary)

#Remove the second item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
my_dictionary.pop(2)
print(my_dictionary)

#Remove the last item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
my_dictionary.pop(5)
print(my_dictionary)

#Remove the second last item in the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
my_dictionary.pop(4)
print(my_dictionary)

#Remove the first item in the first dictionary
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
my_dictionary.pop(1)

#Remove the second item in the second dictionary
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
my_dictionary.pop(2)

#9. Copy a dictionary
#Copy a dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
my_dictionary_copy = my_dictionary.copy()
print(my_dictionary_copy)

#10. Nested dictionaries
#Create a nested dictionary
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
print(my_dictionary)

#Access the first item in the first dictionary
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
print(my_dictionary[1][1])

#Access the second item in the second dictionary
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
print(my_dictionary[2][2])

#Change the first item in the first dictionary
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
my_dictionary[1][1] = 10
print(my_dictionary)

#Change the second item in the second dictionary
my_dictionary = {{1:1,2:2,3:3}:{4:4,5:5,6:6},{7:7,8:8,9:9}} #ERROR
my_dictionary[2][2] = 10
print(my_dictionary)

#11. Dictionary methods
#Clear the dictionary
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
my_dictionary.clear()
print(my_dictionary)

#Get a list of the dictionary's keys
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
print(my_dictionary.keys())

#Get a list of the dictionary's values
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
print(my_dictionary.values())

#Get a list of the dictionary's items
my_dictionary = {1:1,2:2,3:3,4:4,5:5}
print(my_dictionary.items())

#12. The dict() constructor
#Create a dictionary using the dict() constructor
my_dictionary = dict({1:1,2:2,3:3,4:4,5:5})
print(my_dictionary)

#13. Dictionary comprehension
#Create a dictionary using dictionary comprehension
my_dictionary = {x:x for x in range(1,6)}
print(my_dictionary)

#14. Dictionary methods
#Get the value of the "model" key
my_dictionary = {"name":str(input("Enter your first name")),"last_name":str(input("Enter last name")),"birht_year": int(input("Enter your birth year: "))}
print(my_dictionary.get("name"))

#Get the value of the "year" key
my_dictionary = {"name":str(input("Enter your first name")),"last_name":str(input("Enter last name")),"birht_year": int(input("Enter your birth year: "))}
print(my_dictionary.get("last_name"))

#Get the value of the "year" key
my_dictionary = {"name":str(input("Enter your first name")),"last_name":str(input("Enter last name")),"birht_year": int(input("Enter your birth year: "))}
print(my_dictionary.get("birht_year"))

#15. Dictionary methods
#Change the "year" value from 2018 to 2020
my_dictionary = {"name":str(input("Enter your first name")),"last_name":str(input("Enter last name")),"birht_year": int(input("Enter your birth year: "))}
my_dictionary["birht_year"] = 2020
print(my_dictionary)

#16. Dictionary methods
#Print all key names in the dictionary, one by one
my_dictionary = {"name":str(input("Enter your first name")),"last_name":str(input("Enter last name")),"birht_year": int(input("Enter your birth year: "))}
for all_keys  in my_dictionary:
    print(all_keys)

#17. Dictionary methods
#Print all values in the dictionary, one by one
my_dictionary = {"name":str(input("Enter your first name")),"last_name":str(input("Enter last name")),"birht_year": int(input("Enter your birth year: "))}
for all_values in my_dictionary:
    print(my_dictionary[all_values])

#18. Dictionary methods
#Loop through both keys and values, by using the items() function
my_dictionary = {"name":str(input("Enter your first name")),"last_name":str(input("Enter last name")),"birht_year": int(input("Enter your birth year: "))}
for all_keys,all_values in my_dictionary.items():
    print(all_keys,all_values)

#19. Dictionary methods
#Check if the "name" key is present in the dictionary
my_dictionary = {"name":str(input("Enter your first name")),"last_name":str(input("Enter last name")),"birht_year": int(input("Enter your birth year: "))}
if "name" in my_dictionary:
    print("Yes, 'name' is one of the keys in the my_dictionary dictionary")




#20. Dictionary methods
#Check if the "name" key is present in the dictionary if not add it to the dictionary with  option for adding the value of the key
my_dictionary = {"name":str(input("Enter your first name")),"last_name":str(input("Enter last name")),"birht_year": int(input("Enter your birth year: "))}
if "name" not in my_dictionary:
    my_dictionary["name"] = " "
    print(my_dictionary)

