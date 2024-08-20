package trabalhofinal;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;


public class HashSetq2 {
	 public static void main(String[] args) {

	        // Mede o tempo de execução total
	        long totalTimeStart = System.currentTimeMillis();

	        // Inicializa o HashMap para armazenar as palavras
	        HashMap<String, Integer> wordsMap = new HashMap<String, Integer>();

	        // Abre o arquivo de texto para leitura
	        File file = new File("C:/Users/dlpaf/Documents/UFPI/Quarto Periodo/Estrutura de dados/Trabalho Final/leipzig100k.txt");

	        try {
	            // Cria um scanner para ler o arquivo
	            Scanner scanner = new Scanner(file);

	            // Define os delimitadores
	            scanner.useDelimiter("[\\s\\p{Punct}\\d]+");

	            // Adiciona as palavras no HashMap
	            while (scanner.hasNext()) {
	                String word = scanner.next().toLowerCase();
	                if (wordsMap.containsKey(word)) {
	                    wordsMap.put(word, wordsMap.get(word) + 1);
	                } else {
	                    wordsMap.put(word, 1);
	                }
	            }

	            // Fecha o scanner
	            scanner.close();

	            // Imprime o tamanho da tabela de símbolos
	            System.out.println("Tamanho da tabela de símbolos: " + wordsMap.size());

	        } catch (FileNotFoundException e) {
	            e.printStackTrace();
	        }

	        // Imprime as palavras armazenadas na tabela de símbolos
	        for (String word : wordsMap.keySet()) {
	            System.out.println(word + ": " + wordsMap.get(word));
	        }
	        // Realiza a busca pelas 10 palavras
	        String[] searchWords = {"Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government", "Authorities"};
	        /*  
	        for (String word : searchWords) {
	            if (wordsMap.containsKey(word.toLowerCase())) {
	                System.out.println(word + " encontrado " + wordsMap.get(word.toLowerCase()) + " vezes.");
	            } else {
	                System.out.println(word + " não encontrado.");
	            }
	        }
*/
            // Remove as 10 palavras
              for (String word : searchWords) {
                wordsMap.remove(word.toLowerCase());
                System.out.println(word + " palavra apagada com sucesso!");
                
            }
              // Mede o tempo de execução total
  	        long totalTimeEnd = System.currentTimeMillis();
  	        long totalTime = totalTimeEnd - totalTimeStart;

  	        // Imprime o tempo de execução total
  	        System.out.println("Tempo de execução total: " + totalTime + " ms");
	    }
}
