package trabalhofinal;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Scanner;



public class LinkedHashMapq3 {

	    public static void main(String[] args) {
	    	
	    	// Mede o tempo de execução total
	        long totalTimeStart = System.currentTimeMillis();

	        
	        // Inicializa o LinkedHashMap para armazenar as palavras
	        LinkedHashMap<String, Integer> wordsMap = new LinkedHashMap<>();
	
	        

	        // Abre o arquivo de texto para leitura
	        File file = new File("C:/Users/dlpaf/Documents/UFPI/Quarto Periodo/Estrutura de dados/Trabalho Final/leipzig100k.txt");

	        try {
	            // Cria um scanner para ler o arquivo
	            Scanner scanner = new Scanner(file);

	            // Define os delimitadores
	            scanner.useDelimiter("[\\s\\p{Punct}\\d]+");

	            // Adiciona as palavras no LinkedHashMap
	            while (scanner.hasNext()) {
	                String word = scanner.next().toLowerCase();
	                
	                if (word.equals("") || word.equals("0")) {
	                    continue; // Ignora chaves com valor igual a zero ou nulo
	                }
	                // Verifica se a palavra já existe no mapa
	                if (wordsMap.containsKey(word)) {
	                    // Incrementa a contagem de ocorrências
	                    wordsMap.put(word, wordsMap.get(word) + 1);
	                } else {
	                    // Adiciona a palavra com contagem 1
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
	            int count = wordsMap.get(word);
	            System.out.println(word + " ocorre " + count + " vezes");
	        }
	        /*  
	        // Busca de palavras
	        String[] searchWords = {"Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government", "Authorities"};

	        System.out.println("\nBusca de palavras:");

	        for (String searchWord : searchWords) {
	            if (wordsMap.containsKey(searchWord)) {
	                int count = wordsMap.get(searchWord);
	                System.out.println(searchWord + " : " + count);
	            } else {
	                System.out.println(searchWord + " não encontrado.");
	            }
	        }
	        */
	        // Remoção de palavras
	        String[] removeWords = {"Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government", "Authorities"};

	        System.out.println("\nRemoção de palavras:");

	        for (String removeWord : removeWords) {
	            if (wordsMap.containsKey(removeWord)) {
	                wordsMap.remove(removeWord);
	                System.out.println(removeWord + " removido.");
	            } else {
	                System.out.println(removeWord + " não encontrado.");
	            }
	        }


	        // Mede o tempo de execução total
	        long totalTimeEnd = System.currentTimeMillis();
	        long totalTime = totalTimeEnd - totalTimeStart;

	        // Imprime o tempo de execução total
	        System.out.println("Tempo de execução total: " + totalTime + " ms");

	    }
}
