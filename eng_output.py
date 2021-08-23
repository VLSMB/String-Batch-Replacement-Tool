# _*_ coding:utf-8 _*_
from eng_config import eng_config
import datetime,os,sys,sqlite3

def eng_output():
    returnlist = eng_config()
#   returnlist = [FileMode,CodeMode,SearchMode,StrMode,Count,strdict,SaveMode]

    #Search Configs
    if not os.path.exists("config"):
        os.mkdir("config")
    for configfile in os.walk("config"):
        pass
    for confignum in range(100):
        if "Config{}.ini".format(confignum) not in configfile[2]:
            break

    #Create config.ini file
    datebase = sqlite3.connect(os.path.join("config","Config{}.db".format(confignum)))
    cursor = datebase.cursor()
    cursor.execute('create table config(Mode varchar(4)  primary key, Count int(20), KeyDict varchar(10000), ValueDict varchar(10000), SaveMode int(1))')
    sql = 'insert into config (Mode,Count,KeyDict,ValueDict,SaveMode) values(?,?,?,?,?)'
    data = ("".join(returnlist[0:4]),int(returnlist[4]),str(list(returnlist[5].keys())),str(list(returnlist[5].values())),int(returnlist[-1]))
    cursor.execute(sql,data)
    cursor.close()
    datebase.commit()
    datebase.close()
    print("Save the file Config{}.ini successfully!".format(confignum))
    input("Press Enter to exit...")
    sys.exit()
    
