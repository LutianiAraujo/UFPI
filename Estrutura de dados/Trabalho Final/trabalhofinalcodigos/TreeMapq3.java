package trabalhofinal;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class TreeMapq3 {
    public static void main(String[] args) {

        // Mede o tempo de execução total
        long totalTimeStart = System.currentTimeMillis();

        // Abre o arquivo de texto para leitura
        File file = new File("C:/Users/dlpaf/Documents/UFPI/Quarto Periodo/Estrutura de dados/Trabalho Final/leipzig100k.txt");



        // Inicializa o TreeMap para armazenar as palavras e suas frequências
        TreeMap<String, Integer> wordMap = new TreeMap<String, Integer>();



        try {
            // Cria um scanner para ler o arquivo
            Scanner scanner = new Scanner(file);

            // Define os delimitadores
            scanner.useDelimiter("[\\s\\p{Punct}\\d]+");

            // Adiciona as palavras no TreeMap
            while (scanner.hasNext()) {
                String word = scanner.next().toLowerCase();
                if (word.equals("") || word.equals("0")) {
                    continue; // Ignora chaves com valor igual a zero ou nulo
                }
                if (wordMap.containsKey(word)) {
                    int count = wordMap.get(word);
                    wordMap.put(word, count + 1);
                } else {
                    wordMap.put(word, 1);
                }
            }

            // Fecha o scanner
            scanner.close();

            // Imprime o tamanho da tabela de símbolos
            System.out.println("Tamanho da tabela de símbolos: " + wordMap.size());

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }


        // Imprime as palavras armazenadas na tabela de símbolos
        for (Map.Entry<String, Integer> entry : wordMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        /*  
        // Busca de palavras
        String[] searchWords = {"Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government", "Authorities"};

        System.out.println("\nBusca de palavras:");

        for (String searchWord : searchWords) {
            if (wordMap.containsKey(searchWord)) {
                int count = wordMap.get(searchWord);
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
            if (wordMap.containsKey(removeWord)) {
                wordMap.remove(removeWord);
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