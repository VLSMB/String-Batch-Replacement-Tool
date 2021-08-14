# _*_ coding:utf-8 _*_
from chs_start import chs_input
from chs_output import chs_output
from chs_start import chs_none
import os

def chs_main():
    os.system("title 字符串批量替换工具（Debug版）")
    print("您要做什么？")
    print("="*60+"""
0、不使用配置文件直接开始
1、导入配置文件
2、生成配置文件
3、帮助
"""+"="*60)
    while True:
        choice = input("请选择（仅限数字）：")
        if choice not in ("0","1","2","3"):
            print("无效输入！")
        elif choice == "3":
            print("帮助文档：\n"+"="*60+"""
字符串批量替换工具 by VLSMB

本程序主要支持以下功能：
1、批量处理文件
2、可以使用正则表达式和转义序列进行字符串的查找
3、可以对查找到的字符串前或后面插入指定字符
4、支持双语言（简体中文和英文）
5、对于要反复进行的批处理任务，可以使用导入\导出配置文件

用法：
本程序为控制台程序，按照程序的提示内容输入指定文字即可。

目前本程序处于测试阶段，详情关注：
https://github.com/VLSMB/String-Batch-Replacement-Tool
"""+"="*60)
        elif choice == "1":
            chs_input()
            break
        elif choice == "2":
            chs_output()
            break
        elif choice == "0":
            chs_none()
