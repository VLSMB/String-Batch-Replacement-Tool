# _*_ coding:utf-8 _*_
from chs_config import chs_config
import datetime,os,sys

def chs_output():
    returnlist = chs_config()
#   returnlist = [FileMode,CodeMode,SearchMode,StrMode,Count,strdict,SaveMode]

    #查找config数量
    if not os.path.exists("config"):
        os.mkdir("config")
    for configfile in os.walk("config"):
        pass
    for confignum in range(100):
        if "Config{}.ini".format(confignum) not in configfile[2]:
            break

    #创建config.ini文件
    newconfig = open(r"config\Config{}.ini".format(confignum),"w+",encoding="utf-8")
    now = datetime.datetime.now()
    keys = []
    values = []
    for key,value in returnlist[5].items():
        keys.append(key.replace(",","").replace(":",""))
        values.append(value.replace(",","").replace(":",""))# 代替元素中的,         代替元素中的:
    newdict = dict(zip(keys,values))
    newstrtemp = str(newdict).replace(",","").replace(":","")
    newstr = newstrtemp.replace(r"\ue058",",").replace(r"\ue05c",":")
    newconfig.write("""[String Batch Replacement Tool Config]{0}

Modes = {1}
Count = {2}
Task = {3}
SaveMode = {4}""".format(now.strftime("%Y-%m-%d %H:%M:%S"),returnlist[0]+returnlist[1]+returnlist[2]+returnlist[3],
                         returnlist[4],newstr,
                         returnlist[6]))
    newconfig.close()
    print("保存文件Config{}.ini成功！".format(confignum))
    input("请按回车键退出...")
    sys.exit()
    
