- [MANUAL TÉCNICO](#manual-técnico)
- [Proyecto](#proyecto)
- [Palabras clave](#palabras-clave)
- [Introducción](#introducción)
- [Desarrollo](#desarrollo)
  - [1. Archivos de entrada](#1-archivos-de-entrada)
  - [2. Ejemplo de código fuente](#2-ejemplo-de-código-fuente)
  - [3. LÉXICO](#3-léxico)
    - [3.1 Lexemas](#31-lexemas)
    - [3.2. Definición de tokens](#32-definición-de-tokens)
    - [3.3.  Análisis léxico](#33--análisis-léxico)
  - [4.  SINTÁCTICO](#4--sintáctico)
    - [4.1. Gramática de Simple C v2.0](#41-gramática-de-simple-c-v20)
      - [4.1.1. Alfabeto](#411-alfabeto)
      - [4.1.1.1. Símbolos terminales](#4111-símbolos-terminales)
      - [4.1.1.1.1. Expresiones regulares](#41111-expresiones-regulares)
      - [4.1.1.1.2. Palabras reservadas](#41112-palabras-reservadas)
      - [4.1.1.2. Símbolos no terminales](#4112-símbolos-no-terminales)
  - [1.2. Sintáxis](#12-sintáxis)
    - [1.2.1. Precedencia](#121-precedencia)
    - [1.2.2. Producciones](#122-producciones)
  - [7. Utilización de PLY para el análsis léxico y sintáctico](#7-utilización-de-ply-para-el-análsis-léxico-y-sintáctico)


# MANUAL TÉCNICO 
* UNIVERSIDAD DE SAN CARLOS DE GUATEMALA 
* Proyecto 1
* Laboratorio de Lenguajes Formales de Programación 
* Linda Madelin Fabiola Quelex Sep
* 201403745


# Proyecto
Analizador léxico de lenguaje Simple C v2.0

# Palabras clave

* Análisis léxico
* Análisis sintáctico
* Python
* HTML
* Tokens



# Introducción
El presente ensayo es sobre el proyecto 2 del 
Laboratorio de Lenguajes Formales de Programación, de la Facultad de Ingeniería, de la 
Universidad de San Carlos de Guatemala. 
El proyecto fue nombrado como “Analizador Léxico del Lenguajes Simple C v2.0".

Para la realización del proyecto se utilizó el lenguaje 
de programación Python y HTML para la generación de reportes. 

La aplicación permite la carga de un archivo con extensión (.sc) el cual brinda el código fuente a analizar por la apliación, al ser enviadO el contenido del archivo, el analizador retorna reportes con los resultados, a través del navegador. 

# Desarrollo

Para el desarrollo del proyecto 2 se desarrolló e implementó lo siguiente: 


## 1. Archivos de entrada
Se definió una carpeta para los almacenar los archivos de entrada, denominado "ENTRADAS".

## 2. Ejemplo de código fuente
Se desarrolló un código fuente como prueba y para la definición de tokens. A continuación se presenta: 


```Simple C
// comentario de una línea

/*
Comentario
De varias
Líneas
*/

Int _dato_int = 67;
Double Dato_double  =39.87;
String dato_String1= "Hola mundo";
Char _Dato_tipo__Char1 = 'a';
Boolean _ = true;
Boolean B= True;

if ( OPERACION ) {
INSTRUCCIONES
break;
} else {
INSTRUCCIONES
continue
}

// sentencia while
while ( OPERACION ) {
INSTRUCCIONES
}
// sentencia do-while
do {
INSTRUCCIONES
} while ( OPERACION ) ;


```

## 3. LÉXICO 
### 3.1 Lexemas
   
Con el código fuente de prueba se definireron los lexemas que acontinuación se listan:  


- // comentario 1 línea sdri0werw023"#"#" 
- /*línea 1 comentario
    línea 2 comentario"!"#
    línea 3 comentario
   */
- Int
- Double
- String
- Char
- Boolean
- \+
- \-
- \*
- /
- %
- ==
- !=
- \>
- \>=
- <
- <=
- &&
- ||
- !
- ;
- if 
- (
- dato1_
- _datos2
- )
- {
- }
- else
- while
- do
- void
- return
- break
- continue


### 3.2. Definición de tokens
   
Con los lexemas definidos de construyó la tabla de tokens, para Simple C

| Token                   | Descripción                          | Patrón                 |
| ----------------------- | ------------------------------------ | ---------------------- |
| comentario_simple       | Línea de comentario simple           | ^\/\/.*\n              |
| comentario_var_líneas   | Comentario de varias líneas          | \/\*.*\*\/             |
| tipo_int                | Tipo de dato entero                  | int                    |
| tipo_double             | Tipo de dato decimal                 | double                 |
| tipo_string             | Tipo de dato String                  | string                 |
| tipo_char               | Tipo de dato Char                    | char                   |
| tipo_boolean            | Tipo de dato boolean                 | boolean                |
| suma                    | Operador suma                        | +                      |
| resta                   | Operador resta                       | -                      |
| multiplicacion          | Operador multiplicación              | *                      |
| division                | Operador división                    | /                      |
| resto                   | Operador resto                       | %                      |
| igualacion              | Operador igualación                  | ==                     |
| signacion               | Operador de asignación               | =                      |
| diferenciacion          | Operador diferenciación              | !=                     |
| mayor_que               | Operador mayor que                   | >                      |
| mayor_o_igual_que       | Operador mayor o igual que           | >=                     |
| menor_que               | Operador menor que                   | <                      |
| menor_o_igual_que       | Operador menor o igual que           | <=                     |
| and                     | Operador and                         | &&                     |
| or                      | Operador or                          | \|\|                   |
| not                     | Operador not                         | !                      |
| punto_coma              | Punto y coma                         | ;                      |
| condicional             | Condicional                          | if                     |
| par_abierto             | Paréntesis abierto                   | (                      |
| par_cerrado             | Paréntesis cerrado                   | )                      |
| dato_tipo_Int           | Dato tipo Int                        | ^\d+$                  |
| dato_tipo_boolean_true  | Dato tipo boolean                    | true                   |
| dato_tipo_boolean_false | Dato tipo boolean                    | false                  |
| identificador           | Cualquier identificador del lenguaje | [a-zA-Z_][a-zA-Z0-9_]* |
| llave_abierta           | Llave abierta                        | {                      |
| llave_cerrada           | Llave cerrada                        | }                      |
| condicional_else        | Condicional else                     | else                   |
| iterativo_while         | Iteración con ciclo while            | while                  |
| iterativo_do            | Iteración con ciclo do while         | do                     |
| reservada_void          | Palabra reservada                    | void                   |
| reservada_return        | Retorno                              | return                 |
| dato_int                | Dato tipo entero                     | [0-9]+                 |
| dato_double             | Dato tipo double                     | [+-]?[0-9]*\.[0-9]+    |
| dato_string             | Datos tipo String                    | ".*"                   |
| dato_char               | Dato tipo char                       | '(.*){1}'              |
| continue                | continue                             | continue               |
| break                   | break                                | break                  |


### 3.3.  Análisis léxico

Con el código fuente de prueba, los lexemas y la tabla de tokens definidos se presenta un ejemplo de análisis léxico:

| Lexema                                                        | Token                 |
| ------------------------------------------------------------- | --------------------- |
| // comentario 1 línea sdri0werw023"#"#"                       | comentario_simple     |
| /*línea 1 comentario línea 2 comentario línea 3 comentario */ | comentario_var_líneas |
| Int                                                           | tipo_int              |
| Double                                                        | tipo_double           |
| String                                                        | tipo_string           |
| Char                                                          | tipo_char             |
| Boolean                                                       | tipo_boolean          |
| +                                                             | suma                  |
| -                                                             | resta                 |
| *                                                             | multiplicacion        |
| /                                                             | division              |
| %                                                             | resto                 |
| ==                                                            | igualacion            |
| !=                                                            | diferenciacion        |
| >                                                             | mayor_que             |
| >=                                                            | mayor_o_igual_que     |
| <                                                             | menor_que             |
| <=                                                            | menor_o_igual_que     |
| &&                                                            | and                   |
| \/\/                                                          | or                    |
| !                                                             | not                   |
| ;                                                             | punto_coma            |
| if                                                            | condicional           |
| (                                                             | par_abierto           |
| dato1_                                                        | identificador         |
| _datos2                                                       | identificador         |
| )                                                             | par_cerrado           |
| {                                                             | llave_abierta         |
| }                                                             | llave_cerrada         |
| else                                                          | condicional_else      |
| while                                                         | iterativo_while       |
| do                                                            | iterativo_do          |
| void                                                          | reservada_void        |
| (parametro,)*                                                 | parametro             |
| return                                                        | reservada_return      |
| continue                                                      | continue              |
| break                                                         | break                 |


## 4.  SINTÁCTICO

### 4.1. Gramática de Simple C v2.0

####  4.1.1. Alfabeto
####  4.1.1.1. Símbolos terminales
####  4.1.1.1.1. Expresiones regulares

| Token                   | Patrón                 |
| ----------------------- | ---------------------- |
| comentario_simple       | ^\/\/.*\n              |
| comentario_var_líneas   | \/\*.*\*\/             |
| tipo_int                | int                    |
| tipo_double             | double                 |
| tipo_string             | string                 |
| tipo_char               | char                   |
| tipo_boolean            | boolean                |
| suma                    | +                      |
| resta                   | -                      |
| multiplicacion          | *                      |
| division                | /                      |
| resto                   | %                      |
| igualacion              | ==                     |
| signacion               | =                      |
| diferenciacion          | !=                     |
| mayor_que               | >                      |
| mayor_o_igual_que       | >=                     |
| menor_que               | <                      |
| menor_o_igual_que       | <=                     |
| and                     | &&                     |
| or                      | \|\|                   |
| not                     | !                      |
| punto_coma              | ;                      |
| condicional             | if                     |
| par_abierto             | (                      |
| par_cerrado             | )                      |
| dato_tipo_Int           | ^\d+$                  |
| dato_tipo_boolean_true  | true                   |
| dato_tipo_boolean_false | false                  |
| identificador           | [a-zA-Z_][a-zA-Z0-9_]* |
| llave_abierta           | {                      |
| llave_cerrada           | }                      |
| condicional_else        | else                   |
| iterativo_while         | while                  |
| iterativo_do            | do                     |
| dato_int                | [0-9]+                 |
| dato_double             | [+-]?[0-9]*\.[0-9]+    |
| dato_string             | ".*"                   |
| dato_char               | '(.*){1}'              |
| continue                | continue               |
| break                   | break                  |


####  4.1.1.1.2. Palabras reservadas

| Token            | Patrón |
| ---------------- | ------ |
| reservada_void   | void   |
| reservada_return | return |

#### 4.1.1.2. Símbolos no terminales

| Token       | Descripción                                       |
| ----------- | ------------------------------------------------- |
| INITIAL     | Estado inicial de la sintáxis                     |
| EXPRESSIONS | Lista de expresiones separadas por salto de linea |
| E           | Cualquier expresión                               |



## 1.2. Sintáxis

### 1.2.1. Precedencia
Precedencia de operadores de más a menos:

| Precedencia | Operador                                   | Asociatividad |
| :---------: | ------------------------------------------ | ------------- |
|     11      | Agrupacion                                 | Ninguna       |
|     10      | Acceso a arreglo                           | Izquierda     |
|      9      | Llamada a función                          | Izquierda     |
|      8      | Negación unaria, not                       | Derecha       |
|      7      | Potencia                                   | Derecha       |
|      6      | Multiplicación, división, módulo           | Izquierda     |
|      5      | Suma, resta                                | Izquierda     |
|      4      | Menor, menor o igual, mayor, mayor o igual | Izquierda     |
|      3      | Igualación, diferenciación                 | Izquierda     |
|      2      | And                                        | Izquierda     |
|      1      | Or                                         | Izquierda     |


### 1.2.2. Producciones
```ru

Símbolo inicial = INITIAL

INITIAL : INSTRUCCIONES

INSTRUCCIONES : INSTRUCCIONES INSTRUCCIONES2
              | INSTRUCCIONES2

INSTRUCCIONES2 : tk_reservda_void tk_identificador tk_par_abierto tk_par_cerrado tk_llave_abierta tk_llave_cerrada 
                  |tk_reservda_void tk_par_abierto INSTRUCCIONES3 tk_par_cerrado tk_llave_abierta tk_llave_cerrada
                  |tk_reservda_void tk_identificador tk_par_abierto INSTRUCCIONES3 tk_par_cerrado tk_llave_abierta INSTRUCCIONES4 tk_llave_cerrada
                  |INSTRUCCIONES4

INSTRUCCIONES4 : INSTRUCCIONES4 INST5
            | INST5

INST5 : DECLARACION_VAR
        | ASIG


DECLARACION_VAR : DECLARACION_VAR DESCRIPCION
                | DESCRIPCION

DESCRIPCION : tk_dato_tipo_Int tk_identificador tk_asignacion tk_tipo_int tk_punto_coma
              | tk_dato_double tk_identificador tk_asignacion tk_tipo_double tk_punto_coma
              | tk_dato_string tk_identificador tk_asignacion tk_tipo_string tk_punto_coma
              | tk_dato_char tk_identificador tk_asignacion tk_tipo_char tk_punto_coma
              | tk_tipo_boolean tk_identificador tk_asignacion tk_boolean_true tk_punto_coma
              | tk_tipo_boolean tk_identificador tk_asignacion tk_boolean_false tk_punto_coma

ASIG : ASIG DESCRIPCION_2
      | DESCRIPCION_2


DESCRIPCION_2 :  tk_identificador tk_asignacion tk_tipo_int tk_punto_coma
              | tk_identificador tk_asignacion tk_tipo_double tk_punto_coma
              | tk_identificador tk_asignacion tk_tipo_string tk_punto_coma
              | tk_identificador tk_asignacion tk_tipo_char tk_punto_coma
              | tk_identificador tk_asignacion tk_boolean_true tk_punto_coma
              | tk_identificador tk_asignacion tk_boolean_false tk_punto_coma              



INSTRUCCIONES3 : INSTRUCCIONES3  tk_punto_coma DESCRIPCION_3
            | DESCRIPCION_3


DESCRIPCION_3 : tk_dato_tipo_Int tk_identificador
        | tk_dato_string tk_identificador





VERSIÓN 2


INITIAL : INSTRUCCIONES

INSTRUCCIONES : INSTRUCCIONES INSTRUCCIONES2
              | INSTRUCCIONES2

INSTRUCCIONES2 : METODOS
               | FUNCIONES
               | OTROS

METODOS : METODOS METODO
          | METODO 

METODO: METHOD_VOID ID LPAREN RPAREN LKEY empty RKEY 
               | METHOD_VOID ID LPAREN RPAREN LKEY SENTENCES_METHOD RKEY
               | METHOD_VOID ID LPAREN L_PARAMS RPAREN LKEY empty RKEY
               | METHOD_VOID ID LPAREN L_PARAMS RPAREN LKEY SENTENCES_METHOD RKEY


SENTENCES_METHOD : SENTENCES_METHOD SENTENCE_METHOD
                | SENTENCE_METHOD


SENTENCE_METHOD : DECLARATIONS
                | ASSIGNMENTS
                | SENTENCES_IF
                | METHOD_RETURN DOT_AN_DCOMMA

 FUNTIONS : FUNTIONS FUNTION
                | FUNTION 

 FUNTION : TYPE_INT COUPLER
                | TYPE_DOUBLE COUPLER
                | TYPE_STRING COUPLER
                | TYPE_CHAR COUPLER
                | TYPE_BOOL COUPLER


 COUPLER : ID LPAREN RPAREN LKEY empty RKEY 
                | ID LPAREN RPAREN LKEY SENTENCES_FUNTION RKEY
                | ID LPAREN L_PARAMS RPAREN LKEY empty RKEY
                | ID LPAREN L_PARAMS RPAREN LKEY SENTENCES_FUNTION RKEY


SENTENCES_FUNTION : SENTENCES_FUNTION SENTENCE_FUNTION
                          | SENTENCE_FUNTION


SENTENCE_FUNTION : DECLARATIONS
                         | ASSIGNMENTS
                         | METHOD_RETURN TYPE_DATO DOT_AN_DCOMMA
                         | METHOD_RETURN ID DOT_AN_DCOMMA

SENTENCES_IF : SENTENCES_IF SENTENCE_IF
              | SENTENCE_IF


SENTENCE_IF : CONDITIONAL_IF LPAREN OPTIONS RPAREN LKEY SENTENCES RKEY


OPTIONS : OPTIONS OPTION
                | OPTION


OPTION : OPTION IQUALS OPTION
               | OPTION DIFFERENT OPTION
               | OPTION IQUAL_GREATER OPTION
               | OPTION IQUAL_LESS OPTION
               | OPTION AND OPTION
               | OPTION OR OPTION
               | OPTION NOT OPTION
               | OPTION GREATER OPTION
               | OPTION LESS OPTION
               | ID
               | TYPE_DATO



SENTENCES : SENTENCES SENTENCE
                  | SENTENCE


 SENTENCE : DECLARATIONS
                 | ASSIGNMENTS

DECLARATIONS : DECLARATIONS DECLARATION
                     | DECLARATION


DECLARATION : TYPE_INT ID IQUAL INT DOT_AN_DCOMMA
                    | TYPE_DOUBLE ID IQUAL FLOAT DOT_AN_DCOMMA
                    | TYPE_STRING ID IQUAL STRING DOT_AN_DCOMMA
                    | TYPE_CHAR ID IQUAL CHAR DOT_AN_DCOMMA
                    | TYPE_BOOL ID IQUAL DATA_BOOL DOT_AN_DCOMMA
```




## 7. Utilización de PLY para el análsis léxico y sintáctico 

* PLY: es una implementación de Python puro de las populares herramientas de construcción de compiladores lex y yacc. Admite el análisis sintáctico LALR(1), y proporciona una amplia validación de entrada, informes de errores y diagnósticos.

* lex.py: se usa para tokenizar una cadena de entrada. La identificación de tokens generalmente se realiza escribiendo una serie de reglas de expresión regular. Para el proyecto se utilizaron las siguientes expresiones regulares: 

  | Clave                     | Expresion Regular      |
  | ------------------------- | ---------------------- |
  | t_tk_dato_double          | \d+\.\d\d*             |
  | t_tk_dato_tipo_Int        | \d+                    |
  | t_tk_identificador        | [a-zA-Z_][a-zA-Z_0-9]* |
  | t_tk_comentario_var_filas | \/\*(.*\n*)*\*\/       |
  | t_tk_comentario_simple    | \/\/.*                 |
  | t_tk_dato_char            | \'.{1}\'               |
  | t_tk_dato_string          | \".*\"                 |

Ejemplo de implementación: 

```
def t_tk_dato_double(t):
  r'\d+\.\d\d*'
  if t.value in tokens: 
    t.type = t.value
    
  return t

def t_tk_dato_tipo_Int(t):
  r'\d+'
  if t.value in tokens: 
    t.type = t.value
  return t
```

* yacc.py: se utiliza para analizar la sintaxis del lenguaje, la sintaxis generalmente se especifica en términos de una gramática BNF. Por ejemplo, si quisiera analizar expresiones aritméticas simples, primero podría escribir una especificación gramatical inequívoca, ejemplo de implementación: 
  
```
def p_INSTRUCCIONES2(p):
  '''
  INSTRUCCIONES2 : tk_reservda_void tk_identificador tk_par_abierto tk_par_cerrado tk_llave_abierta tk_llave_cerrada 
                  |tk_reservda_void tk_par_abierto INSTRUCCIONES3 tk_par_cerrado tk_llave_abierta tk_llave_cerrada
                  |tk_reservda_void tk_identificador tk_par_abierto INSTRUCCIONES3 tk_par_cerrado tk_llave_abierta INSTRUCCIONES4 tk_llave_cerrada
                  |INSTRUCCIONES4
```



