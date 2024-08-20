package trabalhofinal;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Vector;

public class Vectorq1 {

    public static void main(String[] args) {

        // Mede o tempo de execução total
        long totalTimeStart = System.currentTimeMillis();

        Vector<String> wordsVector = new Vector<String>();

        File file = new File("C:/Users/dlpaf/Documents/UFPI/Quarto Periodo/Estrutura de dados/Trabalho Final/leipzig100k.txt");

        try {
            Scanner scanner = new Scanner(file);

            scanner.useDelimiter("[\\s\\p{Punct}\\d]+");

            while (scanner.hasNext()) {
                String word = scanner.next().toLowerCase();
                wordsVector.add(word);
            }

            scanner.close();

            System.out.println("Tamanho da tabela de símbolos: " + wordsVector.size());

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        for (String word : wordsVector) {
            System.out.println(word);
        }
/*
        System.out.println("Palavras encontradas:");
        ArrayList<String> palavrasBuscadas = new ArrayList<String>();
        palavrasBuscadas.add("lisbon");
        palavrasBuscadas.add("nasa");
        palavrasBuscadas.add("kyunghee");
        palavrasBuscadas.add("konkuk");
        palavrasBuscadas.add("sogang");
        palavrasBuscadas.add("momentarily");
        palavrasBuscadas.add("rubella");
        palavrasBuscadas.add("vaccinations");
        palavrasBuscadas.add("government");
        palavrasBuscadas.add("authorities");

        for (String palavra : palavrasBuscadas) {
            if (wordsVector.contains(palavra)) {
                System.out.println(palavra);
            }
        }
        */
        // Remove as 10 palavras
        System.out.println("Palavras removidas:");
        ArrayList<String> palavrasRemover = new ArrayList<String>();
        palavrasRemover.add("lisbon");
        palavrasRemover.add("nasa");
        palavrasRemover.add("kyunghee");
        palavrasRemover.add("konkuk");
        palavrasRemover.add("sogang");
        palavrasRemover.add("momentarily");
        palavrasRemover.add("rubella");
        palavrasRemover.add("vaccinations");
        palavrasRemover.add("government");
        palavrasRemover.add("authorities");

        for (String palavra : palavrasRemover) {
            if (wordsVector.contains(palavra)) {
            	System.out.println(palavra);
                wordsVector.remove(palavra);
            }
        }
        // Mede o tempo de execução total
        long totalTimeEnd = System.currentTimeMillis();
        long totalTime = totalTimeEnd - totalTimeStart;

        // Imprime o tempo de execução total
        System.out.println("Tempo de execução total: " + totalTime + " ms");
    }
}