import main as a
import LA_F as c
import Grammar_Analysis as d
import Intent_code_generation as e
global number
number = 0
global my_list
my_list = ['BEGIN','END','IF','THEN','ELSE','VAR']
global token
token = list()
global my_newtoken
my_newtoken = list
global  result
result = list()
global now_char
now_char = ""
global symbol
symbol = ""
global error_detect
error_detect = 0


def cal_result():
    global symbol
    symbol = ""
    global error_detect
    error_detect = 0
    c.clearToken()
    c.getchar()
    c.IsS_N_T()
    c.goto_LA_F();"""转去判断"""


def lexical_analysi(line_a):
        global line
        line = line_a
        global line_length;"""存放输入字符串的长度"""
        line_length = len(line)
        while number < len(line):
            cal_result()
            if error_detect == 0:
                if symbol == "注释": print(f'{c.now_result} and {symbol}')
                elif symbol != "ARRAY 数组" : print(f'{c.now_result} and {symbol}')
            else :
                print(f'error : “ {c.now_result} ” “输入的字符无法识别”')
        print(f'词法分析后的列表list为: {token}')


        while d.read_tags < len(token):
            d.Grammar_analysi()
        """print(f'\n语法分析后的字典dict为: {d.combination_result_dict}\n')"""
        print(f"语法分析后得到的元素有： {d.combination_result_dict.keys()}",end='\n')


        print("符号表为：")
        for i in d.symbol_table:
            for j in i :
                if j is not None:
                    print(j,end=" ")
                    continue
            print(end='\n')
        print("中间代码为：")
        for i in d.intermediate_code_result.keys():
            print(f"{i} {d.intermediate_code_result[i]}")

"""        e.clucute()"""


