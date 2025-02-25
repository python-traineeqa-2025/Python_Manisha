# # list1 = list(map(int,input("Enter the integers values")))
# #
# # new_list = []
# #
# # for num in list1:
# #     if int(num) % 2 == 0:
# #        new_list.append(int(num) ** 2)
# #
# # print(new_list)
#
# #list comperhensive
square = []
for x in range(6):
    square.append(x**2)
print(square)
#
#
# #take a list of numbers as input

num = [int(x) for x in (input("Enter the integers values").split())]


sq_num = [x**2 for x in num if x % 2 == 0]
print(sq_num)

#Take int list input check even and is even add +1 and print list

num1 = [int(x) for x in (input("Enter the integers values").split())]

list_1 =[x+1 for x in num1 if x % 2 == 0]
print(list_1)

