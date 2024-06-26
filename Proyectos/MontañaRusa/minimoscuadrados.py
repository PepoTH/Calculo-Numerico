import api
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
#Funcion que calcula los coeficiente de la regresion
def calculo_coeficiente(xi,yi):
    coef = np.polyfit(xi,yi,3)
    return coef
#Funcion que evalua el polinomio y devuelve los valores previstos
def evaluacion_polinomio(poli,xi):
    eval = np.polyval(poli,xi)
    return eval
#Funcion que devuelve el polinomio en una expresion
def polinomio(coef):
    X = sym.symbols("x")
    funcion = coef[0]*(X**3) + coef[1]*(X**2) + coef[2]*(X) + coef[3]
    return funcion
#Funcion que calcula el error de la regresion
def calculo_error(eval,yi):
    st = sum((yi - eval)**2)
    te = (len(yi) - 1)*np.var(yi)
    r23 = 1-st/te
    return r23

#Funcion que realiza la grafica de la regresion 
def grafica_regresion(eval,coef,xi,yi):
    x_valor = np.linspace(xi[0],xi[-1],100)
    y_valor = np.polyval(coef,x_valor)  
    plt.plot(xi,yi, "o", label="Puntos")
    plt.plot(xi,eval,"*",label="Error")
    plt.plot(x_valor,y_valor)
    plt.title('Polinomio de minimos al cuadrado, Regresion Cubica')
    plt.xlabel('xi')
    plt.ylabel('px(xi)')
    plt.legend()
    plt.show()

#API
x,y = api.datos2()

x = x.strip('][').split(',')
for i in range(len(x)): x[i] = float(x[i])

y = y.strip('][').split(',')
for i in range(len(x)): y[i] = float(y[i])

coef = calculo_coeficiente(x,y)
eval = evaluacion_polinomio(coef,x)
funcion = polinomio(coef)
print("El polinomio de la regresion es: ", str(funcion))
errorRegre = calculo_error(eval,y)
print("El error de la regresion es: " , str(errorRegre))

grafica_regresion(eval,coef,x,y)