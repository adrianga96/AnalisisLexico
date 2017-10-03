import re 

class Nodo():
    def __init__(self, val, izq=None, der=None):
        self.valor = val
        self.izq = izq
        self.der = der

class Pila:
    def __init__(self):
        self.pila = []
    def agregar(self, elemento):
        self.pila.append(elemento)
    def sacar(self):
        if self.vacia()==False:
            return self.pila.pop()
        else:
            return "Pila vacia"
    def vacia(self):
        return self.pila == []
    
def verificartokens(variable):
    patronVariable = re.compile('^[a-z][a-zA-Z_$0-9]*$')
    patronValor = re.compile('^[-+]?[0-9]+$')
    patronOperador = re.compile('^[+]$|^[*]$|^[-]$|^[/]$|^[=]$')
    comprobacion = True
    for i in variable: 
        if(patronVariable.match(i)):
            var.append(i)
            tokens["Variable"]=var
        elif(patronValor.match(i)):
            val.append(i)
            tokens["Valor"]=val  
        elif(patronOperador.match(i)):
            op.append(i)
            tokens["Operador"]=op
        else:
            error.append(i)
            comprobacion = False
    return comprobacion

    
def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.sacar()
            nodo_izq = pila.sacar()
            pila.agregar(Nodo(lista[0],nodo_izq,nodo_der))
        elif lista[0] in variables:
                valor = variables[lista[0]]
                pila.agregar(Nodo(valor[0]))
        elif lista[0]=="=":
            variable = pila.sacar().valor
            variables[variable] = [evaluar(pila.sacar())]
            
            if  verificartokens(variable)== True:
                print(variable+" = "+str(variables[variable][0]))
            else:
                print("Error de token en el nombre de la variable: " + variable)
                return 0
               
        else:
            pila.agregar(Nodo(lista[0]))
        return convertir(lista[1:],pila)

def evaluar(arbol):
    try:
        if arbol.valor == "+":
            return evaluar(arbol.izq) + evaluar(arbol.der)
        if arbol.valor == "-":
            return evaluar(arbol.izq) - evaluar(arbol.der)
        if arbol.valor == "/":
            return evaluar(arbol.izq) / evaluar(arbol.der)
        if arbol.valor == "*":
            return evaluar(arbol.izq) * evaluar(arbol.der)
        return int(arbol.valor)
    except ValueError:
         print "Error en el nombre de la variable: " + arbol.valor
         return 0

if __name__ == "__main__":
    pila = Pila()
    opcion = "y"
    variables = {}
    tokens = {}
    var = []
    val = []
    op = []
    error = []
    while(opcion == "y" or opcion == "Y"):
        exp = raw_input("Ingrese la expresion en formato posfijo: ").split(" ")
        if(verificartokens(exp)):
            convertir(exp,pila)
        else:
            print "Se han encontrado errores"
            print "Errores: ",error
        for t in tokens:
            print(t," : ",tokens[t])
        var = []
        val = []
        op = []
        error = []
        opcion = raw_input("Desea ingresar otra expresion?:(y,N)")
