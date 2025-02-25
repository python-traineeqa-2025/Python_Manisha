#Ordered and mutable
#for group similar items or just items in general


a = [1,2,3,4,1,1,1,4]

#accessing elements
# print(a[1])
# print(len(a))
#
# #adding elements to the list
# a.append(99)
# print(a)
#
# #inserting the value in the particular index
# a.insert(1,9)
# print(a)
#
# #counting occurances
# print(a.count(1))
#
# #reversing
# a.reverse()
# print(a)
#
# #sorting
b = [2,4,56,53,12,7,8,45]
# b.sort()
# print(b)

#using sorted() returning a new sorted list
d = sorted(b, reverse = True )
print(d)

#modifying elements
e = [1,2,456,4]
e[0] = 'manisha'
print(e)

#list operations
list1 = [1,2,4]
list2 = [9,0,8]
print(list1 + list2)
print(list2 * 2)

#Removing from the list
a.remove(4) #remove the occurance of the 4
print(a)

popped = a.pop() #removes and replace last element
print(popped)
print(a)

#checking membership

print(4 in a) # false since i have removed the 4 in previous steos
print(10 not in a ) #false


del a[1] #deletes the index 1 of a list
print(a)




