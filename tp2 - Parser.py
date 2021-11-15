#Development for UTN -- My first program in Py --

#Parser

from TP1 import lexer

noTerminales = [
	'Funcion',
	'Tipo',
	'ListaArgumento',
	'SentenciaCompuesta',
	'Argumento',
	'Declaracion',
	'ListaIdent',
	'Sentencia',
	'SentFor',
	'SentWhile',
	'Expr',
	'SentIf',
	'ListaSentencia',
	'ValorR',
	'Comparacion',
	'Mag',
	'Termino',
	'X',
	'Factor',
	'Mag2',
	'Termino2'
]

Terminales = [
	'INT',
	'IF',
	'IGUALDOB',
	'PAROPEN',
	'COMA',
	'PARCLOSE',
	'LLAOPEN',
	'LLACLOSE',
	'SUMA',
	'ASTERISCO',
	'MINUS',
	'BARRA',
	'PUNCOMA',
	'MENOR',
	'MAYOR',
	'FLOAT',
	'WHILE',
	'FOR',
	'IGUAL',
	'IGUALMAY',
	'IGUALMEN',
	'DIF',
	'ELSE',
	'ID',
	'NUM',
	'ERROR_EXPRESION_PARCIAL',
	'TOKEN_INCORRECTO' 
]


# TODO prolijidad!
# lo que espero es lo siguiente
# producciones = {
    # 'Funcion': [
        # ['Tipo','ID','PAROPEN','ListaArgumento','PARCLOSE','SentenciaCompuesta']
    # ],
    # 'ListaArgumento': [
        # ['Argumento'],
        # ['Argumento','COMA','ListaArgumento']
    # ],



producciones = {'Funcion': [
					['Tipo','ID','PAROPEN','ListaArgumento','PARCLOSE','SentenciaCompuesta']
					],
				'ListaArgumento': [
					['Argumento'],['Argumento','COMA','ListaArgumento']
					],
				'Argumento':[
					['Tipo','ID']
					],
				'Declaracion':[
					['Tipo','ListaIdent']
					],
				'Tipo':[
					['INT'],['FLOAT']
					],
				'ListaIdent':[
					['ID'],['ID','COMA','ListaIdent']
					],
				'Sentencia':[
					['Declaracion'],['SentFor'],['SentWhile'],['Expr'],['SentIf'],['SentenciaCompuesta']
					],
				'SentFor':[
					['FOR','PAROPEN','Expr','COMA','Expr','COMA','Expr','PARCLOSE','Sentencia'],
					['FOR','PAROPEN','Expr','COMA','COMA','Expr','PARCLOSE','Sentencia'],
					['FOR','PAROPEN','Expr','COMA','Expr','COMA','PARCLOSE','Sentencia'],
					['FOR','PAROPEN','Expr','COMA','COMA','PARCLOSE','Sentencia']],
				'SentWhile':[['WHILE','PAROPEN','Expr','PARCLOSE','Sentencia']
					],
				'SentIf':[
					['IF','PAROPEN','Expr','PARCLOSE','Sentencia','ELSE','PAROPEN','Sentencia','PARCLOSE'],
					['IF','PAROPEN','Expr','PARCLOSE','Sentencia']
					],
				'SentenciaCompuesta':[
					['LLAOPEN','ListaSentencia','LLACLOSE']
					],
				'ListaSentencia':[
					['Sentencia'],['Sentencia','ListaSentencia']
					],
				'Expr':[
					['ValorR'],['ID','IGUAL','Expr']
					],
				'ValorR':[
					['Mag'],['Mag','X']
					],
				'X':[
					['Comparacion','Mag'],['Comparacion','Mag','X']
					],
				'Comparacion':[
					['IGUALDOB'],['MAYOR'],['MENOR'],['IGUALMAY'],['IGUALMEN'],['DIF']
					],
				'Mag':[
					['Termino'],['Termino','Mag2']
					],
				'Mag2':[
					['MINUS','Termino'],['SUMA','Termino'],['MINUS','Termino','Mag2'],['SUMA','Termino','Mag2']
					],
				'Termino':[
					['Factor'],['Factor','Termino']
					],
				'Termino2':[
					['BARRA','Factor'],['ASTERISCO','Factor'],['BARRA','Factor','Termino2'],['ASTERISCO','Factor','Termino2']
					],
				'Factor':[
					['NUM'],['ID'],['PAROPEN','Expr','PARCLOSE'],['SUMA','Factor'],['MINUS','Factor']
					]
				}

# TODO prolijidad! Cada clave valor en una sola linea, espacios despues de ":"
estado = {'error': False,
			'puntero': 0,
			'cadena': [],
			'terminalesIdentificados': [],
			'terminalActual': estado['cadena'][estado['puntero']],
			}

def importarTokens(src):
	listaDeTerminales = []
	tuplas = lexer(src)
	for elemento in tuplas:
		listaDeTerminales.append(elemento[0])
	listaDeTerminales.append('$')
	return listaDeTerminales

def cantdeProd(cadena):
	for i in producciones:
		if (cadena == i):
			return(len(producciones[i]))	

def ASDR(noTerminal):547186
	for prod in cantdeProd(noTerminal):
		estado['error'] = True
		analizar(producciones[noTerminal][prod])

def analizar(produccion):
	punteroAuxiliar = estado['puntero']
	produccionesAuxiliar = estado['terminalesIdentificados']
	estado['error'] = False
	for nodo in len(produccion):
		if estado['error']==true:
			break
		else:
			if nodo in Terminales:
				if nodo == terminalActual:
					estado['puntero'] += 1
					estado['terminalesIdentificados'].append(nodo)
				else:
					estado['puntero'] = punteroAuxiliar
					estado['error'] = True
			if nodo in noTerminales:
				ASDR(nodo)

def parser(src) :
	estado['puntero'] = 0
	estado['cadena'] = importarTokens(src) 
	ASDR('Funcion')	
	if not estado['error'] and terminalActual == '$' :
		print('La cadena: ',estado['cadena'],' pertenece al lenguaje')
		return True
		print(estado['terminalesIdentificados'])
	else:
		print('La cadena: ',estado['cadena'],' no pertenece al lenguaje')
		print(estado['terminalesIdentificados'])
		return False

assert parser('int a ( float a ) { int b }') == True
assert parser('int') == False
assert parser('int a ( float b ) { int c }') == True
assert parser('1') == False
assert parser('int a (float hola) {ab}') == True
assert parser('int hola ( float beta ) { 34 }') == True
assert parser("int variable (int otravariable){int otravariable}") == True
assert parser("float variable (int otravariable){int otravariable}") == True
assert parser("float a (int b , int c) { for ( 1 , d , 2 ) int e }") == True
assert parser("hola mundo") == False