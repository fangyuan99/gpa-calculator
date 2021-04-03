# 中南林业科技大学绩点计算器
## 1.前言

之前已经在我的博客更新了一篇有关[5分制教务系统绩点计算](http://fangyuan99.gitee.io/blog/2020/10/14/%E6%95%99%E5%8A%A1%E7%B3%BB%E7%BB%9F%E7%BB%A9%E7%82%B9%E8%AE%A1%E7%AE%97/#more)的文章，最近在学习python，就想着把之前的方法更新一下，写两个python练手的小项目。这次的项目一共有两个版本：`本地版local.py（需要用校园网或者easyconnect）`、`在线版（用的是[Moonkk](https://github.com/LittleMoonkk/Csuft-Office-Helper-FE)的数据,不需要用校园网或者easyconnect）`，本地版的比较麻烦。在线版的很方便，但是不是我的网站获得的数据，所以不保证能用。

<!-- more -->

## 2.本地版

### 1.获取数据

首先连接校园网或easyconnect，登陆进校园网之后，输入课表信息的网址：[](http://jwgl.csuft.edu.cn/jsxsd/kscj/cjcx_list)

![](https://i.vgy.me/a8tev7.png)

Ctrl+A全选后，打开根目录下的`grade.xlsx`文件，粘贴。这里在粘贴的时候会出现很多空白行，尽量删除掉，如果实在懒得删除也可以选择不删。![](https://i.vgy.me/yr3lbG.png)

保存即可。

如果要按照学期或学年来计算平均绩点，只需![](https://i.vgy.me/tK1C64.png)

1.删除第一行，点击“排序和筛选”

2.选择升序

3.点击确定

4.删除不用计算的成绩

5.保存即可

### 2.计算绩点

双击根目录下的`local.py`文件，若没有python环境可以双击`local.exe`文件，如果有使用Mac的同学可以帮忙打包成app文件。

程序运行完毕后按照提示“你的绩点数据已经保存到根目录下的`gradePoint.xlsx`文件里，第一行即为绩点信息”。

## 3.在线版

双击`online.py`，或者对应的.exe文件，按照提示输出账号密码即可，不需要使用校园网或者easyconnect

## 4.下载地址

博客地址:
http://fangyuan99.gitee.io/blog/2021/04/03/5%E5%88%86%E5%88%B6%E6%95%99%E5%8A%A1%E7%B3%BB%E7%BB%9F%E7%BB%A9%E7%82%B9%E8%AE%A1%E7%AE%972

github:https://github.com/fangyuan99/gpa-calculator

gitee:https://gitee.com/fangyuan99/gpa-calculator

百度网盘:链接：  提取码：6666 
