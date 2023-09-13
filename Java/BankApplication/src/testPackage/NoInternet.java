package testPackage;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class NoInternet {

	private JFrame frmBanker;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					NoInternet window = new NoInternet();
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
	public NoInternet() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmBanker = new JFrame();
		frmBanker.setTitle("Welcome");
		frmBanker.setBounds(100, 100, 390, 260);
		frmBanker.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmBanker.getContentPane().setLayout(null);
		
		JLabel lblNewLabel = new JLabel("No Internet");
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 14));
		lblNewLabel.setBounds(52, 67, 110, 21);
		frmBanker.getContentPane().add(lblNewLabel);
		
		JLabel image = new JLabel("");
		image.setFont(new Font("Tahoma", Font.PLAIN, 20));
		image.setBounds(206, 73, 110, 25);
		frmBanker.getContentPane().add(image);
		
		JButton btnCreateAccount = new JButton("Try Again");
		btnCreateAccount.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btnCreateAccount.setBounds(235, 187, 113, 23);
		frmBanker.getContentPane().add(btnCreateAccount);
		
		JLabel lblNewLabel_1 = new JLabel("Uh oh...");
		lblNewLabel_1.setFont(new Font("Tahoma", Font.BOLD, 20));
		lblNewLabel_1.setBounds(25, 23, 100, 35);
		frmBanker.getContentPane().add(lblNewLabel_1);
	}
}
