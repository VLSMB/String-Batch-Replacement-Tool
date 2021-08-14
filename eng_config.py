# _*_ coding:utf-8 _*_

def eng_config():
    
    print("\nWhat do you want to do with the file?")
    print("="*60+"""
0. Batch file
1. Single file
"""+"="*60)
    while True:
        FileMode = input("Your choice(Numbers only):")
        #Batch0 Single1
        if FileMode not in ("0","1"):
            print("Invalid input!")
        else:
            break
    
    print("\nThe encoding of the text you are dealing with?")
    print("="*60+"""
0. ASCII
1. ANSI
2. GBK
3. Shift-JIS
4. UTF-7
5. UTF-8
6. UTF-16
7. UTF-32
"""+"="*60)
    CodeMode = input("Your choice(Numbers only):")
    #0.ASCII 1.ANSI 2.GBK 3.SJIS 4.U7 5.U8 6.U16 7.U32
    while True:
        if CodeMode not in ("0","1","2","3","4","5","6","7"):
            print("Invalid input!")
        else:
            break

    print("\nWhat pattern do you want to search for the string?")
    print("="*60+"""
0. Plain Text
1. Escape Sequence
2. Regular Expression
"""+"="*60)
    while True:
        SearchMode = input("Your choice(Numbers only):")
        #0Plain Text 1Escape Sequence 2Regular Expression
        if SearchMode not in ("0","1","2"):
            print("Invalid input!")
        else:
            break

    print("\nWhat do you want to do with the searched string?")
    print("="*60+"""
0. Replace with other strings
1. Insert other strings before the searched string
2. Insert other strings behind the searched string
"""+"="*60)
    while True:
        StrMode = input("Your choice(Numbers only):")
        #0Replace 1Before 2After
        if StrMode not in ("0","1","2"):
            print("Invalid input!")
        else:
            break

    
    while True:
        Count = input("\nPlease enter the number of operations:")
        try:
            if int(Count) <= 0:
                print("Invalid input!")
            else:
                break
        except ValueError:
            print("Invalid input!")
    #Start process
    strdict = {} #The key is the search string,the value is the replacement string
    for time in range(int(Count)):
        print("="*20+"{} of {}".format(time+1,int(Count))+"="*20)
        if SearchMode == "0":
            findstr = input("Please enter the string you want to find:")
        elif SearchMode == "1":
            findstr = input("Please enter the string you want to find and valid Escape Sequences:")
        elif SearchMode == "2":
            findstr = input("Please enter a valid Regular Expression:")
        if StrMode == "0":
            replacestr = input("Please enter the replaced string:")
        else:
            replacestr = input("Please enter the string to be inserted:")
        strdict[findstr] = replacestr

    print("\nHow do you want to save the processing results?")
    print("="*60+"""
0. Directly modify the source file
1. Save as a copy
"""+"="*60)
    while True:
        SaveMode = input("Your choice(Numbers only):")
        #0Directly 1Copy
        if SaveMode not in ("0","1"):
            print("Invalid input!")
        else:
            break
    #return value
    returnlist = [FileMode,CodeMode,SearchMode,StrMode,Count,strdict,SaveMode]
    return returnlist

