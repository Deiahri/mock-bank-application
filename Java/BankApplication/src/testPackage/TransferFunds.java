package testPackage;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JSpinner;
import javax.swing.JToggleButton;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;

public class TransferFunds {

	private JFrame frmTransferHub;
	private JTextField textField;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					TransferFunds window = new TransferFunds();
					window.frmTransferHub.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public TransferFunds() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmTransferHub = new JFrame();
		frmTransferHub.setTitle("Transfer Hub");
		frmTransferHub.setResizable(false);
		frmTransferHub.setBounds(100, 100, 600, 400);
		frmTransferHub.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmTransferHub.getContentPane().setLayout(null);
		
		JButton btnNewButton = new JButton("Transfer ");
		btnNewButton.setBounds(241, 282, 89, 23);
		frmTransferHub.getContentPane().add(btnNewButton);
		
		textField = new JTextField();
		textField.setBounds(304, 206, 86, 20);
		frmTransferHub.getContentPane().add(textField);
		textField.setColumns(10);
		
		JLabel lblNewLabel = new JLabel("Transfer Amount\r\n");
		lblNewLabel.setBounds(163, 209, 131, 14);
		frmTransferHub.getContentPane().add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("From");
		lblNewLabel_1.setBounds(156, 75, 46, 14);
		frmTransferHub.getContentPane().add(lblNewLabel_1);
		
		JLabel lblNewLabel_1_1 = new JLabel("To");
		lblNewLabel_1_1.setBounds(156, 124, 46, 14);
		frmTransferHub.getContentPane().add(lblNewLabel_1_1);
		
		JComboBox comboBox = new JComboBox();
		comboBox.setModel(new DefaultComboBoxModel(new String[] {"Checkings", "Savings"}));
		comboBox.setToolTipText("");
		comboBox.setBounds(275, 71, 115, 22);
		frmTransferHub.getContentPane().add(comboBox);
		
		JComboBox comboBox_1 = new JComboBox();
		comboBox_1.setModel(new DefaultComboBoxModel(new String[] {"Savings", "Checkings"}));
		comboBox_1.setBounds(275, 120, 115, 22);
		comboBox_1.setSize(115,22);
		frmTransferHub.getContentPane().add(comboBox_1);
		System.out.println((String)comboBox_1.getSelectedItem());
	}
}
