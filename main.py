# _*_ coding:utf-8 _*_
from eng_main import eng_main
from chs_main import chs_main
import os

os.system("title String Batch Replacement Tool (Debug)")
print("Please select your launage:")
print("="*60+"""
1.简体中文
2.English
"""+"="*60)
while True:
    choice = input("Your choice:")
    if choice not in ("1","2"):
        print("Invalid input!")
    elif choice == "2":
        eng_main()
        break
    elif choice == "1":
        chs_main()
        break
    
