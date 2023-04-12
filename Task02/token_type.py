from enum import Enum

class TokenType(Enum):
	NUM = 1
	MINUS = 2
	PLUS = 3
	SLASH = 4
	STAR = 5
	EOF = 6
	
	def __str__(self):
		return self.name
    