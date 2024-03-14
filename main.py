from flask import Flask,render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig

#variables globales 

from flask import g
from datetime import datetime,timedelta
from models import db

from models import Pizas,Deta
from sqlalchemy import func

import forms
lista_de_pizzas =[]

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
#proceso de configuracion
csrf=CSRFProtect()
#por que queremos trabajar con ese

'''@app.route("/index",methods=['GET','POST'])
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
    return render_template('index.html', form=create_from)'''


'''@app.route("/empleado",methods=["GET","POST"])
def empleado():
    emple_form=forms.UserForm2(request.form)
    empleado=Empleados.query.all()
    return render_template("empleados.html",empleado=empleado)

'''

'''@app.route("/pizzeria",methods=['GET','POST'])
def pizzeria():
    create_from = forms.UserForm3(request.form)
    if request.method=='POST':
    
        try:
                pizz = Pizas(nombre=create_from.nombre.data, direccion=create_from.direccion.data, 
                             telefono=create_from.telefono.data, tamanio=create_from.tamanio.data, 
                             ingredientes=create_from.ingredientes.data, numPizza=create_from.numPizza.data,
                             fechaV=create_from.fecha.data)
                db.session.add(pizz)                    
                db.session.commit()
        except Exception as e:
                print(f"Error en la base de datos: {e}")
                db.session.rollback()
    return render_template('pizzeria.html', form=create_from)'''
from flask import render_template, request

from flask import request
from datetime import datetime

@app.route("/pizzeria", methods=['GET', 'POST'])
def pizzeria():
    create_from = forms.UserForm3(request.form)
    bus_form = forms.UserBus(request.form)

    print(f"btnO: {request.form.get('btnO')}")
    if request.method == 'POST':
        if 'btnO' in request.form:
            if request.form['btnO'] == '0':
                # Código para agregar una pizza
                ingredientes_seleccionados = []
                if 'jamon' in request.form:
                    ingredientes_seleccionados.append('Jamon')
                if 'pinia' in request.form:
                    ingredientes_seleccionados.append('Piña')
                if 'cham' in request.form:
                    ingredientes_seleccionados.append('Champiñones')
                  
                pizz = Pizas(
                    nombre=create_from.nombre.data,
                    direccion=create_from.direccion.data,
                    telefono=create_from.telefono.data,
                    tamanio=create_from.tamanio.data,
                    ingredientes=", ".join(ingredientes_seleccionados),
                    numPizza=create_from.numPizza.data,
                    fechaV=create_from.fechaV.data
                )
                
                
                
                
                # Calcular el subtotal utilizando la función calcular_subtotal
                subtotal = calcular_subtotal(
                    pizz.tamanio, pizz.numPizza, pizz.ingredientes.split(','))
                
                

                # Asignar el subtotal a un atributo de la instancia de la pizza
                pizz.subTotal = subtotal

                # Agregar la instancia de pizz a la lista de pizzas
                lista_de_pizzas.append(pizz)

                # Ahora renderizamos la plantilla y pasamos la lista de pizzas y el subtotal
                # para que la plantilla pueda mostrar todos los detalles
                return render_template('pizzeria.html', form=create_from, pizza=lista_de_pizzas, subtotal=subtotal)
            if request.form['btnO'] == '1':
                # Código para eliminar campos seleccionados
                pizza_id = request.form.get('eli')
                eliminar_pizza(pizza_id)
                return render_template('pizzeria.html', form=create_from, pizza=lista_de_pizzas)
                
        
            elif request.form['btnO'] == '2':
                # Código para terminar la compra
                try:
                    total_precio = sum(pizza.subTotal for pizza in lista_de_pizzas)
                    
                    detalle = Deta(
                        nombre=lista_de_pizzas[0].nombre,  # Tomar el nombre de la primera pizza en la lista
                        precio=total_precio,
                        fechaV=lista_de_pizzas[0].fechaV
                        )
                    
                    print(detalle)
                    db.session.add(detalle)
                    for pizza in lista_de_pizzas:
                        pizz = Pizas(
                            nombre=pizza.nombre,
                            direccion=pizza.direccion,
                            telefono=pizza.telefono,
                            tamanio=pizza.tamanio,
                            ingredientes=pizza.ingredientes,
                            numPizza=pizza.numPizza,
                            fechaV=pizza.fechaV,
                            precio=pizza.subTotal
                        )
                        db.session.add(pizz)
                        
                        
                    db.session.commit()
                    lista_de_pizzas.clear()  # Limpiar la lista después de guardar en la base de datos
                    flash("Pedido finalizado exitosamente", "success")
                    return render_template('pizzeria.html')
                except Exception as e:
                    db.session.rollback()
                    return render_template('pizzeria.html', form=create_from)
            
            elif request.form['btnO'] == '3':
                # Código para obtener ventas del mes seleccionado
                fechaV = request.form.get('tipo')  # Obtener la fecha del formulario

                ventas_dia_actual, total_ventas_mes = ventas_por_fecha(fechaV)
                return render_template('pizzeria.html', form=create_from, pizza=lista_de_pizzas, ventas_dia_actual=ventas_dia_actual, total_ventas_mes=total_ventas_mes)
        else:
            # Si no hay un valor 'btnO' en el formulario, renderiza el formulario vacío
            return render_template('pizzeria.html', form=create_from, pizza=lista_de_pizzas)

    else:
        # Si el método de la solicitud no es POST, simplemente renderiza el formulario vacío
        return render_template('pizzeria.html', form=create_from, pizza=lista_de_pizzas)


from datetime import datetime
from sqlalchemy import func

def ventas_por_fecha(fechaV):
    # Asumimos que 'fechaV' es una cadena que representa un día de la semana o un mes
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    ventas = []  # Lista para almacenar las ventas

    # Obtener el número correspondiente al día de la semana
    dia_numero = None
    if fechaV.lower() in dias:
        dia_numero = dias.index(fechaV.lower())

    # Obtener el número correspondiente al mes
    mes_numero = datetime.now().month
    if fechaV.lower() in mes:
        mes_numero = mes.index(fechaV.lower()) + 1

    try:
        # Filtrar las ventas por día o mes
        if dia_numero is not None:
            # Filtrar por día de la semana
            
            ventas = Deta.query.filter(func.weekday(Deta.fechaV) == dia_numero).all()
            print(f"Ventas del día actual: {ventas}")
        else:
            # Filtrar por mes
            ventas = Deta.query.filter(func.month(Deta.fechaV) == mes_numero).all()
            print(f"Ventas del mes actual: {ventas}")

        # Calcular la suma total de ventas para el mes
        total_ventas_mes = sum(venta.precio for venta in ventas)
        
        # Crear una lista de tuplas con los datos de las ventas para el día actual
        ventas_dia_actual = [(venta.nombre, venta.precio) for venta in ventas]
        print(f"Ventas del día actual: {ventas_dia_actual}")

    except Exception as e:
        print(f"Error al obtener las ventas: {e}")
        ventas_dia_actual = []  # En caso de error, devolver una lista vacía
        total_ventas_mes = 0    # Total de ventas igual a 0 en caso de error

    print(f"Ventas del día actual: {ventas_dia_actual}")
    print(f"Total de ventas del mes: {total_ventas_mes}")

    #converir a un array de diccionarios ventas_dia_actual
    ventas_dia_actual = [{'nombre': venta[0], 'precio': venta[1]} for venta in ventas_dia_actual]
    print(f"Ventas del día actual: {ventas_dia_actual}")

    return ventas_dia_actual, total_ventas_mes





def calcular_subtotal(tamanio, cantidad, ingredientes):
    costo1 = 0  # Inicializar costo1
    if tamanio == 'Chica':
        costo1 = 40 
    elif tamanio == 'Mediana':
        costo1 = 80 
    elif tamanio == 'Grande':
        costo1 = 120
    
    costo_ingredientes = 0
    if 'Jamon' in ingredientes:
        costo_ingredientes += 10
    if 'Piña' in ingredientes:
        costo_ingredientes += 10
    if 'Champiñones' in ingredientes:
        costo_ingredientes += 10
        
        
    print(f'costo_ingredientes: {costo_ingredientes}')
    # Calcular el subtotal sumando el costo base y el costo de los ingredientes
    subtotal = (costo1 + (len(ingredientes)*10)) * cantidad
    return subtotal


def eliminar_pizza(pizza_id):
    print(f"Hola: {pizza_id is not None:}")
    try:
        if pizza_id is not None:
            pizza_id = int(pizza_id)
            print(lista_de_pizzas.pop(int(pizza_id)))
            flash("Pizza eliminada correctamente", "success")
        else:
            flash("No se proporcionó un ID de pizza válido", "error")
    except Exception as e:
        flash(f"Error al eliminar la pizza: {str(e)}", "error")

if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)# indicar que se crea la estructura de la tabla
                    # si no esta se cea y si esta solo se inicia osi 
    
    with app.app_context():
        db.create_all()
    app.run() 