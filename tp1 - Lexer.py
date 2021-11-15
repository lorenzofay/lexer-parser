#Development for UTN -- My first program in Py --

#Lexer

def lex (cadena_ingresada) :

# Variables temporales.

	digit_temporal	= ""
	cadena_temporal	= ""
	operador_temporal= ""

	lista_tokens = []
	palabras_reservadas = [ "int" , "float" , "for" , "if" , "while" ]
	numeros = [ "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" ]
	opRel = [ "=" , "<" , ">", "!"]
	opMat = [ "+" , "*" , "/" , "-" ]
	simbolo = [ "(" , ")" , "{" , "}", ",", ";", ":="]

	for caracter in cadena_ingresada:
		if caracter.isalpha() :
			cadena_temporal = cadena_temporal + caracter
		elif ( len ( cadena_temporal ) != 0 ) :
			if caracter in simbolo or caracter == " " :
				if cadena_temporal in palabras_reservadas:
					lista_tokens.append(( "<" +cadena_temporal+ ">" , "" ))
					cadena_temporal = ""
				else :
					lista_tokens.append(( "<id>" , cadena_temporal ))
					cadena_temporal = ""
			else :
				print ( "ERROR gramatica no permitida" )
				cadena_temporal = ""
				break
		if caracter in numeros:
			digit_temporal = digit_temporal + caracter
		elif ( len ( digit_temporal ) != 0 ) :
			if caracter.isalpha() :
				print ( "ERROR gramatica no permitida" )
				digit_temporal = ""
				cadena_temporal = ""
				break
			else :
				lista_tokens.append(( "<num>" , digit_temporal ))
				digit_temporal = ""
		if caracter in simbolo or caracter in opMat:
			lista_tokens.append(( "<" +caracter+ ">" , "" ))
		elif caracter in opRel:
			if caracter == "=" and len ( operador_temporal ) !=0 :
				lista_tokens.append(( "<" +operador_temporal + caracter+ ">" , "" ))
				operador_temporal = ""
			elif cadena_ingresada [ cadena_ingresada.index( caracter ) + 1 ] == "=" :
				operador_temporal = operador_temporal + caracter
			else :
				if caracter == "!" :
					print ( "ERROR gramatica no permitida" )
				else :
					lista_tokens.append(( "<" +caracter+ ">" , "" ))
					operador_temporal = ""

	# Si la cadena temporal no se agrego.
	if ( len ( cadena_temporal ) != 0 ) :
		if cadena_temporal in palabras_reservadas:
			lista_tokens. append(( "<" +cadena_temporal+ ">" , "" ))
			cadena_temporal = ""
		else :
			lista_tokens. append(( "<id>" , cadena_temporal ))
			cadena_temporal = ""
	elif ( len ( digit_temporal ) != 0 ) :
		lista_tokens. append(( "< num >" , digit_temporal ))
		digit_temporal = ""

	print (lista_tokens)
		



# Casos de prueba
lex ( "my pogram should fail " ) #todos id
lex ( "define (+ Y 1 23)" ) #['< define >', '< ( >', '< + >', ('< id >','Y'), ('< num >', ''), '< ) >']
lex ( "(if x > y)(x - y)" ) #['< ( >', '< if >', ('< id >', 'x'), '< > >',('< id >', 'y'), '< ) >', '< ( >', ('< id >', 'x'), '< - >', ('< id >', 'y'),'< ) >']
lex ( "define(myfn 2)" ) #['< define >', '< ( >', ('< id >', 'myfn'), ('< num >', ''), '< ) >']
lex ( "xdefine" ) # debe ser un id
lex ( "que no falle <=<=<=" )
#lex ( "norompesnada <" )
lex ( "existe token <=" )
lex ( "unsolo tokens ==" )

#Casos de prueba de errores.
lex ( "define123" ) # Debe arrojar error
lex ( "123define" ) # Debe arrojar error
