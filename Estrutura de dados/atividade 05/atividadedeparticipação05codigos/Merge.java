package atividadedeparticipação05;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Merge {
	  
	  public static void main(String[] args) {
	    String[] names = readNamesFromFile("C:/Users/dlpaf/Desktop/atividadedeparticipação05/nomes500k.txt");
	    long startTime = System.currentTimeMillis();
	    mergeSort(names, 0, names.length-1);
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

	  private static void mergeSort(String[] names, int left, int right) {
	    if (left < right) {
	      int middle = (left + right) / 2;
	      mergeSort(names, left, middle);
	      mergeSort(names, middle + 1, right);
	      merge(names, left, middle, right);
	    }
	  }

	  private static void merge(String[] names, int left, int middle, int right) {
	    int leftSize = middle - left + 1;
	    int rightSize = right - middle;
	    String[] leftArray = new String[leftSize];
	    String[] rightArray = new String[rightSize];
	    for (int i = 0; i < leftSize; i++) {
	      leftArray[i] = names[left + i];
	    }
	    for (int i = 0; i < rightSize; i++) {
	      rightArray[i] = names[middle + 1 + i];
	    }
	    int i = 0, j = 0, k = left;
	    while (i < leftSize && j < rightSize) {
	      if (leftArray[i].compareTo(rightArray[j]) <= 0) {
	        names[k] = leftArray[i];
	        i++;
	      } else {
	        names[k] = rightArray[j];
	        j++;
	      }
	      k++;
	    }
	    while (i < leftSize) {
	      names[k] = leftArray[i];
	      i++;
	      k++;
	    }
	    while (j < rightSize) {
	      names[k] = rightArray[j];
	      j++;
	      k++;
	    }
	  }
	}