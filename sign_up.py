#!C:\Python34\python
import cgi
import cgitb; cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='bdalbum')

form = cgi.FieldStorage() # se instancia solo una vez

nombre = form.getfirst('nombre', 'empty')
usuario = form.getfirst('usuario', 'empty')
password = form.getfirst('password', 'empty')
correo = form.getfirst('correo', 'empty')

if(usuario!="empty" and correo!="empty" and password!="empty" and nombre!="empty" ):
    insertar = db.cursor()
    insertar.execute("insert into usuarios values(2,'%s','%s','%s','%s')" % (nombre,usuario,password,correo))
    db.commit()
    print ("ID de ultimo registro insertado: %s<br>" % insertar.lastrowid)
    insertar.close()

print("""<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="utf-8">
	<title>document</title>
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximun-scale=1.0, minimun-scale=1.0">	
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="js/bootstrap.min.js"></script>
	<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <div class="pr-wrap">
                <div class="pass-reset">
                    <label>
                        Enter the email you signed up with</label>
                    <input type="email" placeholder="Email" />
                    <input type="submit" value="Submit" class="pass-reset-submit btn btn-success btn-sm" />
                </div>
            </div>
            <div class="wrap">
                <p class="form-title">
                    Registrarse</p>
                <form class="login2">
                <input type="nombre" placeholder="Nombre y Apellidos" name="nombre"/>
                <input type="username" placeholder="Username" name="usuario" />
                <input type="password" placeholder="Password" name="password"/>
                <input type="correo" placeholder="Correo" name="correo"/>
                <input type="submit" value="Registrarse" class="btn btn-success btn-sm" />
                
                </form>
            </div>
        </div>
    </div>
</div>
</body>

</html>

""")
db.close()
