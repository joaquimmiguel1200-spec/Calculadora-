from operacoes import CalculadoraCientifica
from interface import Menu

def main():
    calc = CalculadoraCientifica()
    menu = Menu()

    while True:
        menu.exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Encerrando calculadora...")
            break
        
        try:
            # Operações de dois operandos
            if opcao in ['1', '2', '3', '4', '5']:
                n1 = menu.obter_input("Primeiro número: ")
                n2 = menu.obter_input("Segundo número: ")
                if n1 is None or n2 is None: continue

                if opcao == '1': print(f"Resultado: {calc.somar(n1, n2)}")
                elif opcao == '2': print(f"Resultado: {calc.subtrair(n1, n2)}")
                elif opcao == '3': print(f"Resultado: {calc.multiplicar(n1, n2)}")
                elif opcao == '4': print(f"Resultado: {calc.dividir(n1, n2)}")
                elif opcao == '5': print(f"Resultado: {calc.potencia(n1, n2)}")

            # Operações de um operando
            elif opcao in ['6', '7', '8', '9']:
                n = menu.obter_input("Valor/Ângulo (graus): ")
                if n is None: continue

                if opcao == '6': print(f"Resultado: {calc.raiz_quadrada(n)}")
                elif opcao == '7': print(f"Resultado: {calc.seno(n)}")
                elif opcao == '8': print(f"Resultado: {calc.cosseno(n)}")
                elif opcao == '9': print(f"Resultado: {calc.tangente(n)}")

            # Logaritmo
            elif opcao == '10':
                n = menu.obter_input("Número: ")
                b = menu.obter_input("Base (Enter para log natural): ")
                if n is None: continue
                
                if b is None: # Se o usuário errar o input da base ou deixar vazio
                    print(f"Resultado (ln): {calc.logaritmo(n)}")
                else:
                    print(f"Resultado: {calc.logaritmo(n, b)}")

            else:
                print("Opção inválida!")

        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()