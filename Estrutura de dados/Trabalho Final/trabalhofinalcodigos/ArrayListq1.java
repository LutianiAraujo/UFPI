package trabalhofinal;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;


public class ArrayListq1 {

    public static void main(String[] args) {

        // Mede o tempo de execução total
        long totalTimeStart = System.currentTimeMillis();

        ArrayList<String> wordsList = new ArrayList<String>();

        File file = new File("C:/Users/dlpaf/Documents/UFPI/Quarto Periodo/Estrutura de dados/Trabalho Final/leipzig100k.txt");

        try {

            Scanner scanner = new Scanner(file);

            scanner.useDelimiter("[\\s\\p{Punct}\\d]+");

            while (scanner.hasNext()) {
                String word = scanner.next().toLowerCase();
                wordsList.add(word);
            }

            scanner.close();

            System.out.println("Tamanho da tabela de símbolos: " + wordsList.size());

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }


        for (String word : wordsList) {
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
            if (wordsList.contains(palavra)) {
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
            if (wordsList.contains(palavra)) {
            	System.out.println(palavra);
                wordsList.remove(palavra);
            }
        }
        // Mede o tempo de execução total
        long totalTimeEnd = System.currentTimeMillis();
        long totalTime = totalTimeEnd - totalTimeStart;

        // Imprime o tempo de execução total
        System.out.println("Tempo de execução total: " + totalTime + " ms");
    }
}
