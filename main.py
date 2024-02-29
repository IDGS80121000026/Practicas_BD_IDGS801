from flask import Flask,render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig

#variables globales 

from flask import g
from models import db
from  models import Empleados #imortar esto que se encunetra en models 

import forms


app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
#proceso de configuracion
csrf=CSRFProtect()
#por que queremos trabajar con ese

@app.route("/index",methods=['GET','POST'])
def index():
    create_from = forms.UserForm2(request.form)
    if request.method=='POST':
    
        try:
                emple = Empleados(nombre=create_from.nombre.data, direccion=create_from.direccion.data, telefono=create_from.telefono.data, email=create_from.email.data, sueldo=create_from.sueldo.data)
                db.session.add(emple)                    
                db.session.commit()
        except Exception as e:
                print(f"Error en la base de datos: {e}")
                db.session.rollback()
    return render_template('index.html', form=create_from)


@app.route("/empleado",methods=["GET","POST"])
def empleado():
    emple_form=forms.UserForm2(request.form)
    empleado=Empleados.query.all()
    return render_template("empleados.html",empleado=empleado)

if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)# indicar que se crea la estructura de la tabla
                    # si no esta se cea y si esta solo se inicia osi 
    
    with app.app_context():
        db.create_all()
    app.run() 