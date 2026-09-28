# Tutorial

## Uso básico

Para utilizar la implementación de cuadratura Gaussiana, primero se importa el módulo `cuadratura`:

```python
import cuadratura
```

La integral se puede calcular utilizando la función `CuadraturaGaussiana()`. Esta función recibe tres argumentos:

* `LimInf`: límite inferior del intervalo.
* `LimSup`: límite superior del intervalo.
* `N`: número de puntos de Gauss-Legendre.

Por ejemplo, para calcular la integral en el intervalo $[1,3]$ utilizando tres puntos:

```python
import cuadratura

resultado = cuadratura.CuadraturaGaussiana(1, 3, 3)

print(resultado)
```

El programa calcula numéricamente la integral

$$
I=
\int_1^3
\left(x^6-x^2\sin(2x)\right)\,dx.
$$

El resultado obtenido mediante tres puntos es aproximadamente:

```text
317.3442
```

## Comparación utilizando diferentes valores de N

Para observar cómo cambia la aproximación al aumentar el número de puntos, se puede ejecutar:

```python
import cuadratura

for N in range(1, 11):
    resultado = cuadratura.CuadraturaGaussiana(1, 3, N)
    print("N =", N, "Resultado =", resultado)
```

Este código calcula la misma integral utilizando valores de $N$ desde 1 hasta 10.

El valor de $N$ indica cuántos puntos de evaluación utiliza el método de Gauss-Legendre. Al aumentar este número, generalmente se obtiene una aproximación más precisa de la integral.

## Uso de las funciones individuales

También es posible utilizar por separado las funciones que componen el método.

### Evaluar la función

La función `Func()` permite evaluar

$$
f(x)=x^6-x^2\sin(2x)
$$

en un punto determinado:

```python
import cuadratura

resultado = cuadratura.Func(1)

print(resultado)
```

### Obtener puntos y pesos

La función `PuntosPesos()` permite obtener los puntos y pesos de Gauss-Legendre:

```python
import cuadratura

x, w = cuadratura.PuntosPesos(3)

print(x)
print(w)
```

Los valores obtenidos corresponden a los puntos y pesos definidos en el intervalo estándar $[-1,1]$.

### Transformar el intervalo

Después de obtener los puntos y pesos, se pueden transformar al intervalo deseado mediante `EscalarIntervalo()`:

```python
import cuadratura

x, w = cuadratura.PuntosPesos(3)

x, w = cuadratura.EscalarIntervalo(1, 3, x, w)

print(x)
print(w)
```

De esta manera, los puntos pasan del intervalo $[-1,1]$ al intervalo $[1,3]$.

## Ejemplo completo

El procedimiento completo puede resumirse en:

```python
import cuadratura

# Límites de integración
LimInf = 1
LimSup = 3

# Número de puntos
N = 3

# Cálculo de la integral
Resultado = cuadratura.CuadraturaGaussiana(LimInf, LimSup, N)

print("Resultado =", Resultado)
```

Este ejemplo permite ejecutar la implementación completa sin necesidad de realizar manualmente la transformación de los puntos ni la suma ponderada.

