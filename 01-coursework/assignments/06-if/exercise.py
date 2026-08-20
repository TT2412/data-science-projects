# 5.4 条件判断 练习
# 任务：学完浓缩版知识点后补 TODO，运行看结果

# 1. 基础 if：分数判断（把 score 改成 55 和 90 各跑一次）
score = 83
if score >= 60:
    print('及格')
else:
    print('不及格')  # TODO: 再加一个 else，让 score < 60 时输出 '不及格'

# 2. if/elif/else：把均分 83 换算成等级
# 规则：>=90 优秀，>=80 良好，>=70 中等，>=60 及格，否则 挂科
gpa_score = 83
if gpa_score >= 90:
    print('优秀')
elif gpa_score >= 80:
    print('良好')
elif gpa_score >= 70:
    print('中等')
elif gpa_score >= 60:
    print('及格')
else:
    print('挂科')  # TODO: 补全 if / elif / else 结构，输出对应等级

# 3. 条件组合：and 和 or
age = 21
is_student = True
# 打印：是否享受学生折扣（年龄<26 且 是学生）
if age<26 and is_student:
    print('享受学生折扣')  # TODO: 用 if 和 and 判断并打印
if age<6 or age>65:
    print('满足免票条件')  # TODO: 再判断：是否满足"免票"（年龄<6 或 年龄>65）
# TODO

# 4. 挑战：判断平年闰年
# 规则：能被4整除且不能被100整除，或能被400整除 → 闰年
year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('闰年')  
else:
    print('平年')  # TODO: 用 if / and / or 实现，输出"闰年"或"平年"
# 提示：判断整除用  year % 4 == 0

# 5. 教程官方作业：BMI 计算（if/elif/else）
height = 1.75
weight = 80.5
bmi = weight / (height ** 2)
print('BMI =', bmi)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
