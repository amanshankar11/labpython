#Functions 

# def sum(a,b):
#     return a+b
# print(sum(5,10))
# print(sum(12,24))

# def studentinfo(name,age,course):
#     print("Name: ",name)
#     print("Age: ",age)
#     print("Course: ",course)
# studentinfo("Aman",20,"Btech")

# def fact(n):
#     if(n==1):
#         return 1
#     else:
#         return n*(fact(n-1))
# print(fact(5))

# def sum(*args):
#     sum=0
#     print(type(args))
#     # print(type(kwargs))
#     for i in args:
#         sum+=i
#     return sum
# print(sum(2,3,4,5))

# def display(**kwargs):
#     print(type(kwargs))
#     for i,j in kwargs.items():
#         print(f"key={i}\nvalue={j}")
# display(roll_no=10)
# display(roll_no=20,name="Prakash")

# a=10
# def num():
#     global a
#     print(a,id(a))
#     # a+=2
#     # print(a,id(a))
# num()
# print(a,id(a))

# from functools import *
# lst=[]
# n=int(input("Enter the number for factorial: "))
# for i in range(1,n+1):
#     lst.append(i)
# result=reduce(lambda x,y:x*y,lst)
# print(result)

# def decor(fun):
#     def inner():
#         value=fun()
#         value+=2
#         return value
#     return inner
# @decor
# def num():
#     return 10
# print(num())
# result=decor(num)
# print(result())

# def mygen(x,y):
#     while x<=y:
#         yield x
#         x+=1
# g=mygen(5,10)
# lst=list(g)
# for i in lst:
#     print(i,end=" ")
# if __name__=='__main__':
#     print("This is run as a program")
# else:
    # print("This is run as a module")

#OOPS

# class University:
#     students={}
#     @staticmethod
#     def info():
#         n = int(input("Enter the number of students: "))
#         for i in range(n):
#             print(f"\nEntering details for student {i+1}:")
#             name = input("Enter the name of the student: ")
#             dept = input("Enter the department: ")
#             erp = int(input("Enter the ERP number: "))

#             students[f"student_{i+1}"] = {
#             "name": name,
#             "dept": dept,
#             "erp": erp
#          }
# print("\nStudents details:")
# print(students)

# class Test:
#     aman=100
#     def __init__(self):
#         self.a=10
#         self.b=20
#         Test.k=50
#     def m1(self):
#         self.c=30
#         self.d=40
#     @classmethod
#     def m2(Test):
#         Test.g=500
# t1=Test()
# t1.m1()
# print(t1.__dict__)

# t2=Test()
# del t1.a
# print(t1.__dict__)
# print(t1.aman)
# print(t1.k)
# print(t1.__dict__)
# print(Test.__dict__)



# t2.m1()
# t1.c=300
# print(t1.c)

# class Test:
#     a=10
#     def __init__(self):
#         print(self.a)
#         print(Test.a)
#     def m1(self):
#         print(self.a)
#         print(Test.a)
#     @classmethod #we cannot able to access with self 
#     def m2(cls):
#         print(cls.a)
#         print(Test.a)
#     @staticmethod #because cls and self are not available
#     def m3():
#         print(Test.a)
    
# t=Test()
# print(t.a)
# print(Test.a)
# t.m1()
# t.m2()
# t.m3()
# Test.m3()
# t.a=25
# print(t.a)


# class aman:
#     a=25
#     def m1(self):
#         print(self.b)
# a=aman()
# a.a=100
# print(id(a.a))
# print(id(aman.a))

# class Test:
#     a=10
#     def __init__(self):
#         self.a

# t1=Test()
# t1.a+=5
# print(t1.a)
# print(id(t1.a))
# print(Test.a)
# print(id(Test.a))
# def m3():
#     print("hELLO")
# m3()

# class Test:
#     a=10
#     def __init__(self):
#         self.b=20
#         Test.c=30
#     def m1(self):
#         self.d=40
#         Test.e=50
#     @staticmethod
#     def m3():
#         Test.a=40
# print(Test.__dict__)
# t=Test()
# print("With t",t.__dict__)
# print(t.a,t.c)
# t.m1()
# (print(t.__dict__))
# print(Test.__dict__)
# t.m3()
# print(Test.a)

# class University:
#     specialization=input("Enter the Specialization : ")
#     # def __init__(self):
#     #     self.specialization="Computer"
#     @staticmethod
#     def ss():
#         University.specialization="Data Science"
# U=University()
# U.ss()
# print(f"The changed branch is {University.specialization}")    

# class University:
#     Uni_name=input("Enter the Name of University: ")
#     student={}
#     def __init__(self):
#         self.stu_name=input("Enter the Name: ")
#         self.Enrollment=int(input("Enter the Enrollment Number: "))
#         self.phone_num=int(input("Enter the Phone Number: "))
#         # print(self.stu_name)
#         # print(self.Enrollment)
#         # print(self.phone_num)
# n=int(input("Enter the number of students: "))
# for i in range(n):
#     students=University()
#     University.student[i+1]={
#         "Student Name":students.stu_name,
#         "Enrollment Number":students.Enrollment,
#         "Phone Number":students.phone_num,
#     }

# print(University.student)
# a=110

# class Test:
#     a=111
#     def m1(self):
#         print(a)
#         print(self.a)
# t=Test()
# t.m1()
# print(a)

# class Test:
#     def setName(self,name):
#         self.name=name
#     def setMarks(self,marks):
#         self.marks=marks
#     def getName(self):
#         return self.name
#     def getMarks(self):
#         return self.marks
# n=int(input("Enter the no of student: "))
# for i in range(n):
#     name=input("Enter the name: ")
#     marks=int(input("Enter your marks: "))
#     t=Test()
#     t.setName(name)
#     t.setMarks(marks)
# for i in range(n):
#     print(t.getName())
#     print(t.getMarks())


# class Test:
#     def property(self):
#         print("cash+power+gold+land")
#     def fun(self):
#         print("Funn")
# class c(Test):
#     def fun(self):
#         super().fun()
#         print("Lots of funn")
# class d(c):
#     def fun(self):
#         super().fun()
#         print("All fun is gone")
#     def aman():
#         print("I am aman")
# t=Test()
# t.fun()
# t.aman()
# C=d()
# C.property()
# C.fun()

# class Test:
#     def __init__(self,a=None,b=None,c=None):

# class sum1:
#     def sum(self,a,b):
#         return a+b
#     def sum(self,a,b,c):
#         return a+b+c
#     def sum(self,a,b,c,d):
#         return a+b+c+d
# s=sum1()
# print(s.sum(5,3))
# In this case last function will execute


# class sum1:
#     def sum(self,*n):
#         # result=[]
#         # for i,value in enumerate(n):
#         #     result.append(value+result)
#         # return result
#         for i in range(3):
#             result=sum(n)
#             return result
# s=sum1()
# print(s.sum(4,5,6))

