# -*- coding:utf-8 -*-
import requests
from getpass import getpass
import re
import csv
import os
# 输入账号密码
while True:
    username = input("学号: ")
    password = input("密码: ")
    data = {
        "username": username,
        "pwd": password
    }


# 获取数据
    print("数据加载中，请稍候")
    resp2 = requests.post("http://119.29.4.93:5000/", data=data)
    data2 = resp2.text
    if '"code":400' in data2:
        print("获取数据失败，请检查账号密码或网络")
        retry = input("是否重试：1.是，2.否")
        if(int(retry)==2):
            exit(0)
        else:
            os.system("cls")
    else:
        print("获取数据成功")
        break

# 解析数据
year = input("请输入你想要查询绩点的学年（如：2020）: ")
obj = re.compile(r""".*?time":"(?P<time>.*?)".*?className":"(?P<className>.*?)","credit":"(?P<credit>.*?)","grade":"(?P<grade>.*?)".""", re.S)
result = obj.finditer(data2)



#计算绩点的函数
def grade_Point(grade):
    if(grade == "优"):
        return 4
    if(grade == "良"):
        return 3
    if(grade == "中"):
        return 2
    if(grade == "及格"):
        return 1
    if(grade == ''):
        return ''
    return float(grade)/10-5


# 输出数据
list1 = ["开课时间：", "课程名称", "学分", "成绩"]  # 表头
sumCredit = 0
yearGradePoint = []
GradePoint = 0
f = open("data.csv", mode="w")
csvwriter = csv.writer(f)
csvwriter.writerow(list1)
time1 = []
grade_Point1 = []
credit1 = []
name1=[]
# 将解析好的数据存入数组
for it in result:
    # print("开课时间："+it.group("time"))
    # print("课程名称"+it.group("className"))
    # print("学分"+it.group("credit"))
    # print("成绩"+it.group("grade"))
    # print("绩点："+str(grade_Point(it.group("grade"))))
    # print("学习状态"+it.group("studyStatus"))
    # sumCredit += float(it.group("credit"))
    time1.append(it.group("time"))
    name1.append(it.group("className"))
    grade_Point1.append(grade_Point(it.group("grade")))
    credit1.append(float(it.group("credit")))
    dic = it.groupdict().values()
    csvwriter.writerow(dic)
f.close()
# 计算学年总学分
i=0
for index in range(len(time1)):
    if(time1[index][0:4] == year):
        sumCredit+=credit1[index]
        i+=1
#计算平均绩点
for index1 in range(len(grade_Point1)):
    if(time1[index1][0:4] == year):
        a=float(grade_Point1[index1])
        b=float(credit1[index1])
        GradePoint = GradePoint + a*b/sumCredit
# 输出
os.system("cls")
print("注：本软件计算的平均绩点非官方数据，请用户在根目录下生成的data.csv文件中检查课程成绩和数量！！！")
print("您在"+str(year)+"学年的"+str(i)+"门学科的平均绩点为"+str(GradePoint))
input()
