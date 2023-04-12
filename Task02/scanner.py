from token import Token
from token_type import TokenType

class Scanner:
    def scan(self, source):
        f = open(source, "r")
        tokens = []

        for line in f:
            string = line.strip()
            token = self.get_token(string)

            if token != None:
                tokens.append(token)
            else:
                print("Error: Unexpected character: " + line)
                return []
            
        return tokens

    def isNumber(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False
        
    def get_token_type(self, string):
        if self.isNumber(string): return TokenType.NUM
        if string == '-': return TokenType.MINUS
        if string == '+': return TokenType.PLUS
        if string == '/': return TokenType.SLASH
        if string == '*': return TokenType.STAR

        return None
    
    def get_token(self, string):
        token_type = self.get_token_type(string)
        if token_type: return Token(token_type, string)

        return None