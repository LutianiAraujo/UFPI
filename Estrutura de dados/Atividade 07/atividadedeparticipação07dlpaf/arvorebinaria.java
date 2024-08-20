package atividadedeparticipação07dlpaf;

import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class arvorebinaria {

	public class BST {
	    No root;

	    public BST() {
	        root = null;
	    }

	    public void insert(String key) {
	        root = insertRec(root, key);
	    }

	    private No insertRec(No root, String key) {
	        if (root == null) {
	            root = new No(key);
	            return root;
	        }
	        if (key.compareTo(root.key) < 0)
	            root.left = insertRec(root.left, key);
	        else if (key.compareTo(root.key) > 0)
	            root.right = insertRec(root.right, key);
	        return root;
	    }

	    public int size() {
	        return size(root);
	    }

	    private int size(No no) {
	        if (no == null)
	            return 0;
	        else
	            return(size(no.left) + 1 + size(no.right));
	    }

	    public int height() {
	        return height(root);
	    }

	    private int height(No no) {
	        if (no == null)
	            return 0;
	        else {
	            int leftHeight = height(no.left);
	            int rightHeight = height(no.right);
	            if (leftHeight > rightHeight)
	                return (leftHeight + 1);
	            else
	                return (rightHeight + 1);
	        }
	    }

	    public String menorvalor() {
	        No no = menorNo(root);
	        if (no == null)
	            return null;
	        else
	            return no.key;
	    }

	    private No menorNo(No no) {
	        No current = no;
	        while (current.left != null)
	            current = current.left;
	        return current;
	    }

	    public String maiorvalor() {
	        No no = maiorno(root);
	        if (no == null)
	            return null;
	        else
	            return no.key;
	    }

	    private No maiorno(No no) {
	        No current = no;
	        while (current.right != null)
	            current = current.right;
	        return current;
	    }

	    public int internalPathLength() {
	        return internalPathLength(root, 0);
	    }

	    private int internalPathLength(No no, int depth) {
	        if (no == null)
	            return 0;
	        else
	            return depth + internalPathLength(no.left, depth + 1) + internalPathLength(no.right, depth + 1);
	    }

	    public void inorder() {
	        inorderRec(root);
	        System.out.println();
	    }

	    private void inorderRec(No root) {
	        if (root != null) {
	            inorderRec(root.left);
	            System.out.print(root.key + " ");
	            inorderRec(root.right);
	        }
	    }

	    public void postorder() {
	        postorderRec(root);
	        System.out.println();
	    }

	    private void postorderRec(No root) {
	        if (root != null) {
	            postorderRec(root.left);
	            postorderRec(root.right);
	            System.out.print(root.key + " ");
	        }
	    }

	    public void preorder() {
	        preorderRec(root);
	        System.out.println();
	    }

	    private void preorderRec(No root) {
	        if (root != null) {
	            System.out.print(root.key + " ");
	            preorderRec(root.left);
	            preorderRec(root.right);
	        }
	    }

	    public void levelOrder() {
	        Queue<No> queue = new LinkedList<No>();
	        queue.add(root);
	        while (!queue.isEmpty()) {
         }
	    }
	}
}
	    
