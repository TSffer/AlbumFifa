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

codigo=form.getfirst("codigo","empty")

"""
insertar = db.cursor()

for i in range (1 , 41):
  insertar.execute("insert into figurasAlbum values (null,%s,%s)",(i,str(i)+".png"))
db.commit()
"""

cursor = db.cursor()
cursor1 = db.cursor()
if(user!="empty"):
  query = "select id from usuarios where usuario = '%s' " % user
  cursor.execute(query)
  id_usuario = cursor.fetchall()

  id_u = id_usuario[0][0]
else:
  id_u=1;
  f=open("texto.txt")
  id_u=f.read()
  f.close()

  
queryt = "select * from paquetes where codigo = '%s' " % codigo
cursor.execute(queryt)
res_pack = cursor.fetchall()


queryS = "select nombreFigura , figurasAlbum.id from figurasAlbum join usuarios join figurasobtenidas on figurasAlbum.id = figurasobtenidas.id_figura and '%s' = figurasobtenidas.id_usuario  and figurasAlbum.id between 1 and 12 GROUP BY nombreFigura , figurasAlbum.id HAVING count(nombreFigura)>1 order by nombreFigura,figurasAlbum.id ASC " % id_u

cursor1.execute(queryS)
resultado = cursor1.fetchall()

#cursor = db.cursor()
#cursor.execute("select nombreFigura from figurasAlbum where id between 1 and 12" )
#resultado = cursor.fetchall()

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

  <body background="Sel/fondo.jpg">

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="#">%s"""%(user)+""" Obtener figuras:</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
    </nav>
    <div class="wrap">
      <form class="login">
        <input type="text" placeholder="Codigo" name="codigo"/>
        <input type="submit" value="Canjear" class="btn btn-success btn-sm" />
      </form>
    </div>            

    <!-- Page Content -->
    <div class="container">

      <h1 class="my-4 text-center text-lg-left"><font Size="35" color=#2E86C1><i><b>Figuras del paquete</b></i></font></h1>

      <div class="row text-center text-lg-left">""")

xs = []
xi = []

cont = 0

cursor2 = db.cursor()
ids_fig=[]
if(codigo!="empty"):
  for i in range(0,5):
    csql="select nombreFigura from figurasalbum where id = %s " % res_pack[i][2]
    cursor2.execute(csql)
    res = cursor2.fetchall()
    ids_fig.append(res[0][0])


if( not ids_fig ):
  xs.append('10000')
  xi.append(10000)

for i in range(0,len(ids_fig)):
  xs.append(ids_fig[i])
  xi.append(ids_fig[i])
  
for i in range(0,len(res_pack)):
  csql="insert into figurasobtenidas values(null,'%s','%s')" % (id_u,res_pack[i][2])
  cursor2.execute(csql)
  db.commit()
  print("""
        <div class="col-lg-3 col-md-4 col-xs-6">
          <a href="#" class="d-block mb-4 h-100">
            <img id="imagen_1" class="img-fluid img-thumbnail" src=""")
  if(not ids_fig):
    print("http://placehold.it/127x205")
  else:
    print("figuras/"+xs[cont])
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
<h3 class="my-7"><font Size="25" face = "Georgina" color=Gray>Paquete obtenido</font></h3>""")

if(codigo!="empty"):
  print("""

        <div class="row">
  """)

  print("""
          <div class="col-md-1 col-sm-6 mb-14">
            <a href="pagina.py">
              <img class="img-fluid" src=""")
    
  print("figuras/"+res_pack[0][3])
    
  print("""alt="">
            </a>
          </div>
    """)
  print("""
        </div>
  """)
cursor2.close()
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
if(user!="empty"):
  f=open("texto.txt","w")
  f.write(str(id_u)+"\n")
  
