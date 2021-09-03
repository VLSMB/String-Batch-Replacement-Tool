# _*_ coding:utf-8 _*_
def eng_load():
    """View Config file information"""

    import os, sys, sqlite3
    # 声明常量
    FileMode = ("Batch file", "Single file")
    CodeMode = ('ASCII', 'ANSI', 'GBK', 'Shift-JIS', 'UTF-7', 'UTF-8', 'UTF-16', 'UTF-32')
    SearchMode = ("Plain Text", "Escape Sequence", "Regular Expression")
    StrMode = ("Replace with other strings", "Insert other strings before the searched string", "Insert other strings behind the searched string")
    SaveMode = ("Directly modify the source file", "Save as a copy")

    # Find the config file, Copied from eng_input()
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
    print("=" * 60)
    for confignum, configname in enumerate(configfile[2]):
        print("{}、{}".format(confignum, configname))
    print("=" * 60)
    while True:
        choice = input("Your choice(Numbers only):")
        try:
            int(choice)
        except ValueError:
            print("Invalid input!")
            continue
        if int(choice) not in range(confignum + 1):
            print("Invalid input!")
            continue
        else:
            try:
                # Connect the database
                returnlist = []
                connection = sqlite3.connect(os.path.join("config", "Config{}.db".format(int(choice))))
                cursor = connection.cursor()
                # read the database
                cursor.execute("select * from config")
                temptuple = cursor.fetchone()
                # tuple(Modes, Count, "keys", "values", SaveMode)
                # make new "returnlist"
                returnlist.extend(list(temptuple[0]))
                returnlist.append(str(temptuple[1]))
                exec("returnlist.append(dict(zip({0},{1})))".format(temptuple[2], temptuple[3]))
                returnlist.append(str(temptuple[4]))
            except:
                print("The Config file is damaged! Please use another Config file!")
            else:
                break
            finally:
                # close the database
                cursor.close()
                connection.close()

    # Print Config file information
    try:
        print("\n" + "=" * 60 + f"""\nString Batch Replacement Tool Config{confignum}.db Infomation
Number of files processed: {FileMode[int(returnlist[0])]}
Coding: {CodeMode[int(returnlist[1])]}
String search mode: {SearchMode[int(returnlist[2])]}
String operation mode: {StrMode[int(returnlist[3])]}
times: {returnlist[4]}""")
        StringDict = returnlist[5]
        for key, value in StringDict.items():
            time = list(StringDict.keys()).index(key) + 1
            print(" " * 10 + "=" * 20 + f"{time} of {returnlist[4]}" + "=" * 20)
            print(f"""The string to be found: {key}
The string to be replaced: {value}""")
        else:
            print(" " * 10 + "=" * 20 + "=" * len(f"{time} of {returnlist[4]}") + "=" * 20)
        print(f"File saving mode: {SaveMode[int(returnlist[6])]}\n" + "=" * 60 + "\n")
        input("Press Enter to continue...")
    except:
        print("The Config file is damaged! Please use another Config file!")
        input("Press Enter to continue...")