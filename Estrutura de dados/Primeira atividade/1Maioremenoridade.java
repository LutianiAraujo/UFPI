package treinamentoemjava;
import java.util.Scanner;
public class Maioremenoridade {

public static void main(String[] args) {
	   Scanner scan = new Scanner(System.in);
	
	//Variaveis
	int n;
	 System.out.println("Digite a quantidade de pessoas: ");
	    n = scan.nextInt();
	String[] nomes = new String[n];
    int[] idades = new int[n];
    int idadeMaisNova = 99;
    String nomeDaPessoaMaisNova = "";
    int idadeMaisVelha = 0;
    String nomeDaPessoaMaisVelha = "";
    double media = 0;

    //Entrada de dados + calculo da media 
    for (int i = 0; i < n; i++) {
        System.out.println("Digite o nome: ");
        nomes[i] = scan.next();
        System.out.println("Digite a idade:");
        idades[i] = scan.nextInt();
        media = media + idades[i];
    }
    //nomes do maior e menor idade
    for (int i = 0; i < n; i++) {
        if (idades[i] < idadeMaisNova) {
            idadeMaisNova = idades[i];
            nomeDaPessoaMaisNova = nomes[i];
        }
        if (idades[i] > idadeMaisVelha) {
            idadeMaisVelha = idades[i];
            nomeDaPessoaMaisVelha = nomes[i];
        }
    }
    media = media/idades.length;
    		
    // Exibindo os resultados
    System.out.println("Pessoa Mais nova Nome: " + nomeDaPessoaMaisNova);
    System.out.println("Pessoa Mais nova Idade: " + idadeMaisNova);
    System.out.println("Pessoa Mais velha Nome : " + nomeDaPessoaMaisVelha);
    System.out.println("Pessoa Mais velha Idade: " + idadeMaisVelha);
    System.out.println("A média é:" + media);
}
}