# 练习一 条件语句的使用

# 1. 使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
# 2. 提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出

# 练习二 循环语句的使用
# 1. 使用for语句输出1-100之间的所有偶数
# 2. 使用while语句输出1-100之间能够被3整除的数字

str = 'Hello World... '
if len(str) == 10:
    print('10个')
else:
    print('不是10个')

num = int(input('请输入一个1-40之间的数字：'))
if num in range(1, 11):
    print('num在1-10间')
elif num in range(11, 21):
    print('num在11-20间')
elif num in range(21, 31):
    print('num在21-30间')
elif num in range(31, 41):
    print('num在31-40间')
else:
    print('请输入正确的数字.')


for i in range(1, 101):
    if i % 2 == 0:
        print('偶数：', i)

j = 1
while j <= 100:
    if j % 3 == 0:
        print(j);
    j += 1;
