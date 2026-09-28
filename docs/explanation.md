# Método numérico

## Cuadratura de Gauss-Legendre

La cuadratura de Gauss-Legendre es un método de integración numérica que aproxima una integral definida mediante una suma ponderada de los valores de la función en determinados puntos.

Para el intervalo estándar $[-1,1]$, la integral

$$
I=\int_{-1}^{1}f(t)\,dt
$$

se aproxima mediante

$$
I\approx
\sum_{i=1}^{N}w_i f(t_i),
$$

donde $t_i$ son los puntos de Gauss-Legendre y $w_i$ son los pesos correspondientes.

Los puntos $t_i$ corresponden a las raíces del polinomio de Legendre de grado $N$. Los pesos $w_i$ determinan la contribución de cada evaluación de la función a la aproximación de la integral.

En la implementación realizada en Python, los puntos y pesos se obtienen utilizando la función `leggauss` de NumPy:

```python
x, w = np.polynomial.legendre.leggauss(N)
```

## Transformación del intervalo

La expresión anterior está definida para el intervalo $[-1,1]$. Para aplicar el método a un intervalo general $[a,b]$, se realiza un cambio de variable.

Se utiliza la transformación

$$
x=
\frac{b-a}{2}t+
\frac{b+a}{2},
$$

donde $t\in[-1,1]$ y $x\in[a,b]$.

Al derivar esta expresión se obtiene

$$
dx=
\frac{b-a}{2}\,dt.
$$

Por lo tanto,

$$
\int_a^b f(x)\,dx
=
\frac{b-a}{2}
\int_{-1}^{1}
f\left(
\frac{b-a}{2}t+
\frac{b+a}{2}
\right)dt.
$$

Aplicando la cuadratura de Gauss-Legendre se obtiene la aproximación

$$
\boxed{
\int_a^b f(x)\,dx
\approx
\frac{b-a}{2}
\sum_{i=1}^{N}
w_i
f\left(
\frac{b-a}{2}t_i+
\frac{b+a}{2}
\right)
}
$$

Esta transformación es implementada mediante la función `EscalarIntervalo()`.

## Implementación del método

El programa divide el procedimiento numérico en tres etapas principales.

### 1. Obtención de puntos y pesos

La función `PuntosPesos(N)` obtiene los $N$ puntos y pesos de Gauss-Legendre en el intervalo $[-1,1]$.

```python
x, w = PuntosPesos(N)
```

### 2. Transformación del intervalo

La función `EscalarIntervalo()` transforma los puntos y pesos obtenidos al intervalo deseado.

```python
x, w = EscalarIntervalo(LimInf, LimSup, x, w)
```

La transformación de los puntos está dada por

$$
x_i=
\frac{b-a}{2}t_i+
\frac{b+a}{2},
$$

mientras que los pesos se transforman mediante

$$
W_i=
\frac{b-a}{2}w_i.
$$

### 3. Cálculo de la integral

Finalmente, `CuadraturaGaussiana()` realiza la suma

```python
Integral += w[i] * Func(x[i])
```

que corresponde matemáticamente a

$$
I\approx
\sum_{i=1}^{N}W_i f(x_i).
$$

Para el problema considerado,

$$
f(x)=x^6-x^2\sin(2x),
$$

con límites

$$
a=1,\qquad b=3.
$$

Por lo tanto, el programa aproxima la integral

$$
\int_1^3
\left(x^6-x^2\sin(2x)\right)\,dx.
$$

## Influencia del número de puntos

El parámetro $N$ determina el número de puntos utilizados para realizar la aproximación. En general, aumentar $N$ proporciona una aproximación más precisa para una función suficientemente regular.

En este proyecto se puede estudiar esta dependencia calculando la integral para diferentes valores de $N$, por ejemplo desde $N=1$ hasta $N=10$.

