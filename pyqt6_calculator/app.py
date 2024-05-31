import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, Qt, QRect
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget,
    QGroupBox,
    QSpinBox,
    QDoubleSpinBox,
    QLabel,
    QComboBox,
    QPushButton,
    QFrame,
)
from controller import (
    down_amount_calculation, 
    down_percent_calculation, 
    output_calculation, 
    convertToStringOutput
)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mortgage Calculator")

        # Call the main UI...
        self.UiComponents()
        
    def UiComponents(self):
        """
        A function that render out the UI of the app
        """

        # Main container...
        self.main = QWidget()
        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(40)
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.main.setLayout(self.main_layout)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set the container as the main widget of the window...
        self.setCentralWidget(self.main)
        
        # Header...
        self.header = QLabel("Mortgage Calculator", objectName="header")
        self.header.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(self.header, 0, 0, 1, 5)
        
        # Loan Amount Entrybox Container...
        self.loan_amount_groupBox = QGroupBox("Loan Amount")
        self.loan_amount_groupBox_layout = QVBoxLayout()
        self.loan_amount_groupBox.setLayout(self.loan_amount_groupBox_layout)

        # Loan Amount Entrybox...
        self.loan_amount_doubleSpinBox = QDoubleSpinBox()
        
        # Set the parameters of the entrybox...
        self.loan_amount_doubleSpinBox.setMinimum(0.0)
        self.loan_amount_doubleSpinBox.setMaximum(float("inf"))
        self.loan_amount_doubleSpinBox.setPrefix("$ ")
        self.loan_amount_doubleSpinBox.setFont(QFont("Helvetica", 12))
        self.loan_amount_doubleSpinBox.setSingleStep(1000.0)
        self.loan_amount_doubleSpinBox.setMinimumSize(200, 50)
        
        # When the loan amount entrybox's value is changing...
        self.loan_amount_doubleSpinBox.valueChanged.connect(self.update_down_payment_value)
        
        # Add the loan entrybox to the layout...
        self.loan_amount_groupBox_layout.addWidget(self.loan_amount_doubleSpinBox)
        self.main_layout.addWidget(self.loan_amount_groupBox, 1, 0, 1, 2)
        
        # Create down amount entrybox container...
        self.down_amount_groupBox = QGroupBox("Down Amount")
        self.down_amount_groupBox_layout = QHBoxLayout()
        self.down_amount_groupBox.setLayout(self.down_amount_groupBox_layout)
        
        # Create down amount entrybox...
        self.down_amount_doubleSpinBox = QDoubleSpinBox()
        
        # Set the parameters of the entrybox...
        self.down_amount_doubleSpinBox.setMinimum(0.0)
        self.down_amount_doubleSpinBox.setMaximum(self.loan_amount_doubleSpinBox.value())
        self.down_amount_doubleSpinBox.setPrefix("$ ")
        self.down_amount_doubleSpinBox.setFont(QFont("Helvetica", 12))
        self.down_amount_doubleSpinBox.setSingleStep(1000.0)
        self.down_amount_doubleSpinBox.setMinimumSize(200, 50)
        
        # When the down amount is changing...
        self.down_amount_doubleSpinBox.valueChanged.connect(self.update_down_percent_value)
        
        # Create down percent entrybox...
        self.down_percent_doubleSpinBox = QDoubleSpinBox()
        
        # Set the parameters of the entrybox...
        self.down_percent_doubleSpinBox.setMinimum(5)
        self.down_percent_doubleSpinBox.setMaximum(100)
        self.down_percent_doubleSpinBox.setSuffix(" %")
        self.down_percent_doubleSpinBox.setFont(QFont("Helvetica", 12))
        self.down_percent_doubleSpinBox.setSingleStep(5)
        self.down_percent_doubleSpinBox.setMinimumSize(100,50)
        
        # When the value of down percent is changing.
        self.down_percent_doubleSpinBox.valueChanged.connect(self.update_down_payment_value)
        
        # Add the down amount and down percent entrybox to the layout...
        self.down_amount_groupBox_layout.addWidget(self.down_amount_doubleSpinBox)
        self.down_amount_groupBox_layout.addWidget(self.down_percent_doubleSpinBox)
        self.main_layout.addWidget(self.down_amount_groupBox, 2, 0, 1, 2)
        
        # Create loan duration container...
        self.loan_duration_groupBox = QGroupBox("Loan Duration")
        self.loan_duration_groupBox_layout = QVBoxLayout()
        self.loan_duration_groupBox.setLayout(self.loan_duration_groupBox_layout)
        
        # Create loan duration entrybox
        self.loan_duration_comboBox = QComboBox()
        
        # Initialize the options for the combobox...
        self.loan_duration_comboBox.addItems(["10 years", "15 years", "20 years", "30 years"])
    
        
        # Add the combobox to the layout...
        self.loan_duration_groupBox_layout.addWidget(self.loan_duration_comboBox)
        self.main_layout.addWidget(self.loan_duration_groupBox, 3, 0, 1, 2)
        
        # Create interest rate entrybox container...
        self.interest_rate_groupBox = QGroupBox("Interest Rate")
        self.interest_rate_groupBox_layout = QHBoxLayout()
        self.interest_rate_groupBox.setLayout(self.interest_rate_groupBox_layout)
        
        # Create the interest rate entrybox...
        self.interest_rate_doubleSpinBox = QDoubleSpinBox()
        
        # Set the parameters of the entrybox...
        self.interest_rate_doubleSpinBox.setValue(7.67)
        self.interest_rate_doubleSpinBox.setMinimum(0.0)
        self.interest_rate_doubleSpinBox.setSuffix(" %")
        self.interest_rate_doubleSpinBox.setFont(QFont("Helvetica", 12))
        self.interest_rate_doubleSpinBox.setSingleStep(0.1)
        self.interest_rate_doubleSpinBox.setMinimumSize(200, 50)
        
        # Add the entrybox to the layout...
        self.interest_rate_groupBox_layout.addWidget(self.interest_rate_doubleSpinBox)
        self.main_layout.addWidget(self.interest_rate_groupBox, 4, 0, 1, 2)
        
        # Create the calculate button...
        self.calculate_pushBtn = QPushButton("Calculate")
        
        # Set the parameters of the button...
        self.calculate_pushBtn.setMinimumSize(250, 50)
        
        # When the button is being tapped...
        self.calculate_pushBtn.clicked.connect(self.calculate_output)
        
        # Add the button to the layout
        self.main_layout.addWidget(self.calculate_pushBtn, 5, 0, 1, 2)
        
        # Create a vertical line...
        self.line = QFrame()
        self.line.setGeometry(QRect(60, 110, 751, 20))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        
        # Add the line to the layout...
        self.main_layout.addWidget(self.line, 1, 2, 5, 1)
        
        # Create the output container...
        self.output_container = QWidget() 
        
        # Set the parameters of the output container...
        self.output_container_layout = QVBoxLayout()
        self.output_container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_container.setLayout(self.output_container_layout)
        self.output_container.setMinimumSize(400, 500)
        
        # Add the output container to the layout...
        self.main_layout.addWidget(self.output_container, 1, 3, 5, 2)
        
        # Create the output label...
        self.monthy_payment_label = QLabel("Monthly Payment", objectName="output_label")
        self.monthly_payment_output_label = QLabel("N/A", objectName="output")
    
        # Set the parameters of the labels...
        self.monthy_payment_label.setFont(QFont("Helvetica", 15))
        self.monthy_payment_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.monthly_payment_output_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.monthly_payment_output_label.setFont(QFont("Helvetica", 18))
        
        # Add the labels to the layout...
        self.output_container_layout.addWidget(self.monthy_payment_label)
        self.output_container_layout.addWidget(self.monthly_payment_output_label)
        
    def update_down_payment_value(self):
        """Update the down amount when the down % is changing..."""
        loan_amount = self.loan_amount_doubleSpinBox.value()
        down_percent = self.down_percent_doubleSpinBox.value()

        # Update the maximum of down amount and the down amount value...
        self.down_amount_doubleSpinBox.setMaximum(loan_amount)
        self.down_amount_doubleSpinBox.setValue(down_amount_calculation(loan_amount, down_percent))

    def update_down_percent_value(self):
        """Update the down percent when the down amount is changing..."""
        loan_amount = self.loan_amount_doubleSpinBox.value()
        down_payment = self.down_amount_doubleSpinBox.value()

        if loan_amount == 0:
            self.down_percent_doubleSpinBox.setValue(5)
            self.update_down_payment_value()
        else:
            self.down_percent_doubleSpinBox.setValue(down_percent_calculation(down_payment, loan_amount))

    def calculate_output(self):
        """Calculate the output when the calculate button is being tapped..."""
        output = output_calculation(
            self.loan_amount_doubleSpinBox.value(),
            self.down_amount_doubleSpinBox.value(),
            self.interest_rate_doubleSpinBox.value(),
            self.loan_duration_comboBox.currentIndex()
        )
        
        self.monthly_payment_output_label.setText(convertToStringOutput(output))

app = QApplication([])

# Apply styles to the application...
with open("styles.css", "r") as file:
    styles = file.read()
    app.setStyleSheet(styles)
    

# Create the primary window...
window = MainWindow()

# Show the window...
window.show()

app.exec()
