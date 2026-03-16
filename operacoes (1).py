import math

class CalculadoraCientifica:
    """Classe responsável por realizar os cálculos matemáticos."""

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Erro: Divisão por zero não permitida.")
        return a / b

    def potencia(self, base, expoente):
        return math.pow(base, expoente)

    def raiz_quadrada(self, n):
        if n < 0:
            raise ValueError("Erro: Raiz de número negativo.")
        return math.sqrt(n)

    def logaritmo(self, n, base=math.e):
        if n <= 0:
            raise ValueError("Erro: Logaritmo de número <= 0.")
        return math.log(n, base)

    def seno(self, angulo_graus):
        return math.sin(math.radians(angulo_graus))

    def cosseno(self, angulo_graus):
        return math.cos(math.radians(angulo_graus))

    def tangente(self, angulo_graus):
        # Verifica se o ângulo resulta em tangente indefinida (ex: 90º)
        if angulo_graus % 180 == 90:
            raise ValueError("Erro: Tangente indefinida para este ângulo.")
        return math.tan(math.radians(angulo_graus))