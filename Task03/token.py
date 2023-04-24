class Token:

    def __init__(self, type, lexeme):
        self.type = type # token type
        self.lexeme = lexeme # token value

    def __str__(self):
        return "Token [type=" + str(self.type) + ", lexeme=" + self.lexeme + "]"