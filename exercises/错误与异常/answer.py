# 练习一 异常
# 1. 在Python程序中，分别使用未定义变量、访问列表不存在的索引、访问字典不存在的关键字观察系统提示的错误信息
# 2. 通过Python程序产生IndexError，并用try捕获异常处理

# print(a)

try:
    s = [1, 2, 3]
    print(s[3])
except IndexError:
    print('index error ...')

# 定义一个异常，并继承indexError
class WaheheError(IndexError):
    pass
try:
    s = [1, 2, 3]
    raise WaheheError('Hello world...')
    print(s[3])
except WaheheError as e:
    print('index error ... %s' % e)
finally:
    print('finally...')