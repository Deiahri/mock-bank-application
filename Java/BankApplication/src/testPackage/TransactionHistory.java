package testPackage;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JList;
import javax.swing.JTextArea;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class TransactionHistory {

	private JFrame frmTransactionHistory;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					TransactionHistory window = new TransactionHistory();
					window.frmTransactionHistory.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public TransactionHistory() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmTransactionHistory = new JFrame();
		frmTransactionHistory.setTitle("Transaction History");
		frmTransactionHistory.setResizable(false);
		frmTransactionHistory.setBounds(100, 100, 600, 400);
		frmTransactionHistory.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmTransactionHistory.getContentPane().setLayout(null);
		
		JTextArea textArea = new JTextArea();
		textArea.setBounds(56, 55, 462, 241);
		frmTransactionHistory.getContentPane().add(textArea);
		
		JLabel lblNewLabel = new JLabel("Transaction History");
		lblNewLabel.setFont(new Font("Tahoma", Font.BOLD, 20));
		lblNewLabel.setBounds(56, 22, 211, 21);
		frmTransactionHistory.getContentPane().add(lblNewLabel);
		
		JButton btnNewButton = new JButton("Back");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btnNewButton.setBounds(56, 314, 89, 23);
		frmTransactionHistory.getContentPane().add(btnNewButton);
		
		JButton btnHelp = new JButton("Help");
		btnHelp.setBounds(428, 314, 89, 23);
		frmTransactionHistory.getContentPane().add(btnHelp);
	}
}
