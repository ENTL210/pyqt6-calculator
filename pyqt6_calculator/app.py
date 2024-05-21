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
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mortgage Calculator")

        self.UiComponents()
        
    def UiComponents(self):

        self.main = QWidget()
        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(40)
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.main.setLayout(self.main_layout)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(self.main)
        
        # Header...
        self.header = QLabel("Mortgage Calculator")
        self.header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.header.setFont(QFont("Helvetica", 15))
        self.main_layout.addWidget(self.header, 0, 0, 1, 5)
        
        self.loan_amount_groupBox = QGroupBox("Loan Amount")
        self.loan_amount_groupBox_layout = QVBoxLayout()
        self.loan_amount_groupBox.setLayout(self.loan_amount_groupBox_layout)
     
        self.loan_amount_doubleSpinBox = QDoubleSpinBox()
        self.loan_amount_doubleSpinBox.setMinimum(0.0)
        self.loan_amount_doubleSpinBox.setMaximum(float("inf"))
        self.loan_amount_doubleSpinBox.setPrefix("$ ")
        self.loan_amount_doubleSpinBox.setFont(QFont("Helvetica", 10))
        self.loan_amount_doubleSpinBox.setSingleStep(1000.0)
        self.loan_amount_doubleSpinBox.setMinimumSize(200, 50)
        self.loan_amount_doubleSpinBox.valueChanged.connect(self.update_down_payment_value)
        
        self.loan_amount_groupBox_layout.addWidget(self.loan_amount_doubleSpinBox)
        self.main_layout.addWidget(self.loan_amount_groupBox, 1, 0, 1, 2)
        
        self.down_amount_groupBox = QGroupBox("Down Amount")
        self.down_amount_groupBox_layout = QHBoxLayout()
        self.down_amount_groupBox.setLayout(self.down_amount_groupBox_layout)
        
        self.down_amount_doubleSpinBox = QDoubleSpinBox()
        self.down_amount_doubleSpinBox.setMinimum(0.0)
        self.down_amount_doubleSpinBox.setMaximum(self.loan_amount_doubleSpinBox.value())
        self.down_amount_doubleSpinBox.setPrefix("$ ")
        self.down_amount_doubleSpinBox.setFont(QFont("Helvetica", 10))
        self.down_amount_doubleSpinBox.setSingleStep(1000.0)
        self.down_amount_doubleSpinBox.setMinimumSize(200, 50)
        self.down_amount_doubleSpinBox.valueChanged.connect(self.update_down_percent_value)
        
        self.down_percent_doubleSpinBox = QDoubleSpinBox()
        self.down_percent_doubleSpinBox.setMinimum(5)
        self.down_percent_doubleSpinBox.setMaximum(100)
        self.down_percent_doubleSpinBox.setSuffix(" %")
        self.down_percent_doubleSpinBox.setFont(QFont("Helvetica", 10))
        self.down_percent_doubleSpinBox.setSingleStep(5)
        self.down_percent_doubleSpinBox.setMinimumSize(100,50)
        self.down_percent_doubleSpinBox.valueChanged.connect(self.update_down_payment_value)
        
        self.down_amount_groupBox_layout.addWidget(self.down_amount_doubleSpinBox)
        self.down_amount_groupBox_layout.addWidget(self.down_percent_doubleSpinBox)
        self.main_layout.addWidget(self.down_amount_groupBox, 2, 0, 1, 2)
        
        self.loan_duration_groupBox = QGroupBox("Loan Duration")
        self.loan_duration_groupBox_layout = QVBoxLayout()
        self.loan_duration_groupBox.setLayout(self.loan_duration_groupBox_layout)
        
        self.loan_duration_comboBox = QComboBox()
        self.loan_duration_comboBox.addItems(["10 years", "15 years", "20 years", "30 years"])
        self.loan_duration_comboBox.setMinimumSize(200, 50)
        self.loan_duration_comboBox.setFont(QFont("Helvetica", 10))
        
        self.loan_duration_groupBox_layout.addWidget(self.loan_duration_comboBox)
        self.main_layout.addWidget(self.loan_duration_groupBox, 3, 0, 1, 2)
        
        self.interest_rate_groupBox = QGroupBox("Interest Rate")
        self.interest_rate_groupBox_layout = QHBoxLayout()
        self.interest_rate_groupBox.setLayout(self.interest_rate_groupBox_layout)
        
        self.interest_rate_doubleSpinBox = QDoubleSpinBox()
        self.interest_rate_doubleSpinBox.setMinimum(0.0)
        self.interest_rate_doubleSpinBox.setSuffix(" %")
        self.interest_rate_doubleSpinBox.setFont(QFont("Helvetica", 10))
        self.interest_rate_doubleSpinBox.setSingleStep(0.1)
        self.interest_rate_doubleSpinBox.setMinimumSize(200, 50)
        
        self.interest_rate_groupBox_layout.addWidget(self.interest_rate_doubleSpinBox)
        self.main_layout.addWidget(self.interest_rate_groupBox, 4, 0, 1, 2)
        
        self.calculate_pushBtn = QPushButton("Calculate")
        self.calculate_pushBtn.setMinimumSize(250, 50)
        self.calculate_pushBtn.clicked.connect(self.calculate_output)
        self.main_layout.addWidget(self.calculate_pushBtn, 5, 0, 1, 2)
        
        self.line = QFrame()
        self.line.setGeometry(QRect(60, 110, 751, 20))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.main_layout.addWidget(self.line, 1, 2, 5, 1)
        
        self.output_container = QWidget() 
        self.output_container_layout = QVBoxLayout()
        self.output_container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_container.setLayout(self.output_container_layout)
        self.output_container.setMinimumSize(400, 500)
        self.main_layout.addWidget(self.output_container, 1, 3, 5, 2)
        
        self.monthy_payment_label = QLabel("Monthly Payment")
        self.monthy_payment_label.setFont(QFont("Helvetica", 12))
        self.monthy_payment_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.output_container_layout.addWidget(self.monthy_payment_label)
        
        self.monthly_payment_output_label = QLabel("N/A")
        self.monthly_payment_output_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.monthly_payment_output_label.setFont(QFont("Helvetica", 12))
        self.output_container_layout.addWidget(self.monthly_payment_output_label)
        

    def update_down_payment_value(self):
        # Fetch value from the users...
        loan_amount = self.loan_amount_doubleSpinBox.value()
        down_percent = self.down_percent_doubleSpinBox.value()

        # Update the maximum of down amount and the down amount value...
        self.down_amount_doubleSpinBox.setMaximum(loan_amount)
        self.down_amount_doubleSpinBox.setValue(loan_amount * (down_percent / 100))


    def update_down_percent_value(self):
        # Fetch value from the users...
        loan_amount = self.loan_amount_doubleSpinBox.value()
        down_payment = self.down_amount_doubleSpinBox.value()

        if loan_amount == 0:
            self.down_percent_doubleSpinBox.setValue(5)
            self.update_down_payment_value()
        else:
            self.down_percent_doubleSpinBox.setValue(round(((down_payment / loan_amount) * 100), 2))

    def calculate_output(self):
        total_loan_amount = self.loan_amount_doubleSpinBox.value() - self.down_amount_doubleSpinBox.value()
        monthly_interest_rate = (self.interest_rate_doubleSpinBox.value() / 100) / 12
        number_of_payments_arr = [120, 180, 240, 360]
        number_of_payments = number_of_payments_arr[self.loan_duration_comboBox.currentIndex()]
        monthly_mortgage_payment = total_loan_amount * ((monthly_interest_rate * ((1 + monthly_interest_rate) ** number_of_payments)) / (((1 + monthly_interest_rate) ** number_of_payments) - 1))
        self.monthly_payment_output_label.setText(f"${round(monthly_mortgage_payment, 2)}")


app = QApplication([])

window = MainWindow()

window.show()

app.exec()
