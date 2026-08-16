# 5.2 字符串和编码 练习
# 任务：理解字符串拼接、转义符、raw字符串、len()

# 1. 字符串拼接（把 name 改成你自己的名字）
name = 'TT2412'
greeting = 'Hello, ' + name
print(greeting)

# 2. 长度计算
print(len(greeting))

# 3. 转义符实战
print('姓名\t年龄\t学校')   # \t 制表符
print('第一行\n第二行')      # \n 换行

# 4. raw 字符串
print(r'路径是 D:\data\projects')   # r 让反斜杠原样输出

# 5. 挑战：下面的代码会输出什么？先猜，再运行验证
s = 'a'
s = s + 'b'
s = s + 'c'
print(s)
