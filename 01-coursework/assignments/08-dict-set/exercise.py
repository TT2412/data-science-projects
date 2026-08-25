# 5.7 dict 和 set 练习
# 任务：看完浓缩版知识点后补 TODO，运行看结果

# 1. dict 创建与查找：成绩表
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])   # TODO: 观察用 key 直接查

# 2. dict 增改：key 对应的 value 会被覆盖
d['Adam'] = 67        # TODO: 新增 key
d['Bob'] = 80         # TODO: 覆盖 Bob 的成绩
print(d)

# 3. 防 KeyError：用 in 判断 + get() 给默认值
print('Thomas' in d)          # TODO: 观察 in
print(d.get('Thomas'))        # TODO: 观察 get 不报错
print(d.get('Thomas', -1))    # TODO: 观察默认值

# 4. 删除 key
d.pop('Tracy')      # TODO: 删除并返回 value
print(d)

# 5. set：去重 + 增删 + 集合运算
s = {1, 1, 2, 2, 3, 3}
print(s)            # TODO: 观察自动去重
s.add(4)
s.remove(2)
print(s)
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)      # TODO: 交集
print(s1 | s2)      # TODO: 并集

# 6. ★官方思考题（必做）：
# 把 (1, 2, 3) 作为 dict 的 key —— 成功还是报错？把结果注释写下来
d1 = {}
d1[(1, 2, 3)] = '坐标'     # ✅ 不报错：tuple 不可变，能当 key
print(d1)

# 把 (1, [2, 3]) 作为 dict 的 key —— 运行会报错：
# TypeError: unhashable type: 'list'
# 原因：tuple 虽是"不可变外壳"，但里面的 list 可变 → 哈希算不稳，不能当 key
# d2 = {}
# d2[(1, [2, 3])] = '写代码'   # 已注释：取消注释试一次会看到上面的报错

# 7. ★挑战（加分项）：
# 用 dict 统计下面这句话里每个字母出现次数（忽略空格）
sentence = 'hello world'
count = {}
for ch in sentence:
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1
print(count)