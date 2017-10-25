import ply.lex as lex

reservado = {
    'y' : 'AND',
    'o' : 'OR',
    'no' : 'NO',
    'si' : 'CONDICIONAL',
    'entonces' : 'ENTONCES',
    'sino' : 'CONDICIONAL',
    'mientras' : 'CICLO',
    'finmientras' : 'FIN_CICLO'

}


operadores = ['MAS','MENOS','POR','DIVISION','IGUAL','ASIGNACION','MODULO',
              'MAYOR_QUE','MENOR_QUE','MAYOR_IGUAL','MENOR_IGUAL','DIFERENTE']


tokens = operadores + list(reservado.values())+['VAR','NUM']

t_ignore = ' \n:()'
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIVISION = r'\/'
t_IGUAL = r'\=='
t_ASIGNACION = r'\='
t_MODULO = r'\%'
t_MAYOR_QUE = r'\>'
t_MENOR_QUE = r'\<'
t_MAYOR_IGUAL = r'\>='
t_MENOR_IGUAL = r'\<='
t_DIFERENTE = r'\!='

def t_VAR(t):

    r'[a-zA-z_][a-zA-Z_0-9]*'
    t.type = reservado.get(t.value,'VAR')
    return t

def t_NUM(t):
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

    
