import ply.lex as lex

tokens = (
    'NUMERO',
    'SOMA',
    'SUB',
    'MULTI',
    'DIV',
    'APAREN',
    'FPAREN',
)

t_SOMA = r'\+'
t_SUB = r'\-'
t_MULTI = r'\*'
t_DIV = r'/'
t_APAREN = r'\('
t_FPAREN = r'\)'

def t_NUMERO(t):
    r'\d+'
    t.value = float(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Erro de caractere '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = input("Insere seu calculo: \n")
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)