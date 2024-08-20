package atividadedeparticipação05;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Heap {
  
	  public static void main(String[] args) {
	    String[] names = readNamesFromFile("C:/Users/dlpaf/Desktop/atividadedeparticipação05/nomes500k.txt");
	    long startTime = System.currentTimeMillis();
	    heapSort(names);
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

	  private static void heapSort(String[] names) {
	    int n = names.length;
	    for (int i = n / 2 - 1; i >= 0; i--) {
	      heapify(names, n, i);
	    }
	    for (int i = n - 1; i >= 0; i--) {
	      String temp = names[0];
	      names[0] = names[i];
	      names[i] = temp;
	      heapify(names, i, 0);
	    }
	  }

	  private static void heapify(String[] names, int n, int i) {
	    int largest = i;
	    int left = 2 * i + 1;
	    int right = 2 * i + 2;
	    if (left < n && names[left].compareTo(names[largest]) > 0) {
	      largest = left;
	    }
	    if (right < n && names[right].compareTo(names[largest]) > 0) {
	      largest = right;
	    }
	    if (largest != i) {
	      String swap = names[i];
	      names[i] = names[largest];
	      names[largest] = swap;
	      heapify(names, n, largest);
	    }
	  }
	}
