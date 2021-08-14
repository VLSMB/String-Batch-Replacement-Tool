# _*_ coding:utf-8 _*_
from eng_config import eng_config
import datetime,os,sys

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
    newconfig = open(r"config\Config{}.ini".format(confignum),"w+",encoding="utf-8")
    now = datetime.datetime.now()
    keys = []
    values = []
    for key,value in returnlist[5].items():
        keys.append(key.replace(",","").replace(":",""))
        values.append(value.replace(",","").replace(":",""))# instead of,         instead of:
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
    print("Save the file Config{}.ini successfully!".format(confignum))
    input("Press Enter to exit...")
    sys.exit()
    
