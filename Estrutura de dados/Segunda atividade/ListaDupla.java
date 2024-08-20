package atividade2edlisdupenc;

public class ListaDupla {
	Lis inicio;
	Lis fim;
	int tamanho = 0;
	
	public void InsereInicio(String info) {
		Lis lis = new Lis();
		lis.info = info;
		lis.anterior = null;
		lis.proximo = inicio;
		if (inicio != null) {
			inicio.anterior = lis;
		}
		inicio = lis;
		if (tamanho == 0) {
			fim = inicio;
		}
		tamanho++;
	}
	public String retirarInicio() {
		if (inicio == null) {
			return null;
		}
		String out = inicio.info;
		inicio = inicio.proximo;
		if (inicio != null) {
			inicio.anterior = null;
		} else {
			fim = null;
		}
		tamanho--;
		return out;
	}
	public void inserirFim(String info) {
		if(fim == null) {
		    Lis lis = new Lis();
		    lis.info = info;
		    fim = lis;
		    inicio = fim;
		    return ;
		}
		Lis lis = new Lis();
	    lis.info = info;
	    lis.proximo = null;
	    lis.anterior = fim;
	    fim.proximo = lis; 
	    fim = lis;
	    if (tamanho == 0) {
	        inicio = fim;
	    }
	    tamanho++;
	}
	public String retirarfim() {
		if (fim == null) {
			return null;
		}
		String out = fim.info;
		fim = fim.anterior;
		if (fim != null) {
			fim.proximo = null;
		} else {
			inicio = null;
		}
		tamanho--;
		return out;
	}
	
	public String toString() {
	    String str = "[";
	    for(Lis i = inicio; i != null; i = i.proximo) {
	        str += i.info + ", ";
	    }
	    str = str.substring(0, str.length() - 2) + "]";
	    return str;
	}
	 public int buscarNome(String nome) {
	        if(inicio == null) return -1;
	        int indice = 0;
	        for(Lis i = inicio; i != null; i = i.proximo){
	            if(i.info.equals(nome)) return indice;
	            indice ++;
	        }
	        return -1;
	    }
	 public int removerNome(String nome) {
	        if(inicio == null) return -1;
	        int indice = 0;
	        for(Lis i = inicio; i != null; i = i.proximo) {
	            if(i.info.equals(nome)) {
	                if(i.anterior != null) i.anterior.proximo = i.proximo;
	                else inicio = i.proximo;
	                
	                if(i.proximo != null) i.proximo.anterior = i.anterior;
	                else fim = i.anterior;
	                
	                return indice;
	            }
	            indice ++;
	        }
	        return -1;
	    }


}
	
