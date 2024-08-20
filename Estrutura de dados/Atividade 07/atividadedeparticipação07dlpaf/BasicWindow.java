import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;

public class BasicWindow {
	public BasicWindow() {
		JFrame frame = new JFrame(); // cria a tela onde serão desenhados os componentes
		
		// texto
		JLabel label = new JLabel("Nome:");
		label.setBounds(16, 256, 40, 10);
		frame.add(label);
		
		// caixa de texto para entrada de nome
		JTextField field = new JTextField();
		field.setBounds(56, 254, 120, 20);
		frame.add(field);
		
		// inicializa a lista
		DefaultListModel<String> list = new DefaultListModel<>();
		
		JButton button = new JButton("Adicionar");
		button.setBounds(176, 254, 120, 20);
		
		button.addActionListener(new ActionListener() {	
			@Override
			public void actionPerformed(ActionEvent e) {
				list.addElement(field.getText());
			}
		});
		
		frame.add(button);
		
		// criando um painel que contém um painel com scroll que contém a lista de strings
		JList<String> jList = new JList<>(list);
		var panel = new JPanel();
		var scrollPane = new JScrollPane(jList);
		panel.add(scrollPane);
		panel.setBounds(16, 16, 300, 200);
		frame.add(panel);
		
		frame.setSize(512, 512); // tamanho da janela
		frame.setTitle("Estruturas de Dados"); // título da janela
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // encerrar a aplicação ao fechar a janela
		frame.setLayout(null); // posição dos componentes é absoluta (definir valores)
		frame.setLocationRelativeTo(null); // faz com que a janela apareça no centro da tela
		frame.setVisible(true); // mostra a janela
	}
}