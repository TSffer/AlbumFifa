#!C:\Python34\python

import cgi
import cgitb; cgitb.enable()
import mysql.connector
import re

print("Content-Type: text/html\n")

dato = {'user' : 'root',
        'password':'',
        'database':'bdalbum',
        'host':'127.0.0.1'}

db = mysql.connector.connect(** dato)
form = cgi.FieldStorage()

user = form.getfirst("user","empty")

"""
insertar = db.cursor()

for i in range (1 , 41):
  insertar.execute("insert into figurasAlbum values (null,%s,%s)",(i,str(i)+".png"))
db.commit()
"""

cursor = db.cursor()
cursor1 = db.cursor()

query = "select id from usuarios where usuario = '%s' " % user
cursor.execute(query)
id_usuario = cursor.fetchall()

id_u = id_usuario[0][0]
queryS = "select nombreFigura , figurasAlbum.id from figurasAlbum join usuarios join figurasobtenidas on figurasAlbum.id = figurasobtenidas.id_figura and '%s' = figurasobtenidas.id_usuario  and figurasAlbum.id between 52 and 64 GROUP BY nombreFigura , figurasAlbum.id HAVING count(nombreFigura)>1 order by nombreFigura,figurasAlbum.id ASC " % id_u

cursor1.execute(queryS)
resultado = cursor1.fetchall()


cursor.close()
cursor1.close()

print("""

<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Selecciones</title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/thumbnail-gallery.css" rel="stylesheet">

  </head>

  <body background="fondo.jpg">

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="#">Seleccion:</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="pagina3.py?user=%s"""%(user)+""" ">Prev
                <span class="sr-only">(current)</span>
              </a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="pagina5.py?user=%s"""%(user)+""" ">Next
                <span class="sr-only">(current)</span>
              </a>
            </li>

          </ul>
        </div>
      </div>
    </nav>

    <!-- Page Content -->
    <div class="container">

      <h1 class="my-4 text-center text-lg-left"><font Size="35" color=#2E86C1><i><b>Portugal</b></i></font></h1>

      <div class="row text-center text-lg-left">""")

xs = []
xi = []

if( not resultado ):
  xs.append('10000')
  xi.append(10000)

for i in range(0,len(resultado)):
  xs.append(resultado[i][0])
  xi.append(resultado[i][1])

cont = 0
for i in range(0,12):
  print("""
        <div class="col-lg-3 col-md-4 col-xs-6">
          <a href="#" class="d-block mb-4 h-100">
            <img id="imagen_1" class="img-fluid img-thumbnail" src=""")
  a = i
  if(a+52 != xi[cont]):
    print("http://placehold.it/127x205")
    
  else:
    print("../figuras/"+xs[cont]) 
    cont = cont + 1 
    if(cont >= len(xi)):
      cont = cont - 1
   
  print("""alt="">
          </a>
        </div>
  """)


print("""  
      </div>
    </div>
    <!-- /.container -->
    """)

print(""" 
<h3 class="my-7"><font Size="25" face = "Georgina" color=Gray>Figuras Disponibles</font></h3>

      <div class="row">
""")

for i in range (0,12):
  print("""
        <div class="col-md-1 col-sm-6 mb-14">
          <a href="pagina.py">
            <img class="img-fluid" src=""")
  if(i<len(resultado) and len(resultado) != 0):
    print("../figuras/"+resultado[i][0])
  else:
    print("http://placehold.it/127x205")
  
  print("""alt="">
          </a>
        </div>
  """)
print("""
      </div>
""")

print("""
<p class="text-center">
  <button type="reset" class="btn btn-info" style="margin-right: 20px;"><i class="zmdi zmdi-roller"></i> &nbsp;&nbsp; Limpiar</button>
  <button type="submit" class="btn btn-primary"><i class="zmdi zmdi-floppy"></i> &nbsp;&nbsp; Guardar</button>
</p>
""")

print("""
    
    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  </body>

</html>
""")