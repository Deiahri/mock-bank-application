package testPackage;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.Font;

public class userProfile {

	private JFrame frmUserProfile;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					userProfile window = new userProfile();
					window.frmUserProfile.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public userProfile() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmUserProfile = new JFrame();
		frmUserProfile.setResizable(false);
		frmUserProfile.setTitle("User Profile");
		frmUserProfile.setBounds(100, 100, 600, 400);
		frmUserProfile.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmUserProfile.getContentPane().setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Profile Information");
		lblNewLabel.setFont(new Font("Tahoma", Font.BOLD, 20));
		lblNewLabel.setBounds(10, 11, 212, 25);
		frmUserProfile.getContentPane().add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("Name");
		lblNewLabel_1.setBounds(31, 68, 46, 14);
		frmUserProfile.getContentPane().add(lblNewLabel_1);
		
		JLabel lblNewLabel_1_1 = new JLabel("Address");
		lblNewLabel_1_1.setBounds(31, 93, 46, 14);
		frmUserProfile.getContentPane().add(lblNewLabel_1_1);
		
		JLabel lblNewLabel_1_2 = new JLabel("Email");
		lblNewLabel_1_2.setBounds(31, 118, 46, 14);
		frmUserProfile.getContentPane().add(lblNewLabel_1_2);
		
		JLabel lblNewLabel_1_3 = new JLabel("Phone");
		lblNewLabel_1_3.setBounds(31, 143, 46, 14);
		frmUserProfile.getContentPane().add(lblNewLabel_1_3);
		
		JLabel lblNewLabel_1_3_1 = new JLabel("Customer Since");
		lblNewLabel_1_3_1.setBounds(31, 168, 94, 14);
		frmUserProfile.getContentPane().add(lblNewLabel_1_3_1);
	}

}
