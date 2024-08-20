package atividadedeparticipação05;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

	public class Selection {
		  
		  public static void main(String[] args) {
		    String[] names = readNamesFromFile("C:/Users/dlpaf/Desktop/atividadedeparticipação05/nomes500k.txt");
		    long startTime = System.currentTimeMillis();
		    selectionSort(names);
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

		  private static void selectionSort(String[] names) {
		    for (int i = 0; i < names.length - 1; i++) {
		      int minIndex = i;
		      for (int j = i + 1; j < names.length; j++) {
		        if (names[j].compareTo(names[minIndex]) < 0) {
		          minIndex = j;
		        }
		      }
		      if (minIndex != i) {
		        String temp = names[i];
		        names[i] = names[minIndex];
		        names[minIndex] = temp;
		      }
		    }
		  }
		}