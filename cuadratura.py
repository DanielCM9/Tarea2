import numpy as np


def Func(VarInd):
    """Evalúa la función utilizada para la integración.

    La función corresponde a:

        f(x) = x**6 - x**2 * sin(2*x)

    Args:
        VarInd (float): Valor de x donde se evalúa la función.

    Returns:
        float: Valor de la función evaluada.

    Examples:
        >>> Func(1)
        0.09070257317431829
    """
    return VarInd**6 - VarInd**2 * np.sin(2 * VarInd)


def PuntosPesos(N):
    """Obtiene los puntos y pesos de Gauss-Legendre.

    Utiliza la función leggauss de NumPy para obtener los puntos
    y pesos correspondientes a una cuadratura de Gauss-Legendre
    de N puntos en el intervalo [-1, 1].

    Args:
        N (int): Número de puntos de la cuadratura.

    Returns:
        tuple: Una tupla que contiene dos arreglos de NumPy:
            los puntos de Gauss-Legendre y sus pesos correspondientes.

    Examples:
        >>> x, w = PuntosPesos(3)
        >>> len(x)
        3
        >>> len(w)
        3
    """
    x, w = np.polynomial.legendre.leggauss(N)

    return x, w


def EscalarIntervalo(LimInf, LimSup, x, w):
    """Transforma los puntos y pesos al intervalo de integración.

    Realiza el cambio de variable necesario para transformar
    los puntos y pesos definidos originalmente en [-1, 1]
    al intervalo [LimInf, LimSup].

    Args:
        LimInf (float): Límite inferior del intervalo.
        LimSup (float): Límite superior del intervalo.
        x (numpy.ndarray): Puntos de Gauss-Legendre en [-1, 1].
        w (numpy.ndarray): Pesos de Gauss-Legendre.

    Returns:
        tuple: Una tupla que contiene los puntos y pesos
            transformados al intervalo [LimInf, LimSup].

    Examples:
        >>> x, w = PuntosPesos(2)
        >>> x, w = EscalarIntervalo(1, 3, x, w)
        >>> len(x)
        2
        >>> len(w)
        2
    """
    x = 0.5 * (LimSup - LimInf) * x + 0.5 * (LimSup + LimInf)
    w = 0.5 * (LimSup - LimInf) * w

    return x, w


def CuadraturaGaussiana(LimInf, LimSup, N):
    """Calcula una integral mediante cuadratura Gaussiana.

    La función utiliza cuadratura de Gauss-Legendre para aproximar
    la integral de la función definida en Func() sobre el intervalo
    [LimInf, LimSup].

    Args:
        LimInf (float): Límite inferior de integración.
        LimSup (float): Límite superior de integración.
        N (int): Número de puntos utilizados en la cuadratura.

    Returns:
        float: Aproximación numérica de la integral.

    Examples:
        >>> resultado = CuadraturaGaussiana(1, 3, 3)
        >>> isinstance(resultado, float)
        True
    """
    x, w = PuntosPesos(N)

    x, w = EscalarIntervalo(LimInf, LimSup, x, w)

    Integral = 0

    for i in range(N):
        Integral += w[i] * Func(x[i])

    return Integral
