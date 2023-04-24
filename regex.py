from re import compile

class Regex:

    @staticmethod
    def isNum(element):
        # Numero usa . como separador de decimal
        # Numero pode ser positivo (sem sinal) ou negativo
        regex = compile(r'^-?\d+(?:\.\d*)?$')
        result = regex.match(element)

        return result is not None

    @staticmethod
    def isOp(element):
        # Operadores: -, +, * ou /
        regex = compile(rf'^[+\-*\/]$')
        result = regex.match(element)

        return result is not None
