package testPackage;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JTextArea;
import javax.swing.JButton;
import javax.swing.SwingConstants;
import javax.swing.UIManager;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MainAppWindow {

	private JFrame frmBanker;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MainAppWindow window = new MainAppWindow();
					window.frmBanker.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public MainAppWindow() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmBanker = new JFrame();
		frmBanker.setResizable(false);
		frmBanker.getContentPane().setFont(new Font("Tahoma", Font.BOLD, 11));
		frmBanker.setTitle("Home ");
		frmBanker.setBounds(100, 100, 600, 400);
		frmBanker.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmBanker.getContentPane().setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Welcome, ");
		lblNewLabel.setFont(new Font("Tahoma", Font.BOLD, 11));
		lblNewLabel.setBounds(40, 27, 58, 14);
		frmBanker.getContentPane().add(lblNewLabel);
		
		JButton btnNewButton = new JButton("Customize Profile");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
			}
		});
		btnNewButton.setBounds(40, 107, 124, 23);
		frmBanker.getContentPane().add(btnNewButton);
		
		JButton btnViewBalance = new JButton("View Balance");
		btnViewBalance.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				//takes user to AccountBalance.java
				
			}
		});
		btnViewBalance.setBounds(40, 157, 124, 23);
		frmBanker.getContentPane().add(btnViewBalance);
		
		JButton btnTransactions = new JButton("Transactions");
		btnTransactions.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				//takes user to TransactionHistory.java
				if(e.getSource() == btnTransactions) {
					new TransactionHistory();
				}
			}
		});
		btnTransactions.setBounds(40, 212, 124, 23);
		frmBanker.getContentPane().add(btnTransactions);
		
		JLabel lblNewLabel_1 = new JLabel("Here in the welcome center you can edit profile information, view balances and transactions, and transfer funds");
		lblNewLabel_1.setFont(new Font("Tahoma", Font.PLAIN, 10));
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.LEFT);
		lblNewLabel_1.setVerticalAlignment(SwingConstants.TOP);
		lblNewLabel_1.setBounds(40, 52, 534, 23);
		frmBanker.getContentPane().add(lblNewLabel_1);
		
		JLabel lblNewLabel_2 = new JLabel("View and customize your user profile");
		lblNewLabel_2.setBounds(205, 111, 180, 14);
		frmBanker.getContentPane().add(lblNewLabel_2);
		
		JLabel lblNewLabel_3 = new JLabel("View Checking and Saving balance");
		lblNewLabel_3.setBounds(205, 161, 180, 14);
		frmBanker.getContentPane().add(lblNewLabel_3);
		
		JLabel lblNewLabel_5 = new JLabel("Check past and pending transactions");
		lblNewLabel_5.setBounds(205, 216, 180, 14);
		frmBanker.getContentPane().add(lblNewLabel_5);
		
		JTextArea txtrCustomerName = new JTextArea();
		txtrCustomerName.setEditable(false);
		txtrCustomerName.setFont(new Font("Tahoma", Font.BOLD, 11));
		txtrCustomerName.setBackground(UIManager.getColor("Button.background"));
		txtrCustomerName.setText("Customer Name");
		txtrCustomerName.setBounds(96, 25, 215, 22);
		frmBanker.getContentPane().add(txtrCustomerName);
		
		JButton btnNewButton_1 = new JButton("Sign out");
		btnNewButton_1.setBounds(485, 316, 89, 23);
		frmBanker.getContentPane().add(btnNewButton_1);
	}
}
