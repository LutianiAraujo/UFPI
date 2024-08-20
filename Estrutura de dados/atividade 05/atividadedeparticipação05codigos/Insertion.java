package atividadedeparticipação05;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Insertion {

	  public static void main(String[] args) {
	    String[] names = readNamesFromFile("C:/Users/dlpaf/Desktop/atividadedeparticipação05/nomes500k.txt");
	    long startTime = System.currentTimeMillis();
	    insertionSort(names);
	    long endTime = System.currentTimeMillis();
	    for (String name : names) {
	      System.out.println(name);
	    }
	    System.out.println("Sorting took " + (endTime - startTime) + " milliseconds.");
	  }

	  private static String[] readNamesFromFile(String nomes10k) {
	    try {
	      Scanner scanner = new Scanner(new File(nomes10k));
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

	  private static void insertionSort(String[] names) {
	    for (int i = 1; i < names.length; i++) {
	      String key = names[i];
	      int j = i - 1;
	      while (j >= 0 && names[j].compareTo(key) > 0) {
	        names[j + 1] = names[j];
	        j--;
	      }
	      names[j + 1] = key;
	    }
	  }
	}