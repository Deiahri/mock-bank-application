package testPackage;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.Font;
import javax.swing.JPasswordField;
import javax.swing.ImageIcon;

public class AccountBalance {

	private JFrame frmAccountBalance;
	private JPasswordField passwordField;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					AccountBalance window = new AccountBalance();
					window.frmAccountBalance.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public AccountBalance() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmAccountBalance = new JFrame();
		frmAccountBalance.setTitle("Account Balance");
		frmAccountBalance.setResizable(false);
		frmAccountBalance.setBounds(100, 100, 600, 577);
		frmAccountBalance.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmAccountBalance.getContentPane().setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Checking Account");
		lblNewLabel.setBounds(31, 55, 100, 14);
		frmAccountBalance.getContentPane().add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("Saving Account");
		lblNewLabel_1.setBounds(86, 193, 100, 14);
		frmAccountBalance.getContentPane().add(lblNewLabel_1);
		
		JTextArea textArea = new JTextArea();
		textArea.setBounds(221, 95, 155, 22);
		frmAccountBalance.getContentPane().add(textArea);
		
		JTextArea textArea_1 = new JTextArea();
		textArea_1.setBounds(221, 188, 155, 22);
		frmAccountBalance.getContentPane().add(textArea_1);
		
		JButton btnNewButton = new JButton("Help");
		btnNewButton.setBounds(458, 313, 89, 23);
		frmAccountBalance.getContentPane().add(btnNewButton);
		
		JButton btnNewButton_1 = new JButton("Return");
		btnNewButton_1.setBounds(272, 313, 89, 23);
		frmAccountBalance.getContentPane().add(btnNewButton_1);
		
		JButton btnNewButton_2 = new JButton("Transfer Funds");
		btnNewButton_2.setBounds(72, 313, 122, 23);
		frmAccountBalance.getContentPane().add(btnNewButton_2);
		
		JLabel lblNewLabel_2 = new JLabel("Accounts");
		lblNewLabel_2.setFont(new Font("Tahoma", Font.BOLD, 20));
		lblNewLabel_2.setBounds(10, 11, 176, 22);
		frmAccountBalance.getContentPane().add(lblNewLabel_2);
		
		passwordField = new JPasswordField();
		passwordField.setBounds(221, 249, 211, 22);
		frmAccountBalance.getContentPane().add(passwordField);
		
		JLabel lblNewLabel_3 = new JLabel("New label");
		lblNewLabel_3.setIcon(new ImageIcon("C:\\Users\\dytli\\Documents\\MEGAsync\\Drett Stuff\\Drett Eclipse\\UHD\\Spring 2023\\BankApplication\\src\\testPackage\\Line.png"));
		lblNewLabel_3.setBounds(10, 129, 564, 22);
		frmAccountBalance.getContentPane().add(lblNewLabel_3);
	}
}
