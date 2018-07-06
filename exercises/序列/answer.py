# 练习一 字符串

# 1. 定义一个字符串Hello Python 并使用print( )输出
# 2. 定义第二个字符串Let‘s go并使用print( )输出
# 3. 定义第三个字符串"The Zen of Python" -- by Tim Peters 并使用print( )输出


a = 'Hello Python'
print(a)

b = "Let's go"
print(b)

c = '"The Zen of Python"'
print(c)


# 练习二 字符串基本操作

# 1. 定义两个字符串分别为 xyz 、abc
# 2. 对两个字符串进行连接
# 3. 取出xyz字符串的第二个和第三个元素
# 4. 对abc输出10次
# 5. 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出

abc = 'abc'
xyz = 'xyz'
print(abc + xyz)
print(xyz[1:3])
print(abc * 10)
print('a' in abc)
print('a' in xyz)


# 练习三 列表的基本操作

# 1. 定义一个含有5个数字的列表
#
# 2. 为列表增加一个元素 100
#
# 3. 使用remove()删除一个元素后观察列表的变化
#
# 4. 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素

num_list = [1, 3, 6, 7, 10]
print(num_list)
num_list.append(100)
print(num_list)
num_list.remove(3)
print(num_list)
print(num_list[0:3])
print(num_list[-1])

# 练习四 元组的基本操作

# 1. 定义一个任意元组，对元组使用append() 查看错误信息
# 2. 访问元组中的倒数第二个元素
# 3. 定义一个新的元组，和 1. 的元组连接成一个新的元组
# 4. 计算元组元素个数

tuple = (1, 2, 3, 6, 10, 915);
print(tuple)
# 元组不可变，没有append函数
# tuple.append(1);

tuple2 = (7, 9, 4);
print(tuple + tuple2)
print('tuple个数：', len(tuple))
print('tuple2个数：', len(tuple2))
print('tuple + tuple2个数：', len(tuple + tuple2))

