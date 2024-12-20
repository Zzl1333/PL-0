import Lexical_Analysis as b
import Grammar_Analysis as d
import time

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    global line
    line = ""
    """print("是否直接调用PL\0编译器输入文档中保存的输入字符，不选择则需手动输入")
    message = input("请输入 yes or no :")"""
    """while message != "yes" and message != "no":
        message = input("输入错误，请重新输入:\n")
        time.sleep(3)
    if message ==  "yes":
        f = open('PL0_write.txt','r',encoding = 'UTF-8')
        line = f.read()
    elif message == "no" :"""
    print("请输入你要编译的代码： ")
    while 1:
        new_line = input()
        if new_line == '' : break
        line += new_line if line == '' else ' ' + new_line

    b.lexical_analysi(line)
    """print("\n是否将符号表和中间代码的结果写入PL0_read文件中？ ")
    message = input("请输入 yes or no :")
    while message != "yes" and message != "no" :
        message = input("输入错误，请重新输入:\n")
        time.sleep(3)
    if message ==  "yes":
        e = open('PL0_read.txt','w',encoding = 'UTF-8')
        str_message = str(d.symbol_table)
        e.write(str_message)
        str_message=str(d.intermediate_code_result)
        e.write(str_message)
        print("写入完成,已将文本文件覆盖")"""

