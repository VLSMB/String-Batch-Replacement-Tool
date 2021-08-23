# _*_ coding:utf-8 _*_
from eng_config import eng_config
import os,sys,re,sqlite3

def eng_none():
    returnlist = eng_config()
    eng_start(returnlist)
#   returnlist = [FileMode,CodeMode,SearchMode,StrMode,Count,strdict,SaveMode]

def regex(ModeList,filestrs,Task,filenames):
    #Regular Expression
    newstrlist = []
    newstrs = []
    if ModeList[3] == "0": #Replace
        for newstr,fn in zip(filestrs,filenames):
            for key,value in Task.items():
                relist = list(set(re.findall(key,newstr)))
                for tempstr in relist:
                    newstr = newstr.replace(tempstr,value)
            newstrs.append(newstr)
            print("Successfully processed {}!".format(fn))
    elif ModeList[3] == "1":
        for newstr,fn in zip(filestrs,filenames):
            for key,value in Task.items():
                relist = list(set(re.findall(key,newstr)))
                for tempstr in relist:
                    newstr = newstr.replace(tempstr,value+tempstr)
            newstrs.append(newstr)
            print("Successfully processed {}!".format(fn))
    elif ModeList[3] == "2":
        for newstr,fn in zip(filestrs,filenames):
            for key,value in Task.items():
                relist = list(set(re.findall(key,newstr)))
                for tempstr in relist:
                    newstr = newstr.replace(tempstr,tempstr+value)
            newstrs.append(newstr)
            print("Successfully processed {}!".format(fn))
    else:
        print("An unknown error occurred! Please check the Config file!")
        input("Press Enter to exit...")
        sys.exit()
    return newstrs
    
def eng_input():
    #寻找配置文件
    if not os.path.exists("config"):
        print("No Config file!")
        input("Press Enter to exit...")
        sys.exit()
    for configfile in os.walk("config"):
        pass
    if configfile[2] == []:
        print("No Config file!")
        input("Press Enter to exit...")
        sys.exit()
    print("Which Config do you choose?")
    print("="*60)
    for confignum,configname in enumerate(configfile[2]):
        print("{}. {}".format(confignum,configname))
    print("="*60)
    while True:
        choice = input("Your choice(Numbers only):")
        try:
            int(choice)
        except ValueError:
            print("Invalid input!")
            continue
        if int(choice) not in range(confignum+1):
            print("Invalid input!")
            continue
        else:
            try:
                # Connect the database
                returnlist = []
                connection = sqlite3.connect(os.path.join("config","Config{}.db".format(int(choice))))
                cursor = connection.cursor()
                # read the database
                cursor.execute("select * from config")
                temptuple = cursor.fetchone()
                # tuple(Modes, Count, "keys", "values", SaveMode)
                # make new "returnlist"
                returnlist.extend(list(temptuple[0]))
                returnlist.append(str(temptuple[1]))
                exec("returnlist.append(dict(zip({0},{1})))".format(temptuple[2],temptuple[3]))
                returnlist.append(str(temptuple[4]))
            except:
                print("The Config file is damaged! Please use another Config file!")
            else:
                break
            finally:
                # close the database
                cursor.close()
                connection.close()

    eng_start(returnlist)

    
def eng_start(ModeList):
#   modelist = [FileMode,CodeMode,SearchMode,StrMode,Count,strdict,SaveMode]
    EncodingDict = {"0":"ASCII","1":"ANSI","2":"GBK","3":"SJIS","4":"UTF-7","5":"UTF-8","6":"UTF-16","7":"UTF-32"}

    #Retrieve files
    if ModeList[0] == "0": #Traverse the file names in the folder
        print("Please put the text in a folder, and put the folder together with this program.")
        while True:
            FileDir = input("Please enter the folder name (relative path):")
            if not os.path.exists(FileDir):
                print("The folder doesn't exist!")
                continue
            for dirpath,dirnames,tpfilenames in os.walk(FileDir):
                pass
            try:
                if tpfilenames == []:
                    print("There are no files in this folder!")
                    continue
                else:
                    break
            except:
                print("It's not a folder!")
                continue
        filenames = []
        for tp in tpfilenames: #Add the directory name before each file
            filenames.append(FileDir.strip("\\")+"\\"+tp)
    elif ModeList[0] == "1": #Get a file, but still need to be placed in the list, in order to be consistent with the above code
        print("Please put the text together with this program.")
        filenames = []
        while True:
            filetpn = input("Please enter the file name:")
            if not os.path.exists(filetpn):
                print("The file doesn't exist!")
                continue
            else:
                try:
                    open(filetpn)
                except PermissionError:
                    print("The file doesn't exist,or the program permissions are not enough!")
                    continue
                filenames.append(filetpn)
                break
    else:
        print("An unknown error occurred! Please check the Config file!")
        input("Press Enter to exit...")
        sys.exit()

    #open the files and read them   
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
            print("Error using encoding {} to open file{}!".format(EncodingDict[ModeList[1]],filename))
            filenames.pop(x)
            files.pop(x)
            continue
        break

    #Modify string, plain text + escape sequence
    Task = ModeList[5]
    newstrs = []
    if ModeList[2] == "1": #escape sequence
        for key,value in dict(Task).items():
            Task[key] = value.replace(r"\\","\\").replace(r"\'","\'").replace(r'\"','\"').replace(r"\a","\a").replace(r"\b","\b").replace(r"\f","\f").replace(r"\n","\n").replace(r"\r","\r").replace(r"\t","\t").replace(r"\v","\v").replace(r"\o","\o")#将转义序列前多余的\删去
            if key.count("\\") != 0:
                Task[key.replace(r"\\","\\").replace(r"\'","\'").replace(r'\"','\"').replace(r"\a","\a").replace(r"\b","\b").replace(r"\f","\f").replace(r"\n","\n").replace(r"\r","\r").replace(r"\t","\t").replace(r"\v","\v").replace(r"\o","\o")] = value.replace(r"\\","\\").replace(r"\'","\'").replace(r'\"','\"').replace(r"\a","\a").replace(r"\b","\b").replace(r"\f","\f").replace(r"\n","\n").replace(r"\r","\r").replace(r"\t","\t").replace(r"\v","\v").replace(r"\o","\o")
                Task.pop(key)
        if ModeList[3] == "0": #Judging the modification method #0Replace 1Before 2Behind
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,value)
                print("Successfully processed {}!".format(fn))
                newstrs.append(newstr)
        elif ModeList[3] == "1":
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,value+key)
                print("Successfully processed {}!".format(fn))
                newstrs.append(newstr)
        elif ModeList[3] == "2":
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,key+value)
                print("Successfully processed {}!".format(fn))
                newstrs.append(newstr)
        else:
            print("An unknown error occurred! Please check the Config file!")
            input("Press Enter to exit...")
            sys.exit()

    elif ModeList[2] == "0": #Normal
        if ModeList[3] == "0": #Judging the modification method #0Replace 1Before 2Behind
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,value)
                print("Successfully processed {}!".format(fn))
                newstrs.append(newstr)
        elif ModeList[3] == "1":
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,value+key)
                print("Successfully processed {}!".format(fn))
                newstrs.append(newstr)
        elif ModeList[3] == "2":
            for newstr,fn in zip(filestrs,filenames):
                for key,value in Task.items():
                    newstr = newstr.replace(key,key+value)
                print("Successfully processed {}!".format(fn))
                newstrs.append(newstr)
        else:
            print("An unknown error occurred! Please check the Config file!")
            input("Press Enter to exit...")
            sys.exit()
    elif ModeList[2] == "2": #Regular Expression
        try:
            newstrs = regex(ModeList,filestrs,Task,filenames)
        except:
            print("Regular expression is vaild! Please reconfigure the file!")
            input("Press Enter to exit...")
            sys.exit()
    else:
        print("An unknown error occurred! Please check the Config file!")
        input("Press Enter to exit...")
        sys.exit()
    #Save files
    if ModeList[6] == "1":
        for newfile,strnew in zip(filenames,newstrs):
            tempfile = open(newfile+".copy","w+",encoding=EncodingDict[ModeList[1]])
            tempfile.write(strnew)
            tempfile.close()
            print("{} successfully saved!".format(newfile+".copy"))
        input("Press Enter to exit...")
        sys.exit()
    elif ModeList[6] == "0":
        for newfile,strnew in zip(filenames,newstrs):
            tempfile = open(newfile,"w+",encoding=EncodingDict[ModeList[1]])
            tempfile.write(strnew)
            tempfile.close()
            print("{} successfully saved!".format(newfile))
        input("Press Enter to exit...")
        sys.exit()
    else:
        print("An unknown error occurred! Please check the Config file!")
        input("Press Enter to exit...")
        sys.exit()
