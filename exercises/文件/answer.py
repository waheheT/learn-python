# 练习一 文件的创建和使用
# 1. 创建一个文件，并写入当前日期
# 2. 再次打开这个文件，读取文件的前4个字符后退出

import time
file = open('hello.md','w')
file.write('1. 时间是 %s' % time.time())
file.close();


file2 = open('hello.md')
print(file2.read(4))
file2.close()

# 读取文件并打印输出
with open('answer.py', 'r') as f:
    s = f.read()
    print(s);