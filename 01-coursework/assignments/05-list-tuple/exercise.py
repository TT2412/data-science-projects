# 5.3 list 和 tuple 练习
# 任务：学完 5.3 后，把每个 TODO 补完并运行（Ctrl+S → 点三角运行）

# 1. 创建 list：存 5 个你喜欢的城市名
cities = ['深圳', '威尼斯', '巴黎', '东京', '纽约']   # TODO: 补到 5 个
print(cities)

# 2. 索引访问：打印第一个、最后一个、倒数第二个
print(cities[0])     # TODO: 打印第一个
print(cities[-1])    # TODO:打印最后一个
print(cities[-2])    # TODO: 打印倒数第二个

# 3. 修改 list：把第 2 个城市换成 '上海'，末尾追加一个，开头插入一个
cities[1] = '上海'  # TODO: 索引赋值
cities.append('广州')  # TODO: append
cities.insert(0, '北京')  # TODO: insert
print(cities)

# 4. 删除：用 pop() 删掉最后一个，打印删除后 len()
print(cities.pop())  # TODO
print(len(cities))   # TODO

# 5. 切片：打印前 3 个城市
print(cities[0:3])  # TODO

# 6. 二维 list：3x3 网格，打印中间的元素（5）
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(grid[1][1])  # TODO: print(grid[?][?])

# 7. 元组：打印第一个元素，然后注释掉下面会报错的一行
t = (1, 2, 3)
print(t[0])
# t[0] = 100   # 取消注释试试会报什么错？看完了再注释回去

# 8. 单元素元组必须加逗号
one = (5)     # 这是整数不是元组
one_t = (5,)  # 这才是元组
print(type(one), type(one_t))

# 9. 挑战：元组里有 list 会发生什么？
mixed = (1, 2, ['a', 'b'])
mixed[2][0] = 'x'   # 这行会成功吗？为什么？
print(mixed)
