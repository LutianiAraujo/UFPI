from ArvoreBinaria import ArvoreBinaria

def main():
    bst = ArvoreBinaria()

    while True:
        print("Escolha uma opção:")
        print("1 - Inserir novo elemento")
        print("2 - Mostrar tamanho da árvore")
        print("3 - Mostrar altura da árvore")
        print("4 - Mostrar menor elemento")
        print("5 - Mostrar maior elemento")
        print("6 - Calcular comprimento interno")
        print("7 - Mostrar elementos em ordem")
        print("8 - Mostrar elementos em pós-ordem")
        print("9 - Mostrar elementos em pré-ordem")
        print("10 - Mostrar elementos em largura")
        print("0 - Sair")

        opcao = int(input())

        if opcao == 1:
            nome = input("Digite o nome a ser inserido: ")
            bst.inserir(nome)
            print("Nome inserido com sucesso!")

        elif opcao == 2:
            print("Tamanho da árvore: ", bst.tam())

        elif opcao == 3:
            print("Altura da árvore: ", bst.altura())

        elif opcao == 4:
            print("Menor elemento: ", bst.min())

        elif opcao == 5:
            print("Maior elemento: ", bst.max())

        elif opcao == 6:
            print("Comprimento interno: ", bst.internal_path_length())

        elif opcao == 7:
            print("Elementos em ordem: ")
            bst.emordem()

        elif opcao == 8:
            print("Elementos em pós-ordem: ")
            bst.posordem()

        elif opcao == 9:
            print("Elementos em pré-ordem: ")
            bst.preordem()

        elif opcao == 10:
            print("Elementos em largura: ")
            bst.largura()

        elif opcao == 0:
            print("Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()