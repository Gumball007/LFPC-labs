import string

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

TOKENS = {
    # SPECIAL TYPES
    'ILLEGAL': 'ILLEGAL',
    'EOF': 'EOF',

    # IDENTIFIERS & LITERALS
    'IDENTIFIER': 'IDENTIFIER',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOLEAN',
    'string': 'STRING',
    'char': 'CHAR',

    # OPERATORS
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

    # DELIMITERS
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

    def is_digit(self, c):
        return str(c).isnumeric()

    def is_char(self, c):
        return str(c).isalpha()

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

    # skips whitespaces and taps
    def whiteSpace(self):
        while self.c == " " or self.c == "\t" or self.c == "\r":
            self.nextChar()


    def tokenise(self):
        token = None
        value = ''
        self.whiteSpace()  

        
    
with open('lab3/input.txt') as f:
    contents = f.read()

lexer = Lexer(contents)
tokens = lexer.tokenise()
for token in tokens:
    print(token)