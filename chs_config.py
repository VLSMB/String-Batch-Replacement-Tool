# _*_ coding:utf-8 _*_

def chs_config():
    
    print("\n你想要如何处理文件？")
    print("="*60+"""
0、批量处理文件
1、仅处理单个文件
"""+"="*60)
    while True:
        FileMode = input("请选择（仅限数字）：")
        #批量为0 单个为1
        if FileMode not in ("0","1"):
            print("无效输入！")
        else:
            break
    
    print("\n你所处理的文本的编码？")
    print("="*60+"""
0、ASCII
1、ANSI
2、GBK
3、Shift-JIS
4、UTF-7
5、UTF-8
6、UTF-16
7、UTF-32
"""+"="*60)
    CodeMode = input("请选择（仅限数字）：")
    #0.ASCII 1.ANSI 2.GBK 3.SJIS 4.U7 5.U8 6.U16 7.U32
    while True:
        if CodeMode not in ("0","1","2","3","4","5","6","7"):
            print("无效输入！")
        else:
            break

    print("\n你想要使用什么模式搜索字符串？")
    print("="*60+"""
0、纯文本
1、文本+转义序列
2、正则表达式
"""+"="*60)
    while True:
        SearchMode = input("请选择（仅限数字）：")
        #0纯文本 1转义序列 2正则表达式
        if SearchMode not in ("0","1","2"):
            print("无效输入！")
        else:
            break

    print("\n你想要对搜索到的字符串做什么？")
    print("="*60+"""
0、替换为其他字符串
1、将其他字符串插入到已搜索字符串之前
2、将其他字符串插入到已搜索字符串之后
"""+"="*60)
    while True:
        StrMode = input("请选择（仅限数字）：")
        #0替换 1前插 2后插
        if StrMode not in ("0","1","2"):
            print("无效输入！")
        else:
            break

    
    while True:
        Count = input("\n请输入操作次数：")
        try:
            if int(Count) <= 0:
                print("无效输入！")
            else:
                break
        except ValueError:
            print("无效输入！")
    #操作过程
    strdict = {} #键为查找的字符串，值为替换的字符串
    for time in range(int(Count)):
        print("="*20+"第{}次操作".format(time+1)+"="*20)
        if SearchMode == "0":
            findstr = input("请输入要查找的字符串：")
        elif SearchMode == "1":
            findstr = input("请输入要查找的字符串以及合法的转义序列：")
        elif SearchMode == "2":
            findstr = input("请输入合法的正则表达式：")
        if StrMode == "0":
            replacestr = input("请输入替换后的字符串：")
        else:
            replacestr = input("请输入要插入的字符串：")
        strdict[findstr] = replacestr

    print("\n你想要如何保存处理结果？")
    print("="*60+"""
0、直接修改源文件
1、保存为副本
"""+"="*60)
    while True:
        SaveMode = input("请选择（仅限数字）：")
        #0替换 1副本
        if SaveMode not in ("0","1"):
            print("无效输入！")
        else:
            break
    #返回值
    returnlist = [FileMode,CodeMode,SearchMode,StrMode,Count,strdict,SaveMode]
    return returnlist

