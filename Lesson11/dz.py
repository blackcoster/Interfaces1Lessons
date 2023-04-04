import datetime
import time
a = datetime.datetime.now()
print('y')
b =datetime.datetime.now()
print(b-a)

# def decorator(func):
#     def wrapper():
#         func()
#     return wrapper
#
# @decorator
# def basic():
#     print(1)
#
# basic()