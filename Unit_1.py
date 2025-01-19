# #Default values of Datatypes
# #TypeConversion

# '''a=int()
# b=bool()
# c=complex()
# d=float()
# print(a,b,c,d)
# print(type(a),type(b),type(c),type(d))
# '''

# #String to other datatypes

# '''a="10"
# b=float(a)
# c=int(a)
# d=complex(a)
# print(b,c,d)
# '''


# #Int to other datatypes

# '''a=15
# b=float(a)
# c=bool(a)
# d=complex(a)
# e=str(a)
# print(b,c,d,e)
# print(type(b),type(c),type(d),type(e))
# '''

# #Float to other datatypes

# '''a=23.75
# b=int(a)
# c=bool(a)
# d=complex(a)
# e=str(a)
# print(b,c,d,e)
# print(type(b),type(c),type(d),type(e))
# '''

# #Complex to other Datatypes

# '''a=10+5j
# b=int(a)
# c=float(a)
# d=bool(a)
# e=str(a)
# print(b,c,d,e)
# print(type(b),type(c),type(d),type(e))
# '''

# #String(Names) to other Datatypes

# '''a="aman"
# b=int(a)
# c=float(a)
# d=complex(a)
# e=bool(a)
# print(b,c,d,e)
# print(type(b),type(c),type(d),type(e))
# '''

# #Boolean to other Datatypes

# '''a=True
# b=int(a)
# c=float(a)
# d=complex(a)
# e=str(a)
# print(b,c,d,e)
# print(type(b),type(c),type(d),type(e))

# f=False
# g=int(f)
# h=float(f)
# i=complex(f)
# j=str(f)
# print(g,h,i,j)
# print(type(g),type(h),type(i),type(j))
# '''
#Conditional Statements

# age=15
# if age>18:
#     print("You are above 18")
# else:
#     print("You are below 18")

# num=int(input("Enter a number: "))
# if num>0:
#     print("Positive Number")
# elif num==0:
#     print("Zero")
# else:
#     print("Negative Number")

# num=int(input("Enter an number : "))
# if num>=0:
#     if num==0:
#         print("Zero")
#     else:
#         print("Positive")
# else:
#     print("Negative")

#match

# a=int (input("Enter a number from 1 to 5"))

# match a:
#     case 1:
#         print("You have entered 1")
#     case 2:
#         print("You have entered 2")
#     case 3:
#         print("You have entered 3")
#     case 4:
#         print("You have entered 4")
#     case 5:
#         print("You have entered 5")
    

#Loops 

#for loop

# a=int(input("Enter a number: "))
# for i in range(a):
#     print(i+1,end=",")

# a=[1,2,3,4,5]
# sum=0
# for i in a:
#     sum+=i
# print(sum)

# for letter in 'python':
#     print(letter,end=" ")

# import math
# n=int(input("Enter a limit: "))
# for i in range(1,n):
#     k=int(math.sqrt(i))
#     for j in range(2,k+1):
#         if i%j==0:
#             break
#     else:
#         print(i)

#while Loop

# a=int(input("Enter a value: "))
# i=0
# sum=0
# while i<=a:
#     sum+=i
#     i+=1
# print(sum)

# import math
# n=int(input("Enter a limit: "))
# i=1
# while i<=n:
#     k=math.sqrt(i)
#     j=2
#     while j<=k:
#         if i%j==0:
#             break
#         j+=1
#     else:
#         print(i)
#     i+=1

#Lists

# student=[1,2,3,4,5,6,7,8,9]
# print(len(student))
# print(student[0])
# print(student[0:4])
# print(student[-5:-1])
# student.append(10)
# print(student)
# student.sort(reverse=True)
# print(student)
# student.reverse()
# print(student)
# student.insert(0,0)
# print(student)
# student.pop(0)
# print(student)
# student.remove(10)
# print(student)

#Tuples

# aman=(1,2,3,4,5)
# print(aman.index(2))
# print(aman.count(5))

#Dictionaries

# aman={
#     "name":"Aman",
#     "Cgpa":"9.44",
# }
# print(aman)
# print(aman["name"])
# print(aman.keys())
# print(aman.values())
# print(aman.items())
# print(aman.get("name"))
# new_aman={"city":"vadodara",}
# aman.update(new_aman)
# print(aman)

#Sets

# aman={1,2,3,4,5,1,2,3}
# print(aman) #unique 
# aman.add(12)
# print(aman)
# aman.remove(5)
# print(aman)
# aman.pop()
# print(aman)
# aman.pop()
# print(aman)