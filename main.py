from flask import Flask,request, render_template
from livereload import Server
from operaciones import sumar
from operaciones import division_piso


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("inicio.html")

@app.route("/suma")
def ruta_suma():
    numero1=request.args.get("numero1",type=float)
    numero2=request.args.get("numero2",type=float)
    if numero1 is None or numero2 is None:
        return "faltan datos"
    
    return f"el resultado de la suma es {sumar(numero1,numero2)}"



@app.route("/division_piso")
def ruta_dicision_piso():
    numero1=request.args.get("numero1",type=float)
    numero2=request.args.get("numero2",type=float)
    if numero1 is None or numero2 is None:
        return "faltan datos"
    
    return f"el resultado de la suma es {division_piso(numero1,numero2)}"



#if __name__=="__main__":
 #   app.run(debug=True)




if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()
