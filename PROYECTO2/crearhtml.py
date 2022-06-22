from os import startfile


def createHTML(contenido):
    file_exit = input('----->Ingrese el nombre del archivo de salida: ')
    print('\n')
    file = open('P1/tabla_tokens/table-03/{}.html'.format(file_exit),
                'w+', encoding='utf-8')
    
    #ESTRUCTURA HTML
    body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
	<link href='https://fonts.googleapis.com/css?family=Roboto:400,100,300,700' rel='stylesheet' type='text/css'>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" href="css/style.css">
    <title>{file_exit}</title>
</head>"""

    body = body + f"""
<body>
    """
#TABLA DE TOKENS
    body = body + f"""
	<section class="ftco-section">
		<div class="container">
			<div class="row justify-content-center">
				<div class="col-md-6 text-center mb-5">
					<h2 class="heading-section">Reporte de Tokens</h2>
				</div>
			</div>
    """
    
    body = body + f"""
            <div class = "row" >
                <div class = "col-md-12" > 
                    <div class = "table-wrap" >
                        <table class = "table" >
                            <thead class="thead-primary">
                            <tr>
                                <th> Linea </th>
                                <th> Columna</th>
                                <th> Lexema</th>
                                <th> Token </th>
                                <th> Patron </th>
                            </tr>
                            </thead>
    """

    body = body + f"""
                            <tbody>
    """
    	
    # ? Contenido BODY HTML
    tokens = contenido["tokens"]

    for dato in tokens:
        body = body + f"""      <tr >
                                    <td>{dato.row}</td>
                                    <td>{dato.col}</td>
                                    <td>{dato.lexema}</td>
                                    <td>{dato.token}</td>
                                    <td>{dato.patron}</td>
                                </tr>"""

    body = body + f"""
                            </tbody>
                        </table>
                    </div>
				</div>
			</div>
		</div>
	</section>
    """		

#TABLA DE ESTADOS
    if contenido['estados']:
        body = body + f"""
        <section class="ftco-section">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-md-6 text-center mb-5">
                        <h2 class="heading-section">Reporte de Estados</h2>
                    </div>
                </div>
        """
        estados = contenido['estados']
        for dato2 in estados:
            body = body + f"""
                <div class = "row" >
                    <div class = "col-md-12" > 
                        <div class = "table-wrap" >
                            <table class = "table" >
                                <thead class="thead-primary">
                                <tr>
                                    <th> Estado </th>
                                    <th> Caracter </th>
                                    <th> Lexema reconocido</th>
                                    <th> Siguiente estado </th>
                                </tr>
                                </thead>
            """

            body = body + f"""
                                <tbody>
            """
            
        #Contenido BODY HTML

            for x in dato2.estados:
                body = body + f"""   
                                    <tr >"""
                for y in x:
                    body = body + f""" 
                                        <td> {y} </td>
                                        """
                body = body + f"""                       
            
                                    </tr>"""

            body = body + f"""
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            """		





    #TABLA DE ERRORES
    body = body + f"""
	<section class="ftco-section">
		<div class="container">
			<div class="row justify-content-center">
				<div class="col-md-6 text-center mb-5">
					<h2 class="heading-section">Reporte de Errores</h2>
				</div>
			</div>
    """
    
    body = body + f"""
            <div class = "row" >
                <div class = "col-md-12" > 
                    <div class = "table-wrap" >
                        <table class = "table" >
                            <thead class="thead-primary">
                            <tr>
                                <th> Linea </th>
                                <th> Columna</th>
                                <th> Lexema</th>

                            </tr>
                            </thead>
    """

    body = body + f"""
                            <tbody>
    """
    	









    # ? Contenido BODY HTML
    errores = contenido["errores"]

    for dato3 in errores:
        body = body + f"""      <tr >
                                    <td>{dato3.row}</td>
                                    <td>{dato3.col}</td>
                                    <td>{dato3.lexema}</td>

                                </tr>"""

    body = body + f"""
                            </tbody>
                        </table>
                    </div>
				</div>
			</div>
		</div>
	</section>
    """		

#FIN DE LA TABLA 
  
    body = body + f"""
    <script src="js/jquery.min.js"></script>
    <script src="js/popper.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/main.js"></script>
</body>
    """
    
    body = body + f"""
</html>"""

    file.write(body)
    file.close()

    index = 'P1\\tabla_tokens\\table-03\\{}.html'.format(file_exit)

    startfile(index)

# createHTML(["=", "igual", "1","1"])