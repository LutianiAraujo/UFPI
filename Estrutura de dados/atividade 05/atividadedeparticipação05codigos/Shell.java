package atividadedeparticipação05;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Shell {

	  
	  public static void main(String[] args) {
	    String[] names = readNamesFromFile("C:/Users/dlpaf/Desktop/atividadedeparticipação05/nomes500k.txt");
	    long startTime = System.currentTimeMillis();
	    shellSort(names);
	    long endTime = System.currentTimeMillis();
	    for (String name : names) {
	      System.out.println(name);
	    }
	    System.out.println("Sorting took " + (endTime - startTime) + " milliseconds.");
	  }

	  private static String[] readNamesFromFile(String fileName) {
	    try {
	      Scanner scanner = new Scanner(new File(fileName));
	      int count = scanner.nextInt();
	      String[] names = new String[count];
	      for (int i = 0; i < count; i++) {
	        names[i] = scanner.next();
	      }
	      scanner.close();
	      return names;
	    } catch (FileNotFoundException e) {
	      e.printStackTrace();
	      return null;
	    }
	  }

	  private static void shellSort(String[] names) {
	    int n = names.length;
	    for (int gap = n / 2; gap > 0; gap /= 2) {
	      for (int i = gap; i < n; i++) {
	        String key = names[i];
	        int j = i;
	        while (j >= gap && names[j - gap].compareTo(key) > 0) {
	          names[j] = names[j - gap];
	          j -= gap;
	        }
	        names[j] = key;
	      }
	    }
	  }
	}
