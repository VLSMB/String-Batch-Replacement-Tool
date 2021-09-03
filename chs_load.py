# _*_ coding:utf-8 _*_
def chs_load():
    """查看配置文件信息。并打印"""

    import os, sys, sqlite3
    # 声明常量
    FileMode = ("批量处理文件", "仅处理单个文件")
    CodeMode = ('ASCII', 'ANSI', 'GBK', 'Shift-JIS', 'UTF-7', 'UTF-8', 'UTF-16', 'UTF-32')
    SearchMode = ("纯文本", "文本+转义序列", "正则表达式")
    StrMode = ("替换为其他字符串", "将其他字符串插入到已搜索字符串之前", "将其他字符串插入到已搜索字符串之后")
    SaveMode = ("直接修改源文件", "保存为副本")

    # 寻找配置文件 代码复制自chs_input()函数
    if not os.path.exists("config"):
        print("没有保存配置文件！")
        input("请按回车键退出...")
        sys.exit()
    for configfile in os.walk("config"):
        pass
    if configfile[2] == []:
        print("没有保存配置文件！")
        input("请按回车键退出...")
        sys.exit()
    print("你想使用哪一个配置文件？")
    print("=" * 60)
    for confignum, configname in enumerate(configfile[2]):
        print("{}、{}".format(confignum, configname))
    print("=" * 60)
    while True:
        choice = input("请选择（仅限数字）：")
        try:
            int(choice)
        except ValueError:
            print("无效输入！")
            continue
        if int(choice) not in range(confignum + 1):
            print("无效输入！")
            continue
        else:
            try:
                # 打开数据库文件
                returnlist = []
                connection = sqlite3.connect(os.path.join("config", "Config{}.db".format(int(choice))))
                cursor = connection.cursor()
                # 访问数据库
                cursor.execute("select * from config")
                temptuple = cursor.fetchone()
                # tuple(Modes, Count, "keys", "values", SaveMode)
                # 还原列表
                returnlist.extend(list(temptuple[0]))
                returnlist.append(str(temptuple[1]))
                exec("returnlist.append(dict(zip({0},{1})))".format(temptuple[2], temptuple[3]))
                returnlist.append(str(temptuple[4]))
            except:
                print("配置文件损坏！请使用其他配置文件！")
            else:
                break
            finally:
                # 关闭数据库
                cursor.close()
                connection.close()

    # 打印配置信息
    try:
        print("\n" + "="*60 + f"""\n字符串批量替换工具 配置文件 Config{confignum}.db 信息
处理文件数量：{FileMode[int(returnlist[0])]}
文本编码：{CodeMode[int(returnlist[1])]}
字符串搜索方式：{SearchMode[int(returnlist[2])]}
字符串操作方式：{StrMode[int(returnlist[3])]}
操作次数：{returnlist[4]} 次""")
        StringDict = returnlist[5]
        for key, value in StringDict.items():
            time = list(StringDict.keys()).index(key) + 1
            print(" "*10 + "="*20 + f"第{time}次操作" + "="*20)
            print(f"""要查找的字符串：{key}
要替换的字符串：{value}""")
        else:
            print(" " * 10 + "=" * 20 + "=" * len(f"第{time}次操作") + "=" * 23)
        print(f"文件保存方式：{SaveMode[int(returnlist[6])]}\n" + "="*60 + "\n")
        input("请按回车键继续...")
    except:
        print("配置文件损坏！请使用其他配置文件！")
        input("请按回车键继续...")