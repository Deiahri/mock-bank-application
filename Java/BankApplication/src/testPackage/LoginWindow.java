package testPackage;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class LoginWindow {

	private JFrame frmBanker;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					LoginWindow window = new LoginWindow();
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
	public LoginWindow() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmBanker = new JFrame();
		frmBanker.setTitle("Welcome");
		frmBanker.setBounds(100, 100, 600, 400);
		frmBanker.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmBanker.getContentPane().setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Username");
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 20));
		lblNewLabel.setBounds(143, 122, 110, 21);
		frmBanker.getContentPane().add(lblNewLabel);
		
		JLabel lblPassword = new JLabel("Password");
		lblPassword.setFont(new Font("Tahoma", Font.PLAIN, 20));
		lblPassword.setBounds(143, 177, 110, 25);
		frmBanker.getContentPane().add(lblPassword);
		
		JTextArea textArea = new JTextArea();
		textArea.setBounds(307, 124, 141, 22);
		frmBanker.getContentPane().add(textArea);
		
		JTextArea textArea_1 = new JTextArea();
		textArea_1.setBounds(307, 177, 141, 22);
		frmBanker.getContentPane().add(textArea_1);
		
		JButton btnNewButton = new JButton("Login");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btnNewButton.setBounds(241, 213, 113, 23);
		frmBanker.getContentPane().add(btnNewButton);
		
		JButton btnForgotPassword = new JButton("Forgot Password");
		btnForgotPassword.setBounds(241, 247, 113, 21);
		frmBanker.getContentPane().add(btnForgotPassword);
		
		JButton btnCreateAccount = new JButton("Sign up");
		btnCreateAccount.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btnCreateAccount.setBounds(241, 279, 113, 23);
		frmBanker.getContentPane().add(btnCreateAccount);
		
		JLabel lblNewLabel_1 = new JLabel("Welcome!");
		lblNewLabel_1.setFont(new Font("Tahoma", Font.BOLD, 20));
		lblNewLabel_1.setBounds(233, 52, 100, 35);
		frmBanker.getContentPane().add(lblNewLabel_1);
	}
}
