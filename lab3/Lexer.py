import string

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

SPECIAL_TYPES = {
    'ILLEGAL': 'ILLEGAL',
    'EOF': 'EOF',
}

IDENTIFIERS = {
    'IDENTIFIER': 'IDENTIFIER',
    'NUMBER' :'NUMBER',
    'UNKNOWN': 'UNKNOWN',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOLEAN',
    'string': 'STRING',
    'char': 'CHAR',
}

OPERATORS = {
    ':': 'ASSIGN',
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'MULTIPLY',
    '/': 'DIVIDE',
    '&': 'AND',
    '|': 'OR',
    '=': 'EQUAL1',
    '==': 'EQUAL2',
    '!': 'NEGATE',
    '!=': 'NOT_EQUAL',
    '>': 'GREATER',
    '<': 'LESS',
    '>=': 'GE',
    '<=': 'LE',
}

DELIMITERS = {
    '.': 'DOT',
    ',': 'COMMA',
    ';': 'SEMICOLON',
    '(': 'LPAR',
    ')': 'RPAR',
    '[': 'LBRACK',
    ']': 'RBRACK',
    '{': 'LBRACE',
    '}': 'RBRACE',
    '#': 'COMMENT',
    '\n': 'NEWLINE',
}

KEYWORDS = {
    'var': 'VAR',
    'def': 'FUNCTION',
    'if': 'IF',
    'for': 'FOR',
    'else': 'ELSE',
    'while': 'WHILE',
    'or': 'OR',
    'not': 'NOT',
    'to': 'TO',
    'do': 'DO',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'print': 'PRINT',
}


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class Lexer:

    def __init__(self, input):
        self.input = input + "\0"  # Add EOF 
        self.c = ''
        self.index = -1
        self.nextChar()

    # advance with 1 position in char
    def nextChar(self):
        self.index += 1
        if self.index >= len(self.input):
            self.c == "\0"  
        else:
            self.c = self.input[self.index]

    # peeks but don't move
    def peek(self, moves):
        if self.index + moves >= len(self.input):
            return "\0"
        else:
            return self.input[self.index + moves]

    # skips whitespaces 
    def whiteSpace(self):
        while self.c == " " or self.c == "\t" or self.c == "\r":
            self.nextChar()
        
    def skip(self, x):
        self.index += x


    def isKeyword(text):
        text = text.upper()
        for type in KEYWORDS:
            if text == type.name:
                return type
        return False

    def tokeniser(self):
        token = None
        value = ''
        self.whiteSpace()

        if self.c == "#":
            token = Token(DELIMITERS.PLUS, value)   

        elif self.c == "+":
            token = Token(OPERATORS.PLUS, value)  

        elif self.c == "-":
            token = Token(OPERATORS.MINUS, value) 

        elif self.c == "*":
            token = Token(OPERATORS.MULTIPLY, value) 
        
        elif self.c == ":":  
            token = Token(OPERATORS.ASSIGN, value)

        elif self.c == "&":
            token = Token(OPERATORS.AND, value)  
        
        elif self.c == "|":
            token = Token(OPERATORS.OR, value) 

        elif self.c == "=":
            token = Token(OPERATORS.EQUAL1, value) 

        elif self.c == "=":
            token = Token(OPERATORS.EQUAL2, value)   

        elif self.c == "\n":  
            token = Token(DELIMITERS.NEWLINE, value)

        elif self.c == "\0":  
            token = Token(SPECIAL_TYPES.EOF, value)

        elif self.c == ";": 
            token = Token(DELIMITERS.SEMICOLON, value)
        elif self.c == ",": 
            token = Token(DELIMITERS.COMMA, value)

        elif self.c == "(":  
            token = Token(DELIMITERS.LPAR, value)

        elif self.c == ")":  
            token = Token(DELIMITERS.RPAR, value)
        
        elif self.c == "[": 
            token = Token(DELIMITERS.LBRACK, value)

        elif self.c == "]":  
            token = Token(DELIMITERS.RBRACK, value)
        
        elif self.c == "{":  
            token = Token(DELIMITERS.LPAR, value)

        elif self.c == "}":  
            token = Token(DELIMITERS.RPAR, value)

        elif self.c == "<":
            if self.peek(1) == "=":  
                token = Token(DELIMITERS.LE, value)
                self.skip(1)
            else:  
                token = Token(DELIMITERS.LESS, value)

        elif self.c == ">":
            if self.peek(1) == "=":  
                token = Token(DELIMITERS.GE, value)
                self.skip(1)
            else:  
                token = Token(DELIMITERS.GREATER, ">")

        elif self.c == "!":
            if self.peek(1) == "=":  
                token = Token(DELIMITERS.NOT_EQUAL, value)
                self.skip(1)
            else:  
                token = Token(DELIMITERS.NEGATE, value)

        elif self.c.isalpha():
            while self.c.isalnum():
                value += self.c
                if self.peek(1).isalnum():
                    self.nextChar()
                else:
                    break
            if self.isKeyword(value) != False:
                token = Token(self.isKeyword(value), value)  # Keyword Token
            else:
                token = Token(IDENTIFIERS.IDENTIFIER, value)  # Identifier Token

        elif self.c.isdigit():  # Number Token
            while self.c.isdigit():
                value += self.c
                if self.peek(1).isdigit():
                    self.nextChar()
                else:
                    break
            token = Token(IDENTIFIERS.NUMBER, value)

        else:
            token = Token(IDENTIFIERS.UNKNOWN, self.c)

        self.nextChar()
        return token

with open('lab3/input.txt') as f:
    contents = f.read()

lexer = Lexer(contents)
tokens = lexer.tokeniser()
for tok in tokens:
    print(tok)
