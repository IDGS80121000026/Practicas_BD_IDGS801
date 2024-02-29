from flask_sqlalchemy import SQLAlchemy

import datetime

db=SQLAlchemy() #instancia 


class Empleados(db.Model):
    __tablename__='empelados'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    telefono=db.Column(db.String(12))
    email=db.Column(db.String(50))
    sueldo=db.Column(db.Integer)

    
    #se genera la estructura para la tabla 
