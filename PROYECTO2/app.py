from os import startfile
import os
from analizador_ply import Lexico
from crearhtml import  createHTML
from ply.ply.lex import lex

lexico= Lexico()

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
            content2=content.lower()
            print('\n')
            print('***************************************************')
            print('Finalizó la carga de archivos','\n')
            print('***************************************************')
            # ENVIAR CONTENIDO AL ANALIZADOR LÉXICO
            lexer = lex()
            lexer.input(content2)
            # for tok in lexer:
            #     print(tok)
            # contenido = lexico.analizador(content2) 
            # b=Lexico2()
            # contenido=b.analizador(content2)
            # #GENERAR REPORTE
            # report_html=createHTML(contenido)
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