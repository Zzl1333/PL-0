import Lexical_Analysis as b
import GA_F as e

global sym
sym = ""
global read_pointer
read_pointer = 0
global combination_result_dict
combination_result_dict = dict();"""存储结果使用"""
global combination_use_list
combination_use_list = list();"""存储过程使用"""
global combination_use_compound_list
combination_use_compound_list = list();"""存储复合语句使用"""
global combination_use_condition_list
combination_use_condition_list = list();"""存储条件语句使用"""
global combination_use_for_loop_list
combination_use_for_loop_list = list();"""存储条件语句使用"""
global read_tags
read_tags = 0;"""标记list列表已经读取出多少个标识符"""

def Grammar_analysi():
    e.getsym()
    e.main_program()