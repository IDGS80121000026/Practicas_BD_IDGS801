from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,TelField,IntegerField, DateField,SelectField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    nombre= StringField('nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa nombre valido')
    ])
    apaterno= StringField('apaterno',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa apellido valido')
    ])
    amaterno= StringField('amaterno',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa apellido valido')
    ])
    email= EmailField('email',[
        validators.Email(message='Ingresa un correo valido')
    ])
    edad= IntegerField('edad',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa una edad valida')
    ])
    
class UserForm2(Form):
    
    id=IntegerField('id',[validators.number_range(min=4,max=20, message='Ingresa nombre valido')])
    nombre= StringField('nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa nombre valido')
    ])
    direccion= StringField('direccion',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa apellido valido')
    ])
    telefono= StringField('telefono',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa apellido valido')
    ])
    email= EmailField('email',[
        validators.Email(message='Ingresa un correo valido')
    ])
    sueldo= IntegerField('sueldo',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa apellido valido')
    ])
    
class UserForm3(Form):
    
    id=IntegerField('id'#,[validators.number_range(min=4,max=20, message='Ingresa nombre valido')]
                    )
    
    nombre= StringField('Nombre'#,[
        #validators.DataRequired(message='El campo es requerido'),
        #validators.length(min=4,max=10, message='Ingresa nombre valido')
    #]
    )
    direccion= StringField('Direccion'#,[
        #validators.DataRequired(message='El campo es requerido'),
        #validators.length(min=4,max=10, message='Ingresa apellido valido')
    #]
    )
    telefono= StringField('Telefono'#,[
        #validators.DataRequired(message='El campo es requerido'),
        #validators.length(min=4,max=10, message='Ingresa apellido valido')
    #]
    )
    tamanio= EmailField('Tamaño')
    ingredientes= IntegerField('ingredientes')
    numPizza= IntegerField('Num.Pizza'#,[
        #validators.DataRequired(message='El campo es requerido')
    #]
    )
    fechaV= DateField('Fecha')

class UserBus(Form):
    tipo=SelectField('Dia'#,[
        #validators.DataRequired(message='El campo es requerido')
        #]
        )
    