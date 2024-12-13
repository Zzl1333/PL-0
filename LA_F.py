import main as a
import Lexical_Analysis as b

def clearToken():
    b.result.clear()
def IsS_N_T():
    while b.now_char in (' ','\n','\t'):
        getchar();


def goto_LA_F():
    if isLetter():go_isLetter();"""判断字母"""
    elif isDigit():go_isDigit();"""判断数字"""
    elif isColon():go_isColon();"""判断冒号"""
    elif isPlus():go_isPlus();"""判断加号"""
    elif isQuota():go_isQuota();"""判断引号"""
    elif isPlus():go_isPlus();"""判断加号"""
    elif isMinus():go_isMinus();"""判断减号"""
    elif isStar():go_isStar();"""判断星号"""
    elif isEqual():go_isEqual();"""判断等号"""
    elif isExcla():go_isExcla();"""判断叹号"""
    elif isGreat():go_isGreat();"""判断大于号"""
    elif isLess():go_isLess();"""判断小于号"""
    elif isLpar():go_isLpar();"""判断左扩号"""
    elif isRpar():go_isRpar();"""判断右扩号"""
    elif isComma():go_isComma();"""判断逗号"""
    elif isSemi():go_isSemi();"""判断分号"""
    elif isDivi():go_isDivi();"""判断斜竖"""
    else :go_Error();"""错误判断"""

def go_isLetter():
    while isLetter() | isDigit() == 1 :
        catToken()
        getchar()
        if b.now_char == "NULL" :
            break
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
    retract()
    resultValue = reserver(now_result)
    if resultValue == 999 : b.symbol = "IDSY 字符串";
    elif resultValue == 0 : b.symbol = "BEGINSY";
    elif resultValue == 1: b.symbol = "ENDSY";
    elif resultValue == 2: b.symbol = "IFSY";
    elif resultValue == 3: b.symbol = "THENSY";
    elif resultValue == 4: b.symbol = "ELSE";
    elif resultValue == 5:
        array_save()




"""var array[1:5]"""
"""var array"""
def array_save():
    b.symbol = "VAR"
    b.result.clear()
    getchar()
    IsS_N_T()
    global array_record;
    """记录数组的完整表示"""
    array_record = ""

    while b.now_char != "(":
        """数组名部分"""
        catToken()
        array_record = array_record + b.now_char
        getchar()
        if b.now_char == " " or b.now_char == "NULL" or b.now_char == ",": break;"""定义变量结束"""
    now_result = ''.join(b.result)
    b.token.append(now_result)
    b.result.clear()

    if b.now_char == "(":
        catToken()
        array_record = array_record + b.now_char
        getchar()
        now_result = ''.join(b.result)
        b.token.append(now_result)
        b.result.clear()

        while b.now_char != ":":
            catToken()
            array_record = array_record + b.now_char
            getchar()
        now_result = ''.join(b.result)
        b.token.append(now_result)
        b.result.clear()

        if b.now_char == ":":
            catToken()
            array_record = array_record + b.now_char
            getchar()
        now_result = ''.join(b.result)
        b.token.append(now_result)
        b.result.clear()

        while b.now_char != ")":
            catToken()
            array_record = array_record + b.now_char
            getchar()
        now_result = ''.join(b.result)
        b.token.append(now_result)
        b.result.clear()

        if b.now_char == ")":
            catToken()
            array_record = array_record + b.now_char
        now_result = ''.join(b.result)
        b.token.append(now_result)
        b.result.clear()
        b.symbol = "ARRAY 数组"
        if b.symbol == "ARRAY 数组": print(f'{array_record} and {b.symbol}')
        if b.number < b.line_length:
            getchar()
            if b.now_char == ",":
                """,表示继续输入数组"""
                b.token.append(b.now_char)
                array_save()
            else :
                retract()
    else:
        b.symbol = "var 变量"
        if b.number < b.line_length:
            if b.now_char == ",":
                """,表示继续输入定义变量"""
                b.token.append(b.now_char)
                array_save()

def go_isDigit():
    while isDigit() == 1 :
        catToken()
        getchar()
        if b.now_char == "NULL":
            break
    retract()
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
    b.symbol = "INTSY 数字"
def go_isColon():
    catToken();
    getchar()
    if isEqu() == 1:
        catToken()
        b.symbol = "ASSIGNSY 赋值号"
    else :
        retract()
        b.symbol = "COLONSY 冒号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
def go_isQuota():
    catToken()
    b.symbol = "QUOTA 引号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
def go_isPlus():
    catToken()
    b.symbol = "PLUSSY 加号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
def go_isMinus():
    catToken()
    b.symbol = "MINUSSY 减号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
def go_isStar():
    catToken()
    b.symbol = "STARSY 星号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
def go_isEqual():
    catToken()
    b.symbol = "EQUSY 等号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
def go_isExcla():
    catToken()
    b.symbol = "EXCLA 叹号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)

def go_isGreat():
    catToken()
    b.symbol = "GREAT 大于号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)

def go_isLess():
    catToken()
    b.symbol = "LESS 小于号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)

def go_isLpar():
    catToken()
    b.symbol = "LPARSY 左扩号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
def go_isRpar():
    catToken()
    b.symbol = "RPARSY 右扩号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
def go_isComma():
    catToken()
    b.symbol = "COMMASY 逗号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
def go_isSemi():
    catToken()
    b.symbol = "SEMISY 分号"
    global now_result
    now_result = ''.join(b.result)
    b.token.append(now_result)
def go_isDivi():
    global step_number
    step_number =  0
    catToken()
    getchar()
    step_number += 1
    if isStar() == 1:
        catToken()
        getchar()
        step_number += 1
        catToken()
        while isStar() == 0:
            while isStar() == 0:
                getchar()
                step_number += 1
                catToken()
                if b.now_char == "NULL" : break
            while isStar() == 1:
                getchar()
                step_number += 1
                catToken()
                if isDivi():
                    b.symbol = "注释"
                    global now_result
                    now_result = ''.join(b.result)
                    return 0
            if b.now_char == "NULL":break
    p = 0
    while p < step_number :
        retract()
        del b.result[step_number - p]
        p += 1
    now_result = ''.join(b.result)
    b.token.append(now_result)
    b.symbol = "DIVISY 斜竖"
def go_Error():
    catToken()
    global now_result
    now_result = ''.join(b.result)
    b.error_detect = 1

def isLetter():
    if (b.now_char >= 'a' and b.now_char <= 'z') | (b.now_char >= 'A' and b.now_char <= 'Z'):
        return 1
    else : return 0
def isDigit():
    if b.now_char >= '0' and b.now_char <= '9' :
        return 1
    else : return 0
def isColon():
    if b.now_char == ":" : return 1;
    else : return 0;
def isEqu():
    if b.now_char == "=" : return 1;
    else : return 0;
def isQuota():
    if b.now_char == "\"" : return 1;
    else : return 0;
def isPlus():
    if b.now_char == "+" : return 1;
    else : return 0;
def isEqual():
    if b.now_char == "=" : return 1;
    else : return 0;

def isMinus():
    if b.now_char == "-" : return 1;
    else : return 0;
def isStar():
    if b.now_char == "*" : return 1;
    else : return 0;
def isExcla():
    if b.now_char == "!" : return 1;
    else : return 0;
def isGreat():
    if b.now_char == ">" : return 1;
    else : return 0;
def isLess():
    if b.now_char == "<" : return 1;
    else : return 0;
def isLpar():
    if b.now_char == "(" or b.now_char == "{" or b.now_char == "[": return 1;
    else : return 0;
def isRpar():
    if b.now_char == ")" or b.now_char == "}" or b.now_char == "]": return 1;
    else : return 0;
def isComma():
    if b.now_char == "," : return 1;
    else : return 0;
def isSemi():
    if b.now_char == ";" : return 1;
    else : return 0;
def isDivi():
    if b.now_char == "/" : return 1;
    else : return 0;
def getchar():
    if b.number < b.line_length:
        b.now_char = b.line[b.number]
    else :
        b.now_char = "NULL"
        b.number += 1
        return 0
    b.number += 1
    return 0
def catToken():
    b.result.append(b.now_char)
def retract():
    b.number -= 1
def reserver(now_result):
    now_result = now_result.upper()
    try :
        return b.my_list.index(now_result)
    except ValueError as e:
        return 999