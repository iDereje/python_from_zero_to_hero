#set  data type on python an its use cases
#Set is a data type that is used to store a collection of data.
#Set is a collection which is unordered and unindexed. No duplicate members.

#all possible use cases of set data type +examples

#1. Create a set
#Create a set of numbers
my_set = {1,2,3,4,5}
print(my_set)

#Create a set of strings
my_set = {"Gad","Reuven","Yossef"}
print(my_set)

#Create a set of mixed data types
my_set = {1,"Gad",True}
print(my_set)

#Create a set of sets
my_set = {{1,2,3},{4,5,6},{7,8,9}}
print(my_set)

#2. Access set items
#Access the first item in the set ISNT POSSIBLE!!! in set data type
my_set = {1,2,3,4,5}
print(my_set[0]) #ERROR

#Access the second item in the set ISNT POSSIBLE!!! in set data type
my_set = {1,2,3,4,5}
print(my_set[1]) #ERROR

#Access the last item in the set ISNT POSSIBLE!!! in set data type
my_set = {1,2,3,4,5}
print(my_set[-1]) #ERROR

#Access the second last item in the set ISNT POSSIBLE!!! in set data type
my_set = {1,2,3,4,5}
print(my_set[-2]) #ERROR

#Access the first item in the first set ISNT POSSIBLE!!! in set data type
my_set = {{1,2,3},{4,5,6},{7,8,9}}
print(my_set[0][0]) #ERROR

#Access the second item in the second set ISNT POSSIBLE!!! in set data type
my_set = {{1,2,3},{4,5,6},{7,8,9}}
print(my_set[1][1]) #ERROR

#3. Change set items
#Change the first item in the set ISNT POSSIBLE!!! in set data type
my_set = {1,2,3,4,5}
my_set[0] = 10 #ERROR
print(my_set)

#Change the second item in the set ISNT POSSIBLE!!! in set data type
my_set = {1,2,3,4,5}
my_set[1] = 10 #ERROR
print(my_set)

#Change the last item in the set ISNT POSSIBLE!!! in set data type
my_set = {1,2,3,4,5}
my_set[-1] = 10 #ERROR
print(my_set)

#Change the second last item in the set ISNT POSSIBLE!!! in set data type
my_set = {1,2,3,4,5}
my_set[-2] = 10 #ERROR
print(my_set)

#Change the first item in the first set ISNT POSSIBLE!!! in set data type
my_set = {{1,2,3},{4,5,6},{7,8,9}}
my_set[0][0] = 10 #ERROR
print(my_set)

#Change the second item in the second set ISNT POSSIBLE!!! in set data type
my_set = {{1,2,3},{4,5,6},{7,8,9}}
my_set[1][1] = 10 #ERROR
print(my_set)

#4. Add set items
#Add an item to the set
my_set = {1,2,3,4,5}
my_set.add(6)
print(my_set)

#Add multiple items to the set
my_set = {1,2,3,4,5}
my_set.update([6,7,8])
print(my_set)

#5. Remove set items
#Remove an item in the set
my_set = {1,2,3,4,5}
my_set.remove(1)
print(my_set)

#Remove an item in the set
my_set = {1,2,3,4,5}
my_set.discard(1)
print(my_set)

#Remove an item in the set
my_set = {1,2,3,4,5}
my_set.pop()
print(my_set)

#Remove all items in the set
my_set = {1,2,3,4,5}
my_set.clear()
print(my_set)

#6. Join two sets
#Join two sets
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
set3 = set1.union(set2)
print(set3)

#7. Get the intersection of two sets
#Get the intersection of two sets
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.intersection(set2)
print(set3)

#8. Get the difference of two sets
#Get the difference of two sets
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.difference(set2)
print(set3)

#9. Check if two sets are equal
#Check if two sets are equal
set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5}
print(set1 == set2)

#10. Check if a set is a subset of another set
#Check if a set is a subset of another set
set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5,6,7,8,9,10}
print(set1.issubset(set2))


#11. Check if a set is a superset of another set (the use case is for this is to check if a set is a subset of another set but in the opposite direction   )
#Check if a set is a superset of another set
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {1,2,3,4,5}
print(set1.issuperset(set2))

#12. Check if two sets have no items in common
#Check if two sets have no items in common
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
print(set1.isdisjoint(set2))

#13. Check if a set is empty
#Check if a set is empty
set1 = {1,2,3,4,5}
print(len(set1) == 0)

#14. Get the length of a set
#Get the length of a set
set1 = {1,2,3,4,5}
print(len(set1))

#15. Delete a set
#Delete a set
set1 = {1,2,3,4,5}
del set1
print(set1) #ERROR



