import Lexical_Analysis as b
import re

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    global line
    line = ""
    print("请输入要分析的程序:")
    while 1:
        new_line = input()
        if new_line == '' : break
        line += new_line if line == '' else ' ' + new_line
    b.lexical_analysi(line)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
