# _*_ coding:utf-8 _*_
from eng_start import eng_input
from eng_output import eng_output
from eng_start import eng_none
import os

def eng_main():
    os.system("title String Batch Replacement Tool (Debug)")
    print("What do you want to do?")
    print("="*60+"""
0. Start without Config files
1. Import Config file
2. Generate Config file
3. Help
"""+"="*60)
    while True:
        choice = input("Your choice(Numbers only):")
        if choice not in ("0","1","2","3"):
            print("Invalid input!")
        elif choice == "3":
            print("Help Document：\n"+"="*60+"""
String Batch Replacement Tool by VLSMB

This program mainly supports the following functions:
1. Batch processing of files
2. Use Regular Expressions and Escape Sequences to search for strings
3. Insert specified characters before or after the searched string
4. Support dual languages (Simplified Chinese and English)
5. For batch processing tasks to be repeated, you can use Import\Export Config file

usage:
This program is a console program, just enter the specified text according to the prompt content of the program.

This program is currently in the testing stage, pay attention to details:
https://github.com/VLSMB/String-Batch-Replacement-Tool
"""+"="*60)
        elif choice == "1":
            eng_input()
            break
        elif choice == "2":
            eng_output()
            break
        elif choice == "0":
            eng_none()
