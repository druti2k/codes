#write a program to display a person's name, age and address in three different lines.
# name=input("enter a name:")
# age=int(input('enter a age:'))
# address=input('enter a address')
# print(name)
# print(age)
# print(address)

#write a program to swap two variables.
# a,b=2,4
# a,b=4,2
# print(a)
#write a program to conver a float into int.
# g=2.33
# g=int(g)
# print(g)
#write a program to take details from a student for id card and print it into different line.
# print("Student ID card")
# student_name=input("enter your name:")
# roll_no=input("enter your roll_no")
# print(student_name)
# print(roll_no)
# ###-------------------->>>>>List<<<<<<<-----------------------------------####
# prac_list=["ram","shiva","shyam"]
# # x=["krishna","brhama"]
# # prac_list.append("Lord")
# # prac_list.count("Lord")
# print(prac_list.index("ram"))

# prac_list.extend(x)
# prac_list.sort()


##while loop in list:

# i=0
# while i<(len(prac_list)):
#     print(prac_list[i])
#short hand in list:
# [print(i) for i in prac_list]

#for loop in list:

# for i in prac_list:
#     print(i)
# # print(len(prac_list))
# print(prac_list)
# print(prac_list[0])


# a=(1,34,"RAMM")

# # for i in ll:
# #     print(i)
# print(type(a))


#list comprehension:
# L1=[1,3,4,5]
# L2=[]
# for i in L1:
#     L2.append(i)
#     print(L1,"\n",L2)
#     L3=[i for i in L1 if i>45]
#     print(L3)

###------------------------------->>>>>>>>>>>>Tupels<<<<<<<<<<<<-------------------------###

# tup= 1233,33,44,53,5,66 ###we can use ()also
# print(type(tup))
# # slicing 
# print(tup[1::3])
# print(tup[::3])
# print(tup[0:3])
# print(tup[1:])
# print(tup[:4])
#Iteration
#for loop
# for i in tup:
#     print(i)
#while loop
# i=0
# while i<len(tup):
#     print(tup[i])
#     i+=1


##Function
# print(tup.count(53))
# print(tup.index(53))



###------------------------------------->>>>>>>>>>>>Dictionaries<<<<<<<<<<<<<----------------------------------------
# employee_data={"name":"Subham","age":24,"sex":'male'}
# print(employee_data)

#Iteration#
# for x in employee_data:
#     print(x)
##Print all the value nammes one by one.##
# for i in employee_data:
#     print(employee_data[i])
###Using value function###
# for i in employee_data.values():
#     print(i)
####using item function####
# for x,y in employee_data.items():
#     print(x,":",y)
#####Dictionary Function####
# student={"Name":"Druti","Class":"10","Roll No":9}
# print(type(student))

# x=student.get("Name")
# print(x)

# a=student.items()
# print(a)

# b=student.keys()
# print(b)

# c=student.values()
# print(c)

# d=student.copy()
# print(d)

# e=student.setdefault()
# print(e)
#####Nested Dictionaries#####
# Student={1:{"Name":"Druti","Age":24},
#            2:{"Name":"Vasu","Age":24}}
# print(Student)


####----------------------------------------->>>>>>>>>>>>>>>>SET<<<<<<<<<<<<<----------------------------------------####
# a={"Subham","Male",24}
# print(a)
#Iteration#
# for i in a:
#     print(i)

##Set functions##
# a.add("Developer")
# print(a)

# a.remove(24)
# print(a)

# a.discard("Male")
# print(a)

# b=a.copy()
# print(b)
Avengers={"Ironman","Loki","Thar"}
Avengers2={"Superman","Batman","Wonder_woman"}
Avengers3={"Hulk","Akai"}

# print(Avengers.isdisjoint(Avengers2))
# print(Avengers.issubset(Avengers2))
# print(Avengers.issuperset(Avengers2))
# Avengers.update(Avengers2)
# print(Avengers)
# Avengers.clear()
# print(Avengers)
# print(Avengers.union(Avengers3))
# print(Avengers.difference(Avengers2))
# Avengers.difference_update(Avengers2)
# print(Avengers)
# x=Avengers.intersection(Avengers3)
# print(x)
# Avengers.intersection_update(Avengers2)
# print(Avengers2)
# x=Avengers.symmetric_difference(Avengers3)
# print(x)
# Avengers.symmetric_difference_update(Avengers2)
# print(Avengers)

#####------------------------------->>>>>>>>Function<<<<<<<<<<<<-------------------------------
# def hello():
#     print("druti")
# hello()
#Using return Function
# def hello():
#     return
# print("druti")
#Parameters and Argument
# def add(x,y):
#     print(x+y)
# add(10,22)
# add(13,20)
##Arbitary argument
# def hello(*name):
#     print(name)
# hello("Ram","Shiva","Krishna")


###Recursion in python:
# def hello():
#     print("hello")
#     return hello()
# print(hello())

#statement use case:
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return(n*fact(n-1))
# print(fact(10))
##Lamda Function:
# a=lambda b:b*5
# print(a(4))

# x=lambda d,e,f:(d+e)*f
# print(x(3,4,5))
#Local and Global Variables:
# x=2
# def local_var():
#     x=3
#     return x
# print(local_var())

# e=4
# def global_var():
#     global e
#     e=5
#     return e
# print(global_var())

###--------------------->>>>>>>>>>>>>>Modules<<<<<<<<<<<<<<<<<<----------------------------###
#Some in build modules in python
# import datetime
# x=datetime.datetime.now()
# print(x)

# import random
# l=random.randint(1,10)
# print(l)

# import math
# a=min(1,2,3)
# print(a)

######-------->>>>Numpy<<<<<<-------#####
import numpy as np
a=np.array([20,12,33])
b=np.array([21,42,65])
print(a+b)
#slicing
arr=np.array([10,20,30])
print(arr[:2])
##from multipel array:
d=np.array([[11,33,23],[21,4,21]])
print(d[1,:3])


# print(type(a))
# exp=[120,222,434,555,666,777,888,999]
# total=0
# for i in range(5):
#    print("monthly :",i+1,"expense:",exp[i])
#    total=total+exp[i]
# print("total expense:",total)


#fibonace series
# a=0
# b=1
# n=int(input('enter a number: '))
# print(a)
# print(b)
# for i in range(2,n):
#     c=a+b
#     a=b
#     b=c
#     print(c)

# checking prime number or not
# n=int(input('enter a number: '))
# if n>=1:
#     print(n,"is not a prime number")
# else:
#    for i in range(2,n):
#     if n%i==0:
#         print(n,"is not a prime number")
#         break
#    else:
#     print(n,"is a prime number")



   
   




print(bool("False"))
