# + - * /

x = 1 + 1
print(x + 1) # 結果為 3

print(True + True) # 會印出 2
print(True + False) # 會印出 1
print(True) # 會印出 True
print('abc' + '123') # 會印出 abc123
# print('abc' + 1) 會印失敗，字串無法與整數合併

welcome_message = 'Welcome back'
user_name = 'KJ'
show_message = welcome_message + ', ' + user_name
print(show_message)

# > < >= <=
print(1 > 2)
print(1 >= 1)

age = 25
is_adult = age > 18
print('Is he adult?', is_adult)

# == !=
print(1 == 1) # 會印出 True
print(1 == 3) # 會印出 False
print(1 != 1) # 會印出 False
print(1 != 2) # 會印出 True

name = '黃大同'
print(name == '黃同') # 會印出 False

# and or
print(True and True) # 會印出 True
print(True and False) # 會印出 False
print(False and False) # 會印出 False

print(True or True) # 其中一個是 True，就會印出 True
print(True or False) # 其中一個是 True，就印出 True，否則印出 False
print(False or False) # 會印出 False

# 練習
name = '黃大大'
age = 45
print(name != '黃大大' or age > 18)
# name != '黃大大' 結果為 False
# age > 45 結果為 True
# print(False or True)，會印出 True
