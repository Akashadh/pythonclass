# # name = input('entet the name')
# # print(f'your name is {name.title()}')
# # sum = int(input('enter 1st number'))
# # sum1= int(input('enter 2nd number'))
# # print(f' your sum is {sum+sum1}')
#
#
# name = 'akash'
# print(dir(name))
#
# user =('ram',24, 3.14) #tuple
# print(user)
#
# user1=['hari','babita+achyut'] #list
# print(user1)

# user2={'hari', 9867} #set
# print(user2)

# dic={'name': 'ram', 'is': 25} #dic
# print(dic)

# user = ['sita', 'gita']
# print('sita' in user)

# x=20
# y=30
# z=40
#
# if x>y:


# username = input('enter the username')
# password = input('enter the password')
# if username == username and password == 'admin':
#     print('welcome' + username)
# else:
#     print('error')
#
# x=input('Enter the 1st number')
# y=input('Enter the 2nd number')
# z=input('Enter the 3rd number')
# if (x>y) and (x>z):
#     print(f'largest value is {x}')
# elif (y>x) and (y>z):
#     print(f'The largest value is {y}')
# else:
#     print(f'The largest value is {z}')
#
# if x > y:
#     if x > z:
#         print(x)
#     else:
#         print(z)
# else:
#     if y > z:
#         print(y)
#     else:
#         print(z)

# a = int(input('Enter the nep marks'))
# b = int(input('Enter the math mark'))
# c = int(input('Enter the science marks'))
# d = int(input('enter the eng marks'))
# e = int(input('enter the population marks'))
# total = a+b+c+d+e
# print(f'total{total}')
#
# percentage = total/5
# if percentage >= 85 and percentage <= 100
#     print('topper')
# elif percentage >= 75 and percentage <=85
#     print('distinction')
# elif percentage >= 60 and percentage <=75
#     print('first')
# else:
#     print('fail')

print('===*******===')
dell = 50000
mac = 120000
razer = 150000
print(f'dell{dell} mac{mac} razer{razer}')
buy = (input('do you want to buy??yes / no'))
if buy == 'yes':
    quantity = int(input('enter the total quantity of dell laptop'))
    quantity1 = int(input('enter the total quantity of mac laptop'))
    quantity2 = int(input('enter the total quantity of razer laptop'))
    a = dell * quantity + mac * quantity1 + razer * quantity2
    print(f'your laptop price is {a}')

deliver = input('shipping at home or not ? yes/no')
if deliver == 'yes':
    ship = 1000
    print(f'now your shipping price is {ship}')
else:
    ship = 0
    print(f'your shipping price is {ship}')
bag = input('choose the bag option 1) norbag 2) plastic 3) giftbag')
if bag == 'norbag':
    cost = 1000
    print(f'now your bag price will be {cost}')
if bag == 'plastic':
    cost = 50
    print(f'now your bag price will be {cost} ')
    if bag == 'giftbag':
        cost = 5000
        print(f'now your bag price will be {cost} ')
else:
    cost = 0
    print('choose bag ')
venue = input('enter your home location 1)ktm 2)lalitpur 3)bhaktapur')
if venue == 'ktm':
    print('tax will be added 13%')
    tax = 0.13
    total = dell * quantity + mac * quantity1 + razer * quantity2 + ship + cost + tax
    print(f'your total bill is Rs {total}')

else:
    total = dell * quantity + mac * quantity1 + razer * quantity2 + ship + cost
    print(f'your total bill is {total}')
