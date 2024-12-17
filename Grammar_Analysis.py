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
global error_tags
error_tags = "" ; """记录出错信息"""
global combination_error_dict
combination_error_dict = dict();"""存储结果使用"""
global judge_a,judge_if,judge_b
global ls_list
ls_list = list()

global symbol_table
symbol_table = list();
"""符号表"""
global intermediate_code
intermediate_code = list();
"""中间代码"""
global intermediate_code_result
intermediate_code_result = dict();
"""存放中间代码以及行号"""
global intermediate_code_location
intermediate_code_location = 1;
"""中间代码位置"""
global physical_block_location
physical_block_location =  1
"""物理块位置"""

def Grammar_analysi():
    e.getsym()
    e.main_program()

