# 练习一 函数
# 1. 创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和
# 2. 创建一个函数，传入n个整数，返回其中最大的数和最小的数
# 3. 创建一个函数，传入一个参数n，返回n的阶乘

def sum():
    a = input('请输入两个数字.')
    num1, *_, num2 = list(a)
    print(int(num1) + int(num2))

sum()

def getMaxAndMin(*num):
    print(max(list(num)))
    print(min(list(num)))

getMaxAndMin(10, 3, 6, 99, 4, 19)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n-1));

print(factorial(6))

from functools import reduce
i = 10
tt = reduce(lambda x, y : x*y , range(1, i + 1))
print(tt)