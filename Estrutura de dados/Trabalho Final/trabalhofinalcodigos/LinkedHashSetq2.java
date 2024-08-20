package trabalhofinal;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.LinkedHashSet;
import java.util.Scanner;

public class LinkedHashSetq2 {
	public static void main(String[] args) {

        // Mede o tempo de execução total
        long totalTimeStart = System.currentTimeMillis();

		// Inicializa o LinkedHashSet para armazenar as palavras
		LinkedHashSet<String> wordsSet = new LinkedHashSet<String>();

		// Abre o arquivo de texto para leitura
		File file = new File("C:/Users/dlpaf/Documents/UFPI/Quarto Periodo/Estrutura de dados/Trabalho Final/leipzig100k.txt");

		try {
			// Cria um scanner para ler o arquivo
			Scanner scanner = new Scanner(file);

			// Define os delimitadores
			scanner.useDelimiter("[\\s\\p{Punct}\\d]+");

			// Adiciona as palavras no LinkedHashSet
			while (scanner.hasNext()) {
				String word = scanner.next().toLowerCase();
				wordsSet.add(word);
			}

			// Fecha o scanner
			scanner.close();

			// Imprime o tamanho da tabela de símbolos
			System.out.println("Tamanho da tabela de símbolos: " + wordsSet.size());

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}


		// Imprime as palavras armazenadas na tabela de símbolos
		for (String word : wordsSet) {
			System.out.println(word);
		}
		String[] searchWords = {"Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella",
				"vaccinations", "government", "Authorities"};
		  /*  
		for (String word : searchWords) {
			if (wordsSet.contains(word.toLowerCase())) {
				System.out.println("A palavra \"" + word + "\" foi encontrada na tabela de símbolos.");
			} else {
				System.out.println("A palavra \"" + word + "\" não foi encontrada na tabela de símbolos.");
			}
		}
*/
            // Remove as 10 palavras
               for (String word : searchWords) {
                wordsSet.remove(word.toLowerCase());
                System.out.println( word + " palavra apagada com sucesso!");
                
            }

	     // Mede o tempo de execução total
        long totalTimeEnd = System.currentTimeMillis();
        long totalTime = totalTimeEnd - totalTimeStart;

        // Imprime o tempo de execução total
        System.out.println("Tempo de execução total: " + totalTime + " ms");
	}

}
