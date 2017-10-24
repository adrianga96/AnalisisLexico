import ply.lex as lex

reservados = {
    'and' : 'OPERADORLOGICO',
    'or' : 'OPERADORLOGICO',
    'not' : 'OPERADORLOGICO',
    'if' : 'CICLO',
    'then' : 'CICLO',
    'else' : 'CICLO',
    'while' : 'CICLO',
    'endwhile' : 'CICLO'

}


operadores = ['PLUS','MINUS','TIMES','DIVIDE','EQUALS','ASSIGN','MODULE',
              'GREATERTHAN','SMALLERTHAN','GREATERQUAL','SMALLEREQUAL','DIFFERENT']


tokens = operadores + list(reservados.values())+['NAME','NUMBER']

t_ignore = ' \n'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\=='
t_ASSIGN = r'\='
t_MODULE = r'\%'
t_GREATERTHAN = r'\>'
t_SMALLERTHAN = r'\<'
t_GREATERQUAL = r'\>='
t_SMALLEREQUAL = r'\<='
t_DIFFERENT = r'\!='

def t_NAME(t):

    r'[a-zA-z_][a-zA-Z_0-9]*'
    t.type = reservados.get(t.value,'NAME')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("caracter erroneo '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()
archivo = open("text.txt","r")

for linea in archivo.readlines():
    lex.input(linea)
    print("\nlinea : " + linea)
    while True:
        tok = lex.token()
        if not tok: break
        print(str(tok.value) + " -> " + str(tok.type))

    