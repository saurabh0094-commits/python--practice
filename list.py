""" student=["mohan", 89.9, "rohan", 40, "aman", 85]
print(student[0]) """
#1. Append a String
#Create a list of fruits: ["apple", "banana"]. Append "mango" to the list and print the final list.
""" fruits= ["apple", "banana"]
fruits.append("mango")
print(fruits) """
""" thislist=["apple","banana","cherry"]
thislist.append("orange")
print(thislist) """
#3. Append in a Loop
#Create an empty list. Append the square of numbers from 1 to 5 into it using a loop. Print the list.
""" numbers=[]
for x in range(1,6):
    numbers.append(x**2)

print(numbers) """
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in list1:
  list2.append(x)

print(list2)