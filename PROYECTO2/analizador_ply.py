from ply.ply.yacc import yacc
from ply.ply.lex import lex

def getColumn(t):
  line_start = INPUT.rfind('\n', 0, t.lexpos) + 1
  return (t.lexpos-line_start)+1

# Tokens

reserved = (
  'reservada_ini',
  'reservada_fin'
)

tokens = reserved + (
  
  'numero',
  'id',

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
  'tk_boolean_true',
  'tk_boolean_false',
  'tk_asignacion', 
  'tk_comentario_simple',
  'tk_division',
  'tk_dato_double',
  'tk_dato_tipo_Int',
  'tk_dato_char',
  'tk_dato_string',
  'tk_identificador',
)

t_reservada_ini = r'INICIO'
t_reservada_fin = r'FIN'
t_numero = r'\d+'

#LEXEMAS DEL PROYECTO, AUN FALTA AGREGAR LO NUEVO
# t_tk_comentario_var_filas=r'' #falta
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
# t_tk_comentario_simple=r'' #falta
t_tk_division=r'/'
# t_tk_dato_double=r''       #falta
# t_tk_dato_tipo_Int=r''  #falta
# t_tk_dato_char=r'' #falta
# t_tk_dato_string=r'' #falta
t_tk_identificador=r'[a-zA-Z_][a-zA-Z0-9_]*' #falta


# Lexemas ignorados
t_ignore = ' \t\r\n'


"""
  t:
    - lineno: numero de linea
    - value: valor del lexema
    - type: nombre del token
"""

def t_id(t): # t_id
  r'[a-zA-Z_][a-zA-Z_0-9]*'

  if t.value in reserved: t.type = t.value

  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno+=len(t.value)

def t_error(t):
  print(t.lineno, getColumn(t), f"No se pudo reconocer el lexema '{t.value}'")
  t.lexer.skip(1)

lexer = lex()

INPUT = r'''
INICIO
56*9-5/2552
FIN
int
double
string
char
boolean
+ - * % != >= > <= <
&& 
|| ! ; if (){} else while do void  
return == true false  === /

hola
'''

lexer.input(INPUT)

for tok in lexer:
  print(tok)