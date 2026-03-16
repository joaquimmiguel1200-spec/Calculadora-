class Menu:
    """Classe responsável pela interação com o usuário via terminal."""

    @staticmethod
    def exibir_menu():
        print("\n" + "="*30)
        print("   CALCULADORA CIENTÍFICA")
        print("="*30)
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Potência (^)")
        print("6. Raiz Quadrada (√)")
        print("7. Seno (sin)")
        print("8. Cosseno (cos)")
        print("9. Tangente (tan)")
        print("10. Logaritmo")
        print("0. Sair")
        print("-" * 30)

    @staticmethod
    def obter_input(mensagem, tipo=float):
        try:
            return tipo(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            return None