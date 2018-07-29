#!C:\Python34\python
import cgi
import cgitb; cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

form = cgi.FieldStorage() # se instancia solo una vez
buscar = form.getfirst('buscar', 'empty')
db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='bdalbum')


form = cgi.FieldStorage() # se instancia solo una vez
usuario= form.getfirst('usuario', 'empty')
password= form.getfirst('password', 'empty')

cursor=db.cursor()
if (usuario!='empty'):
    sql="Select * From usuarios where usuario='%s'" % (usuario)
    cursor.execute(sql)
    resultado=cursor.fetchall()
else:
    resultado=""
cursor.close()  


print("""
<!DOCTYPE html>
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
                    Sign In</p>
                <form class="login">
                <input type="text" placeholder="Username" name="usuario"/>
                <input type="password" placeholder="Password" name="password"/>
                <input type="submit" value="Sign In" class="btn btn-success btn-sm" />
                <div class="remember-forgot">
                    <div class="row">
                        <div class="col-md-6">
                            <div class="checkbox">
                                <label>
                                    <input type="checkbox" />
                                    Remember Me
                                </label>
                            </div>
                        </div>
                        <div class="col-md-6 forgot-pass-content">
                            <a href="javascription:void(0)" class="forgot-pass">Forgot Password</a>
                        </div>
                    </div>
                </div>
                </form>
            </div>
        </div>
    </div>
</div>
<a href="sign_up.py" class="button" style="text-decoration:none; font-size: 24px; color: #FFF;margin-top: 30px">REGISTRARSE</a>
</body>

</html>
""")

if (resultado!=""):
    for registro in resultado:
        resultado=resultado;
    if(registro[2]==password):
        print("""
        <h1>que caraasdbshf </h1>
        <META HTTP-EQUIV="REFRESH" CONTENT="0;URL=main_page/index.py?user=%s"""%(registro[2])+""" ">  
        """) #en esta parte esta lo que te decia donde veas pagina.py?user=%s o algo asi es para pasar parametros a una nueva pagina #


db.close()
