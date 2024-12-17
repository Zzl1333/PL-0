import Lexical_Analysis as b
import Grammar_Analysis as d

def getsym():
    d.sym = b.token[d.read_pointer]
    d.read_pointer += 1
    d.read_tags +=1
def main_program():
    global mark
    mark = ""
    part_program()
def part_program():
    d.combination_use_list.clear()
    if d.sym == "const" or d.sym == "CONST": constant_dscription()
    elif d.sym == "var" or d.sym == "VAR": quantity_description()
    elif d.sym == "procedure" or d.sym == "PROCEDURE": process_description()
    else : statement()

"""----------------------------分隔符----------------------------------"""
def constant_dscription():
    """常量说明部分"""
    constant_definition()
def quantity_description():
    """变量说明部分"""
    quantity_definition()
def process_description():
    """过程说明部分"""
    process_definition()
def statement():
    """语句"""
    d.combination_use_list.clear()
    if d.sym == "begin" :
        compound_statement()
        return 1
    elif d.sym == "if" :
        conditional_statement()
        return 1
    elif d.sym == "while" :
        for_loop_statement()
        return 1
    elif d.sym == "call" :
        procedure_call_statement()
        return 1
    elif d.sym == "read" :
        read_statement()
        return 1
    elif d.sym == "write" :
        write_statement()
        return 1
    else :
        if assignment_statement() == 1:
            return 1


"""----------------------------分隔符----------------------------------"""
"""语句"""
def compound_statement():
    """复合语句"""
    d.combination_use_compound_list.clear()
    d.combination_use_compound_list.append(d.sym)
    d.combination_use_compound_list.append(" :")
    d.combination_use_condition_list.clear()
    getsym()
    while d.sym != "end":
        statement()
        if len(d.combination_use_list) == 0 :
            d.combination_use_compound_list.extend(d.combination_use_condition_list)
        else :
            d.combination_use_compound_list.extend(d.combination_use_list)

        if d.read_tags < len(b.token):
            getsym()
    d.combination_use_compound_list.append(" ")
    d.combination_use_compound_list.append(d.sym)
    combination_result = ''.join(d.combination_use_compound_list)
    d.combination_result_dict[combination_result] = f'这是一个复合语句 '
    return 1

def conditional_statement():
    """条件语句"""
    d.combination_use_list.clear()
    d.combination_use_list.append(d.sym)
    d.combination_use_list.append(" ")
    getsym()
    if is_condition() == 1:
        getsym()
        if d.sym == "then" :
            d.combination_use_list.append(" ")
            d.combination_use_list.append(d.sym)
            getsym()
            d.combination_use_condition_list.extend(d.combination_use_list)
            d.combination_use_condition_list.append(" ")
            if statement() == 1:
                d.combination_use_condition_list.extend(d.combination_use_list)
                if d.read_tags < len(b.token):
                    getsym()
                    if d.sym == "else":
                        d.combination_use_condition_list.append(" ")
                        d.combination_use_condition_list.extend(d.sym)
                        d.combination_use_condition_list.append(" ")
                        getsym()
                        if statement() == 1:
                            d.combination_use_condition_list.extend(d.combination_use_list)
                            combination_result = ''.join(d.combination_use_condition_list)
                            d.combination_use_list.clear()
                            d.combination_result_dict[combination_result] = "这是一个条件语句 ::= if<条件>then<语句>[else<语句>]"
                    else :
                        d.read_pointer -= 1
                        d.read_tags -= 1
                        return 1
                else :
                    combination_result = ''.join(d.combination_use_condition_list)
                    d.combination_result_dict[combination_result] = "这是一个条件语句 ::= if<条件>then<语句>"

def for_loop_statement():
    """当型循环语句"""
    d.combination_use_list.clear()
    d.combination_use_list.append(d.sym)
    d.combination_use_list.append(" ")
    getsym()
    if is_condition() == 1:
        getsym()
        if d.sym == "do" :
            d.combination_use_list.append(" ")
            d.combination_use_list.append(d.sym)
            d.combination_use_list.append(" ")
            getsym()
            d.combination_use_for_loop_list.extend(d.combination_use_list)
            if statement() == 1:
                d.combination_use_for_loop_list.extend(d.combination_use_list)
                combination_result = ''.join(d.combination_use_for_loop_list)
                d.combination_result_dict[combination_result] = "这是一个当型循环语句 ::= while <条件> do <语句>"

def procedure_call_statement():
    """过程调用语句"""
    d.combination_use_list.clear()
    d.combination_use_list.append(d.sym)
    getsym()
    if is_letter_number(d.sym):
        d.combination_use_list.append(d.sym)

        d.intermediate_code.append((d.combination_use_list[0], d.combination_use_list[1], "_", "_"))
        d.intermediate_code_result[d.intermediate_code_location] = ((d.combination_use_list[0], d.combination_use_list[1], "_", "_"))
        d.intermediate_code_location += 1

        if d.read_tags < len(b.token):
            getsym()

        if d.sym == "(":
            d.combination_use_list.append(d.sym)
            getsym()
            if pass_by_value() == 1:
                getsym()
                while d.sym != ")":
                    if d.sym == ",":
                        d.combination_use_list.append(d.sym)
                        getsym()
                        if pass_by_value() == 1:
                            getsym()
                d.combination_use_list.append(d.sym)
                combination_result = ' '.join(d.combination_use_list)
                d.combination_result_dict[combination_result] = "这是一个过程调用语句 ::= call <标识符> [(<传值参数>{，<传值参数>})]"
                return 1
        else:
            d.read_pointer -= 1
            d.read_tags -= 1
            combination_result = ' '.join(d.combination_use_list)
            d.combination_result_dict[combination_result] = "这是一个过程调用语句 ::= call <标识符> [(<传值参数>{，<传值参数>})]"
            return 1
    else:return 0

def read_statement():
    """读语句"""
    d.combination_use_list.clear()
    d.combination_use_list.append(d.sym)
    getsym()
    if d.sym == "(":
        d.combination_use_list.append(d.sym)
        getsym()
        if is_variables() == 1 :
            getsym()
            while d.sym != ")":
                if d.sym == ",":
                    d.combination_use_list.append(d.sym)
                    getsym()
                    if is_variables() == 1:
                        getsym()
            for i in range(len(d.ls_list)):
                d.intermediate_code.append(('read', d.ls_list[i], '_', '_'))
                d.intermediate_code_result[d.intermediate_code_location] = (('read', d.ls_list[i], '_', '_'))
                d.intermediate_code_location += 1

            d.ls_list.clear()
            d.combination_use_list.append(d.sym)
            combination_result = ''.join(d.combination_use_list)
            d.combination_result_dict[combination_result] = "这是一个读语句 ::= read (<变量引用>{,<变量引用>})"
            return 1

def write_statement():
    """写语句"""
    d.combination_use_list.clear()
    d.combination_use_list.append(d.sym)
    d.combination_use_list.append(" ")
    getsym()
    if d.sym == "(":
        d.combination_use_list.append(d.sym)
        getsym()
        if is_expression() == 1:
            getsym()
            while d.sym != ")":
                if d.sym == ",":
                    d.combination_use_list.append(d.sym)
                    d.ls_list.append(',')
                    getsym()
                    if is_expression() == 1:
                        getsym()
            d.combination_use_list.append(d.sym)

            lisi_list = list()
            i = 0
            while len(d.ls_list) != 0:
                if d.ls_list[i] == ',':
                    lisi_list.extend(d.ls_list[0:i])
                    j = 0
                    while j <= i :
                        d.ls_list.pop(i-j)
                        j+=1
                    i = 0

                    while len(lisi_list) != 1:
                        while '*' in lisi_list:
                            """先处理符号串中的*运算"""
                            lo = lisi_list.index('*')
                            physical_code = 'T' + str(d.physical_block_location)
                            d.physical_block_location += 1
                            d.intermediate_code.append(
                                (lisi_list[lo], lisi_list[lo - 1], lisi_list[lo + 1], physical_code))
                            d.intermediate_code_result[d.intermediate_code_location] = (
                                (lisi_list[lo], lisi_list[lo - 1], lisi_list[lo + 1], physical_code))
                            d.intermediate_code_location += 1
                            lisi_list[lo + 1] = physical_code
                            lisi_list.pop(lo)
                            lisi_list.pop(lo - 1)

                        while '/' in lisi_list:
                            """先处理符号串中的/运算"""
                            lo = d.ls_list.index('/')
                            physical_code = 'T' + str(d.physical_block_location)
                            d.physical_block_location += 1
                            d.intermediate_code.append(
                                (lisi_list[lo], lisi_list[lo - 1], lisi_list[lo + 1], physical_code))
                            d.intermediate_code_result[d.intermediate_code_location] = (
                                (lisi_list[lo], lisi_list[lo - 1], lisi_list[lo + 1], physical_code))
                            d.intermediate_code_location += 1
                            lisi_list[lo + 1] = physical_code
                            lisi_list.pop(lo)
                            lisi_list.pop(lo - 1)
                        if len(lisi_list) == 1:
                            d.intermediate_code.append(('write', lisi_list[0], '_', '_'))
                            d.intermediate_code_result[d.intermediate_code_location] = (
                            ('write', lisi_list, '_', '_'))
                            d.intermediate_code_location += 1
                            lisi_list.clear()

                        """多次计算时选择物理块保存中间数据"""
                        physical_code = 'T' + str(d.physical_block_location)
                        d.physical_block_location += 1
                        d.intermediate_code.append((lisi_list[1], lisi_list[0], lisi_list[2], physical_code))
                        d.intermediate_code_result[d.intermediate_code_location] = (
                            (lisi_list[1], lisi_list[0], lisi_list[2], physical_code))
                        d.intermediate_code_location += 1
                        lisi_list[2] = physical_code
                        lisi_list.pop(1)
                        lisi_list.pop(0)

                    d.intermediate_code.append(('write', lisi_list[0], '_', '_'))
                    d.intermediate_code_result[d.intermediate_code_location] = (
                        ('write', lisi_list[0], '_', '_'))
                    d.intermediate_code_location += 1
                    lisi_list.clear()

                    continue
                elif ',' not in d.ls_list:
                    lisi_list.extend(d.ls_list)
                    d.ls_list.clear()
                    while len(lisi_list) != 1:
                        while '*' in lisi_list:
                            """先处理符号串中的*运算"""
                            lo = lisi_list.index('*')
                            physical_code = 'T' + str(d.physical_block_location)
                            d.physical_block_location += 1
                            d.intermediate_code.append(
                                (lisi_list[lo], lisi_list[lo - 1], lisi_list[lo + 1], physical_code))
                            d.intermediate_code_result[d.intermediate_code_location] = (
                                (lisi_list[lo], lisi_list[lo - 1], lisi_list[lo + 1], physical_code))
                            d.intermediate_code_location += 1
                            lisi_list[lo + 1] = physical_code
                            lisi_list.pop(lo)
                            lisi_list.pop(lo - 1)

                        while '/' in lisi_list:
                            """先处理符号串中的/运算"""
                            lo = d.ls_list.index('/')
                            physical_code = 'T' + str(d.physical_block_location)
                            d.physical_block_location += 1
                            d.intermediate_code.append(
                                (lisi_list[lo], lisi_list[lo - 1], lisi_list[lo + 1], physical_code))
                            d.intermediate_code_result[d.intermediate_code_location] = (
                                (lisi_list[lo], lisi_list[lo - 1], lisi_list[lo + 1], physical_code))
                            d.intermediate_code_location += 1
                            lisi_list[lo + 1] = physical_code
                            lisi_list.pop(lo)
                            lisi_list.pop(lo - 1)
                        if len(lisi_list) == 1:
                            d.intermediate_code.append(('write', lisi_list[0], '_', '_'))
                            d.intermediate_code_result[d.intermediate_code_location] = (
                            ('write', lisi_list[0], '_', '_'))
                            d.intermediate_code_location += 1
                            lisi_list.clear()
                            break

                        """多次计算时选择物理块保存中间数据"""
                        physical_code = 'T' + str(d.physical_block_location)
                        d.physical_block_location += 1
                        d.intermediate_code.append((lisi_list[1], lisi_list[0], lisi_list[2], physical_code))
                        d.intermediate_code_result[d.intermediate_code_location] = (
                            (lisi_list[1], lisi_list[0], lisi_list[2], physical_code))
                        d.intermediate_code_location += 1
                        lisi_list[2] = physical_code
                        lisi_list.pop(1)
                        lisi_list.pop(0)

                i += 1


            combination_result = ''.join(d.combination_use_list)
            d.combination_result_dict[combination_result] = "这是一个写语句 ::= write (<表达式>{,<表达式>})"
            return 1

def assignment_statement():
    """赋值语句"""
    if is_variables() == 1:
        judge_a = d.ls_list[0]
        d.ls_list.clear()
        getsym()
        if d.sym == ":=":
            judge_if = d.sym
            d.combination_use_list.append(d.sym)
            getsym()
            if is_expression() == 1:
                length = len(d.ls_list)
                cishu = int(length/2)

                if cishu == 0 :
                    judge_b = d.ls_list[0]
                    judge_c = '_'
                    d.intermediate_code.append((judge_if, judge_b, judge_c, judge_a))
                    d.intermediate_code_result[d.intermediate_code_location] = ((judge_if, judge_b, judge_c, judge_a))
                    d.intermediate_code_location += 1
                    d.ls_list.clear()

                elif cishu == 1:
                    judge_b = d.ls_list[0]
                    judge_if = d.ls_list[1]
                    judge_c = d.ls_list[2]
                    d.intermediate_code.append((judge_if, judge_b, judge_c, judge_a))
                    d.intermediate_code_result[d.intermediate_code_location] = ((judge_if, judge_b, judge_c, judge_a))
                    d.intermediate_code_location += 1
                    d.ls_list.clear()
                elif cishu >= 2:
                    i = 0
                    while len(d.ls_list) != 3 :
                        while '*' in d.ls_list:
                            """先处理符号串中的*运算"""
                            lo = d.ls_list.index('*')
                            physical_code = 'T' + str(d.physical_block_location)
                            d.physical_block_location += 1
                            d.intermediate_code.append((d.ls_list[lo], d.ls_list[lo-1], d.ls_list[lo+1], physical_code))
                            d.intermediate_code_result[d.intermediate_code_location] = ((d.ls_list[lo], d.ls_list[lo-1], d.ls_list[lo+1], physical_code))
                            d.intermediate_code_location += 1
                            d.ls_list[lo+1] = physical_code
                            d.ls_list.pop(lo)
                            d.ls_list.pop(lo-1)

                        while '/' in d.ls_list:
                            """先处理符号串中的/运算"""
                            lo = d.ls_list.index('/')
                            physical_code = 'T' + str(d.physical_block_location)
                            d.physical_block_location += 1
                            d.intermediate_code.append((d.ls_list[lo], d.ls_list[lo-1], d.ls_list[lo+1], physical_code))
                            d.intermediate_code_result[d.intermediate_code_location] = ((d.ls_list[lo], d.ls_list[lo-1], d.ls_list[lo+1], physical_code))
                            d.intermediate_code_location += 1
                            d.ls_list[lo+1] = physical_code
                            d.ls_list.pop(lo)
                            d.ls_list.pop(lo-1)

                        """多次计算时选择物理块保存中间数据"""
                        physical_code = 'T' + str(d.physical_block_location)
                        d.physical_block_location += 1
                        d.intermediate_code.append((d.ls_list[1], d.ls_list[0], d.ls_list[2], physical_code))
                        d.intermediate_code_result[d.intermediate_code_location] = ((d.ls_list[1], d.ls_list[0], d.ls_list[2], physical_code))
                        d.intermediate_code_location += 1
                        d.ls_list[2] = physical_code
                        d.ls_list.pop(1)
                        d.ls_list.pop(0)

                    d.intermediate_code.append((d.ls_list[1], d.ls_list[0], d.ls_list[2], judge_a))
                    d.intermediate_code_result[d.intermediate_code_location] = (
                    (d.ls_list[1], d.ls_list[0], d.ls_list[2], judge_a))
                    d.intermediate_code_location += 1
                    d.ls_list.clear()



                combination_result = ''.join(d.combination_use_list)
                d.combination_result_dict[combination_result] = "这是一个赋值语句 ::= <变量引用>:=<表达式>"
                return 1





"""----------------------------分隔符----------------------------------"""
"""过程说明部分"""
def process_definition():
    d.combination_use_list.clear()
    getsym()
    global constant
    constant = ""
    constant = d.sym
    if identifier(constant) == 1:
        d.combination_use_list.append(constant)

        mmk = 0
        for lo in d.symbol_table:
            if lo[1] == constant: mmk = 1
        if mmk == 0:
            d.symbol_table.append(("procedure", constant))
        if mmk == 1:
            print(f"{constant}已声明]")
        mmk = 0

        combination_result = ''.join(d.combination_use_list)

        d.intermediate_code.append(("procedure", combination_result, "_", "_"))
        d.intermediate_code_result[d.intermediate_code_location] = (("procedure", combination_result, "_", "_"))
        d.intermediate_code_location += 1

        d.combination_result_dict[combination_result] = "这是一个procedure <标识符>"
        if d.read_tags < len(b.token):
            getsym()
            if d.sym == "," : process_definition()
            else :
                part_program()
                if d.read_tags < len(b.token):
                    getsym()
                    while d.sym == ";" :
                        process_definition()
                        getsym()
                    d.read_pointer -= 1
                    d.read_tags -= 1
                    return 1
"""----------------------------分隔符----------------------------------"""
"""变量说明部分"""
def quantity_definition():
    """变量声明"""
    d.combination_use_list.clear()
    getsym()
    global constant
    constant = ""
    constant = d.sym
    d.combination_use_list.append(constant)
    if identifier(constant) == 1:
        now_use = constant
        mmk = 0
        for lo in d.symbol_table:
            if lo[1] == constant: mmk = 1
        if mmk == 0:
            d.symbol_table.append(("var", now_use, "0"));
            """先将变量放入符号表，值设为0"""
        if mmk == 1:
            print(f"{constant}已声明]")
        mmk = 0
        d.intermediate_code.append(("var", constant, "_", "_"))

        if d.read_tags < len(b.token) :
            getsym()
            constant = d.sym
            if constant == "(":
                """这是一个数组"""
                d.combination_use_list.append(constant)

                linshi_use = list()
                linshi_use.append(constant)
                getsym()

                constant = d.sym
                if array_bound(constant) == 1:
                    d.combination_use_list.append(constant)
                    linshi_use.append(constant)
                    getsym()
                    constant = d.sym
                    if constant == ":":
                        d.combination_use_list.append(constant)
                        linshi_use.append(constant)
                        getsym()
                        constant = d.sym
                        if array_bound(constant) == 1:
                            d.combination_use_list.append(constant)
                            linshi_use.append(constant)
                            getsym()
                            constant = d.sym
                            if constant == ")":
                                d.combination_use_list.append(constant)
                                linshi_use.append(constant)
                                if d.read_tags < len(b.token):
                                    getsym()
                                global combination_result

                                linshi_use = ''.join(linshi_use)
                                mmk = 0
                                for lo in d.symbol_table:
                                    if lo[1] == constant: mmk = 1
                                if mmk == 0:
                                    d.symbol_table.pop()
                                d.symbol_table.append(("var", now_use, linshi_use));
                                """将变量数组放入符号表"""
                                if mmk == 1:
                                    print(f"{constant}已声明")
                                mmk = 0
                                combination_result = ''.join(d.combination_use_list)
                                d.intermediate_code.pop()
                                d.intermediate_code.append(("var", combination_result, "_", "_"))
                                d.intermediate_code_result[d.intermediate_code_location] = (
                                ("var", combination_result, "_", "_"))
                                d.intermediate_code_location += 1


                                d.combination_result_dict[combination_result] = "这是一个var <变量声明>::= <标识符>(<数组界>:<数组界>)"
            else :
                """这只是一个变量，后续继续输入"""
                d.intermediate_code_result[d.intermediate_code_location] = (("var", now_use, "_", "_"))
                d.intermediate_code_location += 1
                combination_result = ''.join(d.combination_use_list)
                d.combination_result_dict[combination_result] = "这是一个var <变量声明>"
        else :
            """这只是一个变量，后续无输入，仅定义一个变量,即<变量>::=<标识符>"""
            d.intermediate_code_result[d.intermediate_code_location] = (("var", now_use, "_", "_"))
            d.intermediate_code_location += 1
            combination_result = ''.join(d.combination_use_list)
            d.combination_result_dict[combination_result] = "这是一个var <变量声明>"
    if d.read_tags < len(b.token):
        if d.sym == "," : quantity_description()
        elif d.sym == "const" :constant_definition()
        elif d.sym == "var" :quantity_description()
        elif d.sym == " " : return 0
        else :
            d.read_pointer -= 1
            d.read_tags -= 1
            return 1
def array_bound(constant):
    """数组界"""
    if identifier(constant) == 1: return 1
    elif is_number(constant) == 1: return 1
    else : return 0
"""----------------------------分隔符----------------------------------"""
"""常量说明部分"""
def constant_definition():
    """常量定义"""
    d.combination_use_list.clear()
    getsym()
    global constant
    constant = ""
    constant = d.sym
    if identifier(constant) == 1:
        getsym()
        if d.sym == "=" :
            global unsigned_number
            unsigned_number = ""
            getsym()
            unsigned_number = d.sym
            if unsigned_integer(unsigned_number) == 1 :
                d.combination_use_list.append(constant)
                d.combination_use_list.append("=")
                d.combination_use_list.append(unsigned_number)

                d.intermediate_code.append(("const", constant, "_", "_"))
                d.intermediate_code_result[d.intermediate_code_location] = (("const", constant, "_", "_"))
                d.intermediate_code_location += 1
                d.intermediate_code.append(("=", unsigned_number, "_", constant))
                d.intermediate_code_result[d.intermediate_code_location] = (("=", unsigned_number, "_", constant))
                d.intermediate_code_location += 1

                mmk = 0
                for lo in d.symbol_table:
                    if lo[1] == constant: mmk = 1
                if mmk == 0:
                    d.symbol_table.append(("const", constant, unsigned_number));
                    """将常量放入符号表"""
                if mmk == 1:
                    print(f"{constant}已声明")
                mmk = 0

                global combination_result
                combination_result = ''.join(d.combination_use_list)
                d.combination_result_dict[combination_result]= "这是一个const <常量定义>::= <标识符>=<无符号整数>"
    if d.read_tags < len(b.token):
        getsym()
        if d.sym == "," :
            constant_definition()
        elif d.sym == "var" :
            quantity_definition()
        else :
            d.read_pointer -= 1
            d.read_tags -= 1
            return 1
def identifier(constant):
    """标识符"""
    global identifier_mark
    identifier_mark = 1;"""1代表正确，0代表错误"""
    identifier_mark = is_letter_number(constant)
    if identifier_mark == 1 :return 1
    else : return 0
def unsigned_integer(unsigned_number):
    """无符号整数"""
    global unsigned_number_mark
    unsigned_number_mark = 1;"""1代表正确，0代表错误"""
    unsigned_number_mark = is_number(unsigned_number)
    if unsigned_number_mark == 1 :return 1
    else :return 0

"""----------------------------分隔符----------------------------------"""
"""终结符匹配函数"""
def is_letter_number(constant):
    """判断标识符"""
    if constant[0] >= "0" and constant[0] <= "9":
        return 0
    for i in constant[1:]:
        if i < "0" or (i > "9" and i < "A") or (i > "Z" and i < "a") or i > "z" :
            return 0
    else :return 1

def is_letter():
    """判断字母"""
    for i in constant:
        if i < "A" or (i > "Z" and i < "a") or i > "z":
            return 0
    else:return 1
def is_number(unsigned_number):
    """判断数字"""
    for i in unsigned_number:
        if i < "0" or i > "9":
            return 0
    else :return 1

def is_condition():
    """判断条件"""
    if is_expression() == 1 :
        judge_a = d.ls_list[0]
        getsym()
        if relational_operators(d.sym) == 1:
            judge_if = d.sym
            getsym()
            if is_expression() == 1:
                judge_b = d.ls_list[1]
                physical_code = '$' + str(d.intermediate_code_location + 1)
                judge_if = 'j' + str(judge_if)
                d.intermediate_code.append((judge_if, judge_a, judge_b, physical_code))
                d.intermediate_code_result[d.intermediate_code_location] = ((judge_if, judge_a, judge_b, physical_code))
                d.intermediate_code_location += 1
                d.ls_list.clear()

                return 1
    elif d.sym == "odd" :
        d.combination_use_list.append(d.sym)
        getsym()
        if is_expression() == 1:
            d.combination_use_list.append(d.sym)
            return 1
    else : return 0

def is_expression():
    """判断表达式"""
    if d.sym == "+" or d.sym == "-":
        d.combination_use_list.append(d.sym)
        getsym()
    if is_term() == 1:
        if d.read_tags < len(b.token):
            getsym()
            while d.sym == "+" or d.sym == "-":
                d.combination_use_list.append(d.sym)
                d.ls_list.append(d.sym)
                getsym()
                if is_term() == 1:
                    if d.read_tags < len(b.token):
                        getsym()
            d.read_pointer -= 1
            d.read_tags -= 1
            return 1
        return 1
    else : return 0

def is_term():
    """判断项"""
    if is_factor() == 1:
        if d.read_tags < len(b.token):
            getsym()
            while d.sym == "*" or d.sym == "/":
                d.combination_use_list.append(d.sym)
                d.ls_list.append(d.sym)
                getsym()
                if is_factor() == 1 :
                    getsym()
            d.read_pointer -= 1
            d.read_tags -= 1
            return 1
        else : return 1
    else :
        return 0

def is_factor():
    """判断因子"""
    if is_variables() == 1:
        return 1
    elif is_number(d.sym) == 1:
        d.combination_use_list.append(d.sym)
        d.ls_list.append(d.sym)
        return 1
    elif d.sym == "(":
        d.combination_use_list.append(d.sym)
        getsym()
        if is_expression() == 1:
            d.combination_use_list.append(d.sym)
            getsym()
            if d.sym == ")":
                d.combination_use_list.append(d.sym)
                return 1
    else:
        return 0

def is_variables():
    """变量引用"""
    if is_letter_number(d.sym) == 1:
        d.combination_use_list.append(d.sym)
        d.ls_list.append(d.sym)
        if d.read_tags < len(b.token):
            getsym()
            if d.sym == "(":
                if is_expression() == 1:
                    d.combination_use_list.append(d.sym)
                    getsym()
                    if d.sym == ")":
                        d.combination_use_list.append(d.sym)
                        return 1
            else:
                d.read_pointer -= 1
                d.read_tags -= 1
                return 1
    else : return 0

def relational_operators(code):
    """关系运算符"""
    if code in ["==","#","<","<=",">",">="]:
        d.combination_use_list.append(d.sym)
        return 1
    else : return 0

def pass_by_value():
    """传值参数"""
    if is_expression() == 1:
        return 1
    else :return 0

def error_calculate():
    """处理出错"""
