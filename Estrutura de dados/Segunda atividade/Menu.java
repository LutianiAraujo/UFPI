package atividade2edlisdupenc;
import java.util.Scanner;
public class Menu {
		public static void main(String[] args) {
			int numero;
			Scanner input = new Scanner(System.in);
			ListaDupla list = new ListaDupla();
			int ni;

			do {
				System.out.println(
						"Digite 1 para inserir, 2 para mostrar a Lista,3 para buscar por nome, 4 para deletar, 5 para parar: ");
				numero = input.nextInt();
				switch(numero) {
				case 1: {
					System.out.println("Digite 1 para inserir no inicio, 2 para inserir no final: ");
					ni = input.nextInt();
					switch(ni) {
					case 1: {
						System.out.print("Insira um nome: ");
						input.nextLine();
						String str = input.nextLine();
						list.InsereInicio(str);
						break;
					}
					case 2: {
						System.out.print("Insira um nome: ");
						input.nextLine();
						String str = input.nextLine();
						list.inserirFim(str);
						break;
					}
					}

					break;
				}
				case 2: {
					System.out.println(list);
				}
					break;
				case 3: {
					ListaDupla l = new ListaDupla();
					System.out.print("Insira um nome: ");
					input.nextLine();
					String str = input.nextLine();
					l.buscarNome(str);

					break;
				}
				case 4: {
					ListaDupla l = new ListaDupla();
					System.out.print("Insira um nome para remover: ");
					input.nextLine();
					String str = input.nextLine();
					l.removerNome(str);

					break;
				}
				case 5: {
					System.out.println("Finalizando o Programa, Obrigado!");
					break;
				}

				}
			} while(numero != 5);
			input.close();
		}
	}
