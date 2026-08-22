# 5.6 循环 练习
# 任务：看完浓缩版知识点后补 TODO，运行看结果

# 1. for 循环遍历 list：把每个城市打印出来
cities = ['深圳', '威尼斯', '米兰']
for c in cities:
    print(c)      # TODO: 观察，for c 会依次取每个城市

# 2. range + 累加：计算 1+2+...+100（高斯 5050）
total = 0
for x in range(101):
    total = total + x   # TODO: range(101) 生成 0-100
print('1到100的和 =', total)

# 3. ★官方作业（必做）：利用循环依次对 list 中的每个名字打印出 Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for c in L:
    print('Hello,', c, '!')  # TODO: 用 for 循环，让输出是：
# Hello, Bart!
# Hello, Lisa!
# Hello, Adam!

# 4. while 循环：打印 1 到 10
n = 1
while n <= 10:
    print(n)
    n = n + 1  # TODO: 用 while 补全，n<=10 时打印 n 并 n+1

# 5. while 累加：100 以内奇数之和（1+3+5+...+99）
s = 0
m = 99
while m > 0:
    s = s + m
    m = m - 2
print('100 以内奇数之和 =', s)  # TODO: 用 while（m>0 时 s=s+m, m=m-2）

# 6. break：打印 1~10 然后打印 END
n = 1
while True:
    if n > 10:
        break     # TODO: 观察 break 提前退出
    print(n)
    n = n + 1
print('END')

# 7. continue：只打印奇数 1,3,5,7,9
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

# 8. ★挑战（加分项，做完全部必做后再做）：
# 求 1~100 中能被 3 整除但不能被 5 整除的所有数之和
total = 0
for y in range(1,101):
    if y % 3 == 0 and y % 5 != 0:
        total = total + y
print('1~100 中能被 3 整除但不能被 5 整除的所有数之和 =', total)
