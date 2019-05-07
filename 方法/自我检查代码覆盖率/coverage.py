#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/7 0007   9:49
# 文件     ：coverage.py
# IDE      : PyCharm


"""
Python3下，使用pip3 install coverage，安装coverage
完成安装后，cd到test*开头的模块目录下
运行coverage3 run allTest.py   这个是运行所有test开头的模块
再次执行coverage html 执行代码覆盖率 通过html文件查看
执行后，在Chapter4目录下回生成htmlcov文件夹（代码覆盖率统计），找到里面的index.html打开
这里会详细展示代码运行情况

————————————————————————华丽的分割线——————————————————————————————
常用dos命令：
D: 去往D盘

cd.. 返回上一级目录

cd 文件名 目录切换到该文件名（子目录）下

cd \ 直接回根目录

dir 当前根目录下的文件目录

dir /s 所有目录

dir/p 目录多的时候，p用来分屏，显示完一屏后停下来

dir/w 所有文件一屏内显示，只显示文件和子目录

dir *.bat 显示所有扩展名是bat的文件,*代表任意字符。*为通配符，可代表多个字符，在分隔符前起作用

dir a* 显示所有文件名是a的文件，*代表任意字符

dir a? 显示所有文件名是以a开头，并只有2个字母，？代表任意字符。?为通配符，只能代表1个字符，在分隔符前起作用

dir /ta 显示目录的文件上次访问时间 access

dir /tc 显示目录的文件创建时间 creat

md 文件名 创建目录-make directory

rd 文件名 移除目录-remove directory 移除的目录中不能有子目录和文件，不能删除当前目录

copy con 1.txt 建立文件名为1的txt文档 建立后直接跳到文档内容，ctrl+z完成内容编辑

del 1.txt 删除文件名为1的txt文档 del仅用于文档，rd用于文件

ren 文件名 新文件名 重命名

type 1.txt 显示文件1.txt的内容 一般只适用于txt

tree 显示文件目录树，含最底层目录

echo 显示此命令后的字符

echo off 在此语句后所有运行的命令都不显示命令行本身

pause 暂停

Ctrl+C 中断操作 比如运行tree很长的时候

鼠标右键-标注 可选中文本

鼠标操作-粘贴 可粘贴文本

F7 查看之前执行的命令 MAC下的win系统，需要加Fn

help 指令帮助

cls 清除屏幕

ver 查看系统版本

date 查看日期

time 查看时间

ipconfig 查看电脑和网络地址

ipconfig /all 显示所有网络适配器的完整TCP/IP配置信息

winver 查看windows系统版本

notepad 打开记事本程序

mspaint 打开画图程序

calc 打开计算机程序

mstsc 远程桌面连接-Microsoft Terminal Server Connection

regedit 注册表编辑器

devmgmt 设备管理器程序-device management

taskmgr 任务管理器-task manager

tasklist 显示计算机进程

appwiz.cpl 添加/删除程序-application wizard

ncpa.cpl 网络连接属性-network control panel applet

firewall.cpl 防火墙

control 打开控制面板

Tab键 补全文件名
"""