package atividadedeparticipação05;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class quicksimplificado {

	  public static void main(String[] args) {
	    String[] names = readNamesFromFile("C:/Users/dlpaf/Desktop/atividadedeparticipação05/nomes500k.txt");
	    long startTime = System.currentTimeMillis();
	    quickSort(names, 0, names.length-1);
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

	  private static void quickSort(String[] names, int left, int right) {
	    if (left < right) {
	      int pivotIndex = partition(names, left, right);
	      quickSort(names, left, pivotIndex-1);
	      quickSort(names, pivotIndex+1, right);
	    }
	  }

	  private static int partition(String[] names, int left, int right) {
	    int pivotIndex = (left + right) / 2;
	    String pivotValue = names[pivotIndex];
	    swap(names, pivotIndex, right);
	    int storeIndex = left;
	    for (int i = left; i < right; i++) {
	      if (names[i].compareTo(pivotValue) < 0) {
	        swap(names, storeIndex, i);
	        storeIndex++;
	      }
	    }
	    swap(names, right, storeIndex);
	    return storeIndex;
	  }

	  private static void swap(String[] names, int i, int j) {
	    String temp = names[i];
	    names[i] = names[j];
	    names[j] = temp;
	  }
	}
