from model import *


# parser super sencillo y un poco feo
def parser(stringCode):
    end = len(stringCode)-1
    if stringCode[0] != '(':
        # es atomico, asumimos que es un numero
        if stringCode.isnumeric():
            return NumberNode(int(stringCode[0]))
        else:
            raise Exception("Primitive Value " + stringCode[0] + "not supported")
    # sino esta compuesto y es operacion
    stringCode = stringCode[1:len(stringCode)-1]
    # borramos los parentesis del inicio y el final
    first = stringCode[1:end-1].split(" ", 1)
    # partimos por espacios y consideramos si hay sub parentesis
    tokens = splitArgs(stringCode)
    # el primer token es la operacion
    first = tokens.pop(0)
    # los demos son los argumentos
    args = list(map(parser,tokens))
    if first == "+":
        return AdditionNode(args[0],args[1])
    elif first == "-":
        return SubstractNode(args[0],args[1])
    elif first == "++":
        return PlusPlusNode(args[0])
    elif first == "--":
        return MinusMinusNode(args[0])
    else:
        raise Exception("Operation " + first + "not supported")


def splitArgs(string):
    open_counter = 0
    temp = ""
    result = []
    for key in string:
        if key == ' ' and open_counter == 0:
            # adding an argument
            result.append(temp.strip())
            temp = ""
        elif key == '(':
            open_counter = open_counter + 1
        elif key == ')':
            open_counter = open_counter - 1
        else:
            pass
        temp = temp + key
    # adding last arg
    result.append(temp.strip())
    return result
