from ply.ply.yacc import yacc
from ply.ply.lex import lex
import os
from crearhtml import  createHTML

#ANÁLISIS LÉXICO

def getColumn(t):
  line_start = INPUT.rfind('\n', 0, t.lexpos) + 1
  return (t.lexpos-line_start)+1

exp_reg = {   #ingresar las expresiones regulares
  'true': 'tk_boolean_true',
  'false':'tk_boolean_false',
  'int':  't_tk_tipo_int',
  'double': 't_tk_tipo_double',
  'string': 't_tk_tipo_string',
  'char': 't_tk_tipo_char',
  'boolean': 't_tk_tipo_boolean',
  'else': 't_tk_condicional_else',
  'while': 't_tk_iterativo_while',
  'do': 't_tk_iterativo_do',
  'void':'t_tk_reservda_void',
  'return':'t_tk_reservada_return',
}




reserved = {
  'true': 'tk_boolean_true',
  'false':'tk_boolean_false',
  'int':  't_tk_tipo_int',
  'double': 't_tk_tipo_double',
  'string': 't_tk_tipo_string',
  'char': 't_tk_tipo_char',
  'boolean': 't_tk_tipo_boolean',
  'else': 't_tk_condicional_else',
  'while': 't_tk_iterativo_while',
  'do': 't_tk_iterativo_do',
  'void':'t_tk_reservda_void',
  'return':'t_tk_reservada_return',
}

tokens = (
  #LEXEMAS DEL PROYECTO, AUN FALTA AGREGAR LO NUEVO
  'tk_comentario_var_filas',
  'tk_tipo_int',
  'tk_tipo_double',
  'tk_tipo_string',
  'tk_tipo_char',
  'tk_tipo_boolean',
  'tk_suma',
  'tk_resta',
  'tk_multiplicacion',
  'tk_resto',
  'tk_diferenciacion',
  'tk_mayor_o_igual_que',
  'tk_mayor_que',
  'tk_menor_o_igual_que',
  'tk_menor_que',
  'tk_and',
  'tk_or',
  'tk_not',
  'tk_punto_coma',
  'tk_condicional',
  'tk_par_abierto',
  'tk_par_cerrado',
  'tk_llave_abierta',
  'tk_llave_cerrada',
  'tk_condicional_else',
  'tk_iterativo_while',
  'tk_iterativo_do',
  'tk_reservda_void',
  'tk_reservada_return',
  'tk_igualacion',
  'tk_asignacion', 
  'tk_comentario_simple',
  'tk_division',
  'tk_dato_double',
  'tk_dato_tipo_Int',
  'tk_dato_char',
  'tk_dato_string',
  'tk_identificador',
) + tuple(reserved.values())

t_tk_tipo_int=r'int'
t_tk_tipo_double=r'double'
t_tk_tipo_string=r'string'
t_tk_tipo_char=r'char'
t_tk_tipo_boolean=r'boolean'
t_tk_suma=r'\+'
t_tk_resta=r'-'
t_tk_multiplicacion=r'\*'
t_tk_resto=r'%'
t_tk_diferenciacion=r'!='
t_tk_mayor_o_igual_que=r'>='
t_tk_mayor_que=r'>'
t_tk_menor_o_igual_que=r'<='
t_tk_menor_que=r'<'
t_tk_and=r'&&'
t_tk_or=r'\|\|'
t_tk_not=r'!'
t_tk_punto_coma=r';'
t_tk_condicional=r'if'
t_tk_par_abierto=r'\('
t_tk_par_cerrado=r'\)'
t_tk_llave_abierta=r'{'
t_tk_llave_cerrada=r'}'
t_tk_condicional_else=r'else'
t_tk_iterativo_while=r'while'
t_tk_iterativo_do=r'do'
t_tk_reservda_void=r'void'
t_tk_reservada_return=r'return'
t_tk_igualacion=r'=='
t_tk_boolean_true=r'true'
t_tk_boolean_false=r'false'
t_tk_asignacion=r'='
t_tk_division=r'/'

# Lexemas ignorados
t_ignore = ' \t\r'

"""
  t:
    - lineno: numero de linea
    - value: valor del lexema
    - type: nombre del token
"""
#Expresiones regulares para AFD

def t_tk_dato_double(t):
  r'\d+.\d\d*'
  if t.value in tokens: 
    t.type = t.value
  return t

def t_tk_dato_tipo_Int(t):
  r'\d+'
  if t.value in tokens: 
    t.type = t.value
  return t

def t_tk_identificador(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  if t.value in reserved.keys():
    t.type = reserved[t.value]
  return t

def t_tk_comentario_var_filas(t): 
  r'\/\*(.*\n*)*\*\/'
  if t.value in tokens: 
    t.type = t.value
  return t

def t_tk_comentario_simple(t):
  r'\/\/.*'
  if t.value in tokens: 
    t.type = t.value
  return t

def t_tk_dato_char(t):
  r'\'.{1}\''
  if t.value in tokens: 
    t.type = t.value
  return t

def  t_tk_dato_string(t):
  r'\".*\"'   # corregir no puede aceptar " dentro de las comillas del string
  if t.value in tokens: 
    t.type = t.value
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno+=len(t.value)

def t_error(t):
  print(t.lineno, getColumn(t), f"No se pudo reconocer el lexema '{t.value}'")
  t.lexer.skip(1)

lexer = lex()




#ANÁLISIS SINTÁCTICO



# precedence = (
#   ('left','operador_suma','operador_resta'),
#   ('left','operador_multiplicacion','operador_division','operador_resto')
# )

# """
# ASOCIATIVIDAD IZQUIERDA (left)
# ((5 + 5) + 5)
# ((5 ^ 5) ^ 5)
# ASOCIATIVIDAD DERECHA (right)
# (5 + (5 + 5))
# (5 ^ (5 ^ 5))
# """

# """
# p[0] : Lado izquierdo de la producción
# p[1+] : Lado derecho de la producción
# Lo que habrá en los elementos del lado derecho será:
# - Un token si es un símbolo terminal
# - Lo que regresemos de su producción si es un símbolo no terminal
# Para retornar algo de una producción se debe asignar a p[0]
# """

# # Producciones
# def p_INITIAL(p):
#   '''
#   INITIAL : reservada_inicio EXPRESSIONS reservada_fin
#   '''
#   p[0] = p[2]

# def p_EXPRESSIONS(p):
#   '''
#   EXPRESSIONS : EXPRESSIONS E
#               | E
#   '''
#   if len(p)==3:
#     p[0] = p[1]
#     p[0].append(p[2])
#   else:
#     p[0] = [p[1]]

# def p_E(p):
#   '''
#   E : E operador_suma E
#     | E operador_resta E
#     | E operador_multiplicacion E
#     | E operador_division E
#     | E operador_resto E
#     | id
#     | numero
#   '''
#   if len(p)==2:
#     p[0] = {"linea": p.lexer.lineno, "columna": getColumn(p.lexer), "valor": p[1]}
#   else:
#     p[0] = {"linea": p.lexer.lineno, "columna": getColumn(p.lexer), "operacion": p[2], "izquierda": p[1], "derecha": p[3]}

# def p_error(p):
#   print(p)
#   if p:
#     print(f"Sintaxis no válida cerca de '{p.value}' ({p.type})")
#   else:
#     print("Ninguna instrucción válida")



# parser = yacc(start='INITIAL')
# # lexer.lex(reflags=re.IGNORECASE)  # case insensitive

                           


#MENÚ
report_html=createHTML
print('\n','---------------------------------------------------', 'ANALIZADOR LÉXICO PARA SIMPLE C ','---------------------------------------------------')
print('MENÚ PRINCIPAL','\n')
contadorprocesos=0
while contadorprocesos>=0:
    print('\n')
    question1=input('¿Desea iniciar el análisis léxico?'+'\n'+'Responda: si o no'+'\n')
    print('\n')
    print('***************************************************')
    try:
        if question1=='si': 
            #SELECCIÓN DE ARCHIVOS
            list_files= os.listdir('C:/Users/Linda Quelex/Desktop/UNIVERSIDAD 2022/(3.1) LAB LFP/PROYECTOS/PROYECTO2/LFP-VJ-201403745-P2/PROYECTO2/ENTRADAS')
            print('\n')
            print('Archivos disponibles: ')
            for i in range(len(list_files)):
                print('Archivo ',i,':',list_files[i])
            print('\n')
            print('***************************************************')
            archivoseleccionado= input('----->Ingrese el nombre del archivo: ')
            print('\n')
            print('***************************************************')
            print('El archivo a analizar es: ', archivoseleccionado) 
            #filename=list_files[int(archivoseleccionado)]   
            file = open( './ENTRADAS/'+ archivoseleccionado, encoding='utf-8')
            content = file.read()
            INPUT=content.lower()
            print('\n')
            print('***************************************************')
            print('Finalizó la carga de archivos','\n')
            print('***************************************************')

            # ENVIAR CONTENIDO AL ANALIZADOR LÉXICO
            lexer.input(INPUT.lower())
            for tok in lexer:
              lista_tokens=list()
              lista_tokens.append(tok)
              print("lista de tokens",lista_tokens)
              # print(tok)
              dt = {
                    'tokens':lista_tokens}
            print("dict-------",dt)
              # print(lexer[tok])
              
            # #GENERAR REPORTE
            report_html=createHTML(dt)
    except: 
        print('\n','-------------------------------------')
        print('El archivo no existe intente de nuevo')
        print('\n','-------------------------------------')
    print('\n')
    salir=input('¿Desea intentar de nuevo?' +'\n'+'Responda: si o no'+'\n')
    if salir=='si':
        contadorprocesos+=1
    else: 
        salir=input('¿Desea salir de la aplicación?' +'\n'+'Responda: si o no'+'\n')
        if salir=='si':
            exit()
        else: 
            contadorprocesos+=1








