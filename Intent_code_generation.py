"""import Grammar_Analysis as d
global Assembly_code;#汇编代码
Assembly_code = dict()
global Assembly_code_location
Assembly_code_location = 1
global Register_blocks;#物理块
Register_blocks = dict()
global Register_blocks_location
Register_blocks_location = 1
global Register_blocks_content;#物理块内容
Register_blocks_content = dict()
def clucute():
    total = d.intermediate_code_result.keys()
    for i in total:
        if d.intermediate_code_result[i][0] == 'const':
            global Register_blocks_location
            physical_code = '$' + str(Register_blocks_location)
            Register_blocks_location += 1
            Register_blocks[physical_code] = d.intermediate_code_result[i][1]
            Assembly_code[Assembly_code_location] =
        elif d.intermediate_code_result[i][0] == '=':
            Register_blocks_content[d.intermediate_code_result[i][3]] = d.intermediate_code_result[i][1]"""