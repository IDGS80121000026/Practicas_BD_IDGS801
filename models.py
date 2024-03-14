from flask_sqlalchemy import SQLAlchemy

import datetime

db=SQLAlchemy() #instancia 


class Pizas(db.Model):
    __tablename__='venta'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    telefono=db.Column(db.String(12))
    tamanio=db.Column(db.String(20))
    ingredientes=db.Column(db.String(100))
    numPizza=db.Column(db.Integer)
    precio=db.Column(db.Double)
    fechaV=db.Column(db.Date)
    
class Deta (db.Model):
    __tablename__='detalle'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    precio=db.Column(db.Double)
    fechaV=db.Column(db.Date)
    
    
    #se genera la estructura para la tabla 
