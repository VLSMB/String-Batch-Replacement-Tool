# _*_ coding:utf-8 _*_
from chs_config import chs_config
import os,sys,re

def chs_none():
    returnlist = chs_config()
    chs_start(returnlist)
#   returnlist = [FileMode,CodeMode,SearchMode,StrMode,Count,strdict,SaveMode]

def regex(ModeList,filestrs,Task,filenames):
    #正则表达式模式
    newstrlist = []
    newstrs = []
    if ModeList[3] == "0": #替换模式
        for newstr,fn in zip(filestrs,filenames):
            for key,value in Task.items():
                relist = list(set(re.findall(key,newstr)))
                for tempstr in relist:
                    newstr = newstr.replace(tempstr,value)
            newstrs.append(newstr)
            print("成功处理{}！".format(fn))
    elif ModeList[3] == "1":
        for newstr,fn in zip(filestrs,filenames):
            for key,value in Task.items():
                relist = list(set(re.findall(key,newstr)))
                for tempstr in relist:
                    newstr = newstr.replace(tempstr,value+tempstr)
            newstrs.append(newstr)
            print("成功处理{}！".format(fn))
    elif ModeList[3] == "2":
        for newstr,fn in zip(filestrs,filenames):
            for key,value in Task.items():
                relist = list(set(re.findall(key,newstr)))
                for tempstr in relist:
                    newstr = newstr.replace(tempstr,tempstr+value)
            newstrs.append(newstr)
            print("成功处理{}！".format(fn))
    else:
        print("发生未知错误！请检查配置文件是否存在问题！")
        input("请按回车键退出...")
        sys.exit()
    return newstrs
    
def chs_input():
    #寻找配置文件
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
    print("="*60)
    for confignum,configname in enumerate(configfile[2]):
        print("{}、{}".format(confignum,configname))
    print("="*60)
    while True:
        choice = input("请选择（仅限数字）：")
        try:
            int(choice)
        except ValueError:
            print("无效输入！")
            continue
        if int(choice) not in range(confignum+1):
            print("无效输入！")
            continue
        else:
            try:
                config = open(r"config\config{}.ini".format(int(choice)),encoding="utf-8")
                configtext = config.readlines()
                returnlist = []           
                #重新生成returnlist
                returnlist.extend(list(configtext[2][-5:-1])) #读取Mode值
                int(configtext[2][-5:-1])
                returnlist.append(configtext[3][-2]) #读取Count值
                int(configtext[3][-2])
                #将Task的值转换成字典
                dicttemp = configtext[4][7:][:-1].strip("{}") #提取字典，现在是字符串
                temp1 = dicttemp.split("") #将每一组键值放在列表里，这玩意是代替“,”
                temp2 = []
                for tp in temp1:
                    temp2.extend(tp.replace("'","").strip(" ").split("")) #删除“,”和“:”，这玩意是代替“:”
                temp3 = []
                for tp in temp2[:]:
                    temp3.append(tp.strip(" ")) #删除“ ”
                    #偶数索引为键，基数索引为值
                lkeys = []
                lvalues = []
                for lkey,lvalue in enumerate(temp3): #键值分开
                    if lkey % 2 == 0:
                        lkeys.append(lvalue)
                    else:
                        lvalues.append(lvalue)
                returndict = dict(zip(lkeys,lvalues)) #转换为字典
                returnlist.append(returndict) #加入到returnlist中
                returnlist.append(configtext[5][-1])
                int(configtext[5][-1])
                break
            except:
                print("配置文件损坏！请使用其他配置文件！")
    chs_start(returnlist)

    
def chs_start(ModeList):
#   modelist = [FileMode,CodeMode,SearchMode,StrMode,Count,strdict,SaveMode]
    EncodingDict = {"0":"ASCII","1":"ANSI","2":"GBK","3":"SJIS","4":"UTF-7","5":"UTF-8","6":"UTF-16","7":"UTF-32"}

    #检索文件
    if ModeList[0] == "0": #遍历文件夹内的文件名
        print("请把所需要操作的文本放在一个文件夹内，并将文件夹与本程序放在一起。")
        while True:
            FileDir = input("请输入文件夹名称（相对路径）：")
            if not os.path.exists(FileDir):
                print("指定的文件夹不存在！")
                continue
            for dirpath,dirnames,tpfilenames in os.walk(FileDir):
                pass
            try:
                if tpfilenames == []:
                    print("该文件夹内没有文件！")
                    continue
                else:
                    break
            except:
                print("输入的不是文件夹！")
                continue
        filenames = []
        for tp in tpfilenames: #将每个文件前加上目录名称
            filenames.append(FileDir.strip("\\")+"\\"+tp)
    elif ModeList[0] == "1": #获取一个文件，但仍需要放在列表里，为了和上面的代码一致
        print("请将要操作的文件与本程序放在同一个目录内。")
        filenames = []
        while True:
            filetpn = input("请输入文件名称：")
            if not os.path.exists(filetpn):
                print("该文件不存在！")
                continue
            else:
                try:
                    open(filetpn)
                except PermissionError:
                    print("该文件不存在，或程序权限不够！")
                    continue
                filenames.append(filetpn)
                break
    else:
        print("发生未知错误！请检查配置文件是否存在问题！")
        input("请按回车键退出...")
        sys.exit()

    #打开文件files并读取文件    
    while True:
        files = []
        filestrs = []
        x = 0
        try:
            for filename in filenames:
                files.append(open(filename,"r+",encoding=EncodingDict[ModeList[1]]))
            for file,filename in zip(files,filenames):
                filestrs.append(file.read())
                x += 1
        except:
            print("使用编码{}打开文件{}出错！".format(EncodingDict[ModeList[1]],filename))
            filenames.pop(x)
            files.pop(x)
            continue
        break
    #filenames filestrs一一对应

    #修改字符串，纯文本+转义序列
    Task = ModeList[5]
    newstrs = []
    if ModeList[2] == "1": #转义序列模式
        for key,value in dict(Task).items():
            Task[key] = value.replace(r"\\","\\").replace(r"\'","\'").replace(r'\"','\"').replace(r"\a","\a").replace(r"\b","\b").replace(r"\f","\f").replace(r"\n","\n").replace(r"\r","\r").replace(r"\t","\t").replace(r"\v","\v").replace(r"\o","\o")#将转义序列前多余的\删去
            if key.count("\\") != 0:
                Task[key.replace(r"\\","\\").replace(r"\'","\'").replace(r'\"','\"').replace(r"\a","\a").replace(r"\b","\b").replace(r"\f","\f").replace(r"\n","\n").replace(r"\r","\r").replace(r"\t","\t").replace(r"\v","\v").replace(r"\o","\o")] = value.replace(r"\\","\\").replace(r"\'","\'").replace(r'\"','\"').replace(r"\a","\a").replace(r"\b","\b").replace(r"\f","\f").replace(r"\n","\n").replace(r"\r","\r").replace(r"\t","\t").replace(r"\v","\v").replace(r"\o","\o")
                Task.pop(key)
        if ModeList[3] == "0": #判断修改方式 #0替换 1前插 2后插
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,value)
                print("成功处理{}！".format(fn))
                newstrs.append(newstr)
        elif ModeList[3] == "1":
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,value+key)
                print("成功处理{}！".format(fn))
                newstrs.append(newstr)
        elif ModeList[3] == "2":
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,key+value)
                print("成功处理{}！".format(fn))
                newstrs.append(newstr)
        else:
            print("发生未知错误！请检查配置文件是否存在问题！")
            input("请按回车键退出...")
            sys.exit()

    elif ModeList[2] == "0": #正常模式
        if ModeList[3] == "0": #判断修改方式 #0替换 1前插 2后插
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,value)
                print("成功处理{}！".format(fn))
                newstrs.append(newstr)
        elif ModeList[3] == "1":
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,value+key)
                print("成功处理{}！".format(fn))
                newstrs.append(newstr)
        elif ModeList[3] == "2":
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,key+value)
                print("成功处理{}！".format(fn))
                newstrs.append(newstr)
        else:
            print("发生未知错误！请检查配置文件是否存在问题！")
            input("请按回车键退出...")
            sys.exit()
    elif ModeList[2] == "2": #正则表达式模式
        try:
            newstrs = regex(ModeList,filestrs,Task,filenames)
        except:
            print("正则表达式不合法！请重新对文件进行配置！")
            input("请按回车键退出...")
            sys.exit()
    else:
        print("发生未知错误！请检查配置文件是否存在问题！")
        input("请按回车键退出...")
        sys.exit()
    #保存文件
    if ModeList[6] == "1":
        for newfile,strnew in zip(filenames,newstrs):
            tempfile = open(newfile+".copy","w+",encoding=EncodingDict[ModeList[1]])
            tempfile.write(strnew)
            tempfile.close()
            print("{}保存成功！".format(newfile+".copy"))
        input("请按回车键退出...")
        sys.exit()
    elif ModeList[6] == "0":
        for newfile,strnew in zip(filenames,newstrs):
            tempfile = open(newfile,"w+",encoding=EncodingDict[ModeList[1]])
            tempfile.write(strnew)
            tempfile.close()
            print("{}保存成功！".format(newfile))
        input("请按回车键退出...")
        sys.exit()
    else:
        print("发生未知错误！请检查配置文件是否存在问题！")
        input("请按回车键退出...")
        sys.exit()
