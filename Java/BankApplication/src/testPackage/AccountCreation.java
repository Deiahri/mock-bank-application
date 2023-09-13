package testPackage;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.Font;
import javax.swing.JComboBox;

public class AccountCreation {

	private JFrame frmCreateANew;
	private JTextField usernameField;
	private JTextField passwordField;
	private JTextField nameField;
	private JTextField emailField;
	private JTextField addressField;
	private JTextField ssnField;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					AccountCreation window = new AccountCreation();
					window.frmCreateANew.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public AccountCreation() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmCreateANew = new JFrame();
		frmCreateANew.setResizable(false);
		frmCreateANew.setTitle("Create a New Account");
		frmCreateANew.setBounds(100, 100, 600, 400);
		frmCreateANew.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmCreateANew.getContentPane().setLayout(null);
		
		usernameField = new JTextField("");
		usernameField.setBounds(70, 115, 158, 20);
		frmCreateANew.getContentPane().add(usernameField);
		
		JLabel usernameLabel = new JLabel("Username");
		usernameLabel.setFont(new Font("Tahoma", Font.PLAIN, 12));
		usernameLabel.setBounds(70, 97, 158, 17);
		frmCreateANew.getContentPane().add(usernameLabel);
		
		JButton btnNewButton = new JButton("Create Account");
		btnNewButton.setBounds(367, 314, 130, 23);
		frmCreateANew.getContentPane().add(btnNewButton);
		
		JButton btnBack = new JButton("Back");
		btnBack.setBounds(59, 314, 107, 23);
		frmCreateANew.getContentPane().add(btnBack);
		
		JLabel lblNewLabel_1_1 = new JLabel("Sign-Up");
		lblNewLabel_1_1.setFont(new Font("Tahoma", Font.PLAIN, 20));
		lblNewLabel_1_1.setBounds(20, 14, 146, 35);
		frmCreateANew.getContentPane().add(lblNewLabel_1_1);
		
		JLabel lblPassword = new JLabel("Password");
		lblPassword.setFont(new Font("Tahoma", Font.PLAIN, 12));
		lblPassword.setBounds(70, 142, 158, 17);
		frmCreateANew.getContentPane().add(lblPassword);
		
		passwordField = new JTextField();
		passwordField.setColumns(10);
		passwordField.setBounds(70, 160, 158, 20);
		frmCreateANew.getContentPane().add(passwordField);
		
		JLabel lblName = new JLabel("Name");
		lblName.setFont(new Font("Tahoma", Font.PLAIN, 12));
		lblName.setBounds(70, 56, 158, 17);
		frmCreateANew.getContentPane().add(lblName);
		
		nameField = new JTextField();
		nameField.setColumns(10);
		nameField.setBounds(70, 74, 158, 20);
		frmCreateANew.getContentPane().add(nameField);
		
		JLabel lblEmail = new JLabel("Email");
		lblEmail.setFont(new Font("Tahoma", Font.PLAIN, 12));
		lblEmail.setBounds(303, 97, 158, 17);
		frmCreateANew.getContentPane().add(lblEmail);
		
		emailField = new JTextField();
		emailField.setColumns(10);
		emailField.setBounds(303, 115, 158, 20);
		frmCreateANew.getContentPane().add(emailField);
		
		JLabel lblAddress = new JLabel("Address");
		lblAddress.setFont(new Font("Tahoma", Font.PLAIN, 12));
		lblAddress.setBounds(303, 142, 158, 17);
		frmCreateANew.getContentPane().add(lblAddress);
		
		addressField = new JTextField();
		addressField.setColumns(10);
		addressField.setBounds(303, 160, 158, 20);
		frmCreateANew.getContentPane().add(addressField);
		
		JLabel lblSsn = new JLabel("SSN");
		lblSsn.setFont(new Font("Tahoma", Font.PLAIN, 12));
		lblSsn.setBounds(303, 56, 158, 17);
		frmCreateANew.getContentPane().add(lblSsn);
		
		ssnField = new JTextField();
		ssnField.setColumns(10);
		ssnField.setBounds(303, 74, 158, 20);
		frmCreateANew.getContentPane().add(ssnField);
	}
}
