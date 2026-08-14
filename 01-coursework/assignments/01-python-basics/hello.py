# 第一个 Python 脚本
# 运行方式：在终端里执行  python hello.py

# 1. 变量和打印
name = "TT2412"
print("你好，我是", name)

# 2. list 和循环
courses = ["高数C", "ArcGIS", "Python（正在学）"]
for c in courses:
    print("学过/正在学：", c)

# 3. 函数
def add(a, b):
    return a + b

print("3 + 4 =", add(3, 4))

# 4. dict 和条件判断
skills = {"python": 0, "gis": 70, "math": 30}
for k, v in skills.items():
    if v < 50:
        print(k, "还需要补，当前熟练度", v)
    else:
        print(k, "还行，当前熟练度", v)
