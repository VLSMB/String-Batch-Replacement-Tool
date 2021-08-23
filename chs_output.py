# _*_ coding:utf-8 _*_
from chs_config import chs_config
import datetime,os,sys,sqlite3

def chs_output():
    returnlist = chs_config()
#   returnlist = [FileMode,CodeMode,SearchMode,StrMode,Count,strdict,SaveMode]

    #查找config数量
    if not os.path.exists("config"):
        os.mkdir("config")
    for configfile in os.walk("config"):
        pass
    for confignum in range(100):
        if "Config{}.db".format(confignum) not in configfile[2]:
            break

    #创建config.db文件
    datebase = sqlite3.connect(os.path.join("config","Config{}.db".format(confignum)))
    cursor = datebase.cursor()
    cursor.execute('create table config(Mode varchar(4)  primary key, Count int(20), KeyDict varchar(10000), ValueDict varchar(10000), SaveMode int(1))')
    sql = 'insert into config (Mode,Count,KeyDict,ValueDict,SaveMode) values(?,?,?,?,?)'
    data = ("".join(returnlist[0:4]),int(returnlist[4]),str(list(returnlist[5].keys())),str(list(returnlist[5].values())),int(returnlist[-1]))
    cursor.execute(sql,data)
    cursor.close()
    datebase.commit()
    datebase.close()
    print("保存文件Config{}.db成功！".format(confignum))
    input("请按回车键退出...")
    sys.exit()
    
