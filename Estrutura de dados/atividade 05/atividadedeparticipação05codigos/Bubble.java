package atividadedeparticipação05;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Bubble {
	  
	  public static void main(String[] args) {
	    String[] names = readNamesFromFile("C:/Users/dlpaf/Desktop/atividadedeparticipação05/nomes100k.txt");
	    long startTime = System.currentTimeMillis();
	    bubbleSort(names);
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

	  private static void bubbleSort(String[] names) {
	    boolean swapped;
	    for (int i = 0; i < names.length - 1; i++) {
	      swapped = false;
	      for (int j = 0; j < names.length - i - 1; j++) {
	        if (names[j].compareTo(names[j + 1]) > 0) {
	          String temp = names[j];
	          names[j] = names[j + 1];
	          names[j + 1] = temp;
	          swapped = true;
	        }
	      }
	      if (!swapped) {
	        break;
	    }
	  }
	}
}
