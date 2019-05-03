

import datetime

a=[[1,2,3,4,5,5],['a','b','c']]
for ele in a:
    print(ele)


exit(0)


a, b = 0, 1
while a < 20 :
    print("a={a} , b={b}".format(a=a, b=b))
    a, b = b, a+b


exit(0)

today = datetime.date.today()
koradia='surname'
text1 = 'mit'.format(mit=koradia)
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)
print(text1)

print(7//3)
print(7/3)
num = 4


def sum():
    print("mitesh ", 5/6)


while num > 0:
    print(num)
    num = num - 1

sum()
