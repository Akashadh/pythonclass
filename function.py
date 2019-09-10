# # def test():
# #     print('hello')
# # test()
#
# # def user(name):
# #     return 'hello' + name
# #
# # print(user('ram'))
#
# # def add_sub(x, y):
# #     add = x + y
# #     sub = x - y
# #     return [add,sub]
# #
# #
# # result =(add_sub(40,7))
# # print(f'answer is {result[0]}')
#
# # def take_value():
# #     p = int(input('enter the principal'))
# #     t = int(input('enter the time'))
# #     r = int(input('enter the rate'))
# #
# #     return [p, t, r]
# #
# #
# # def calculate():
# #     get = take_value()
# #     x = get[0]
# #     y = get[1]
# #     z = get[2]
# #     return (x * y * z) / 100
# #
# #
# # def display():
# #     print(calculate())
# #
# #
# # display()
#
#
# # def my_rep(x):
# #     name= input('enter your name? ')
#
#
# # def my_rep(data, time):
# #     x = 1
# #     list = []
# #     while (x <= time):
# #         list.append(data)
# #         x = x + 1
# #     return list
# #
# #
# # print(my_rep('ram', 20))
#
#
# # name=inputg('enter the name')
# # a=iint()
#
# # def user(*name, **data):
# #     print(name)
# #     print(data)
# #
# #
# # user('ram', 'sita', 12, name='akash', age=20)
#
# # name, age = input('enter the name and age?').split()
# # print(name)
# # print(age)
#
#
# # function scope
#
# x = 10
#
#
# def test():
#     global x
#     x = x + 1
#     print(x)
#
#
# test()
#
#
# def name(nam, age):
#     print(nam)
#     if age > 8:
#         print(age)
#
#
# name('ram', 2)
#
# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
#
# print(fac(5))
#
# def name():
#     def user():
#         print(1)
#     return user()
# name()


#lambda function
# user = lambda x,y: x+y
# print(user(10, 12))


# def doc(any_function):
#     def test():
#         return f'{any_function.__doc__}'
#     return test
# @doc
# def user():
#     '''hello aliza'''
#     return 'user'
# print(user())
#
#
# @doc
# def name(x):
#     return x
# print(2)

#
# def name(function):
#     def check(x,y):
#         if x==0:
#             return 'not proceed'
#         return function(x,y)
#     return check
#
# @name
# def add(x,y):
#     return x+y
#
# print(add(10,10))
#
# @name
# def sub(x,y):
#     return x-y
# print(sub(0,14))


# def check(function):
#     def user(*name):
#         return function(*name)
#
#     return check
#
#
# @check
# def name():
#     return name
# a = ['ram', 'hari', 'sita']
# print(a)



# def name():
#     name1=input('enter the name ??')
#     name2=int(input('how many times do you want to print?'))
#     i=1
#     while(1<=name2):
#         print(name1)
#         i=i+1
# name()




# def life():
#     name1=int(input('enter how many number'))
#     i=1
#     x=[]
#
#     while(i<=name1):
#         name2 = input('enter name in list')
#         x.append(name2)
#         i+= 1
#         for name in x:
#             print(name)
# life()



#calculator

# def calc(function):
#     def check(x, y):
#         if x < 1:
#             print('invalid input')
#         return function(x, y)
#
#     return check
#
#
# @calc
# def add(x,y):
#     a = x + y
#     return a
#
#
# print(add.__name__)




