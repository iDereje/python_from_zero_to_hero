#tulip  data type on python an its use cases
#Tulip is a data type that is used to store a collection of data.
#Tulip is a collection which is ordered and unchangeable. Allows duplicate members.

#all possible use cases of tulip data type +examples

#1. Create a tulip
#Create a tulip of numbers
my_tulip = (1,2,3,4,5)
print(my_tulip)

#Create a tulip of strings
my_tulip = ("Gad","Reuven","Menashe")
print(my_tulip)

#Create a tulip of mixed data types
my_tulip = (1,"Gad",True)
print(my_tulip)

#Create a tulip of tulips
my_tulip = ((1,2,3),(4,5,6),(7,8,9))
print(my_tulip)

#2. Access tulip items
#Access the first item in the tulip
my_tulip = (1,2,3,4,5)
print(my_tulip[0])

#Access the second item in the tulip
my_tulip = (1,2,3,4,5)
print(my_tulip[1])

#Access the last item in the tulip
my_tulip = (1,2,3,4,5)
print(my_tulip[-1])

#Access the second last item in the tulip
my_tulip = (1,2,3,4,5)
print(my_tulip[-2])

#Access the first item in the first tulip
my_tulip = ((1,2,3),(4,5,6),(7,8,9))
print(my_tulip[0][0])

#Access the second item in the second tulip
my_tulip = ((1,2,3),(4,5,6),(7,8,9))
print(my_tulip[1][1])

#3. Change tulip items
#Change the first item in the tulip ISNT POSSIBLE!!! in tulip data type
my_tulip = (1,2,3,4,5)
my_tulip[0] = 10 #ERROR
print(my_tulip)


