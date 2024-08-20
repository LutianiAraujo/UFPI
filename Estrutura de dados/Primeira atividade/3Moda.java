package Atividade1;
import java.util.*;

public class Moda {

public static void main(String argumentos[]){
    Integer []a = {7,2,8,10,5,3,1,6,6,1,6};
    System.out.println("Moda: ");

    System.out.println();
       Integer[] result = mode(a);

       for(int i = 0; i< result.length;i++) {
           System.out.print(result[i]);    
    }

}

  public static Integer[] mode(Integer[] a){
      Set<Integer> modas = new LinkedHashSet<Integer>(  );
      int maxCount=0;   
      for (int i = 0; i < a.length; ++i){
        int count = 0;
        for (int j = 0; j < a.length; ++j){
          if (a[j] == a[i]) 
              ++count;
        }
        if (count > maxCount){
          maxCount = count;
          modas.clear();
          modas.add( a[i] );
        } else if ( count == maxCount ){
          modas.add( a[i] );
        }
      }
      return modas.toArray( new Integer[modes()]);
    }

private static int modes() {
    return 0;
}
}