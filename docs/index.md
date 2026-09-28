# Cuadratura Gaussiana

## Introducción

La integración numérica permite aproximar el valor de una integral definida mediante métodos computacionales. Estos métodos son especialmente útiles cuando una integral no puede resolverse fácilmente de forma analítica o cuando se requiere obtener una solución numérica.

En este proyecto se implementa el método de **cuadratura de Gauss-Legendre** utilizando Python y la biblioteca NumPy. El método permite aproximar una integral mediante una suma ponderada de los valores de una función evaluados en determinados puntos del intervalo de integración.

Como ejemplo, se considera la función

$$
f(x)=x^6-x^2\sin(2x)
$$

y se desea calcular numéricamente la integral

$$
I=\int_1^3
\left(x^6-x^2\sin(2x)\right)\,dx.
$$

La implementación permite seleccionar el número de puntos $N$ utilizados en la cuadratura y obtener una aproximación del valor de la integral.

El programa se divide en diferentes funciones. Primero se obtienen los puntos y pesos de Gauss-Legendre, posteriormente se transforman al intervalo de integración y finalmente se realiza la suma ponderada que proporciona la aproximación numérica.

