from operator import truediv

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro
        descuento = 0

        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0
        total_pagar = total_sin_descuento - descuento

        return render_template('ejercicio1.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               descuento=descuento,
                               total_pagar=total_pagar,
                               calculado=True)
    return render_template('ejercicio1.html', calculado=False)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']

        if usuario =="juan" and contrasenia =="admin":
            mensaje = "Bienvenido administrador juan"
        elif usuario =="pepe" and contrasenia =="user":
            mensaje = "Bienvenido usuario Pepe"
        else:
            mensaje = "El usuario o contraseña no es valido"

    return render_template('ejercicio2.html', mensaje=mensaje)
if __name__ == '__main__':
    app.run(debug=True)