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
    QFrame
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
        self.header.setFont(QFont("Helvetica", 25))
        self.main_layout.addWidget(self.header, 0, 0, 1, 5)
        
        self.loan_amount_groupBox = QGroupBox("Loan Amount")
        self.loan_amount_groupBox_layout = QVBoxLayout()
        self.loan_amount_groupBox.setLayout(self.loan_amount_groupBox_layout)
     
        self.loan_amount_doubleSpinBox = QDoubleSpinBox()
        self.loan_amount_doubleSpinBox.setMinimum(0.0)
        self.loan_amount_doubleSpinBox.setMaximum(float("inf"))
        self.loan_amount_doubleSpinBox.setPrefix("$ ")
        self.loan_amount_doubleSpinBox.setFont(QFont("Helvetica", 15))
        self.loan_amount_doubleSpinBox.setSingleStep(1000.0)
        self.loan_amount_doubleSpinBox.setMinimumSize(200, 50)
        self.loan_amount_doubleSpinBox.valueChanged.connect(self.set_down_payment_max)
        
        self.loan_amount_groupBox_layout.addWidget(self.loan_amount_doubleSpinBox)
        self.main_layout.addWidget(self.loan_amount_groupBox, 1, 0, 1, 2)
        
        self.down_amount_groupBox = QGroupBox("Down Amount")
        self.down_amount_groupBox_layout = QHBoxLayout()
        self.down_amount_groupBox.setLayout(self.down_amount_groupBox_layout)
        
        self.down_amount_doubleSpinBox = QDoubleSpinBox()
        self.down_amount_doubleSpinBox.setMinimum(0.0)
        self.down_amount_doubleSpinBox.setMaximum(self.loan_amount_doubleSpinBox.value())
        self.down_amount_doubleSpinBox.setPrefix("$ ")
        self.down_amount_doubleSpinBox.setFont(QFont("Helvetica", 15))
        self.down_amount_doubleSpinBox.setSingleStep(1000.0)
        self.down_amount_doubleSpinBox.setMinimumSize(200, 50)
        
        self.down_percent_spinBox = QSpinBox()
        self.down_percent_spinBox.setMinimum(5)
        self.down_percent_spinBox.setMaximum(100)
        self.down_percent_spinBox.setSuffix(" %")
        self.down_percent_spinBox.setFont(QFont("Helvetica", 15))
        self.down_percent_spinBox.setSingleStep(5)
        self.down_percent_spinBox.setMinimumSize(100,50)
        
        self.down_amount_groupBox_layout.addWidget(self.down_amount_doubleSpinBox)
        self.down_amount_groupBox_layout.addWidget(self.down_percent_spinBox)
        self.main_layout.addWidget(self.down_amount_groupBox, 2, 0, 1, 2)
        
        self.loan_duration_groupBox = QGroupBox("Loan Duration")
        self.loan_duration_groupBox_layout = QVBoxLayout()
        self.loan_duration_groupBox.setLayout(self.loan_duration_groupBox_layout)
        
        self.loan_duration_comboBox = QComboBox()
        self.loan_duration_comboBox.addItems(["10 years", "15 years", "20 years", "30 years"])
        self.loan_duration_comboBox.setMinimumSize(200, 50)
        
        self.loan_duration_groupBox_layout.addWidget(self.loan_duration_comboBox)
        self.main_layout.addWidget(self.loan_duration_groupBox, 3, 0, 1, 2)
        
        self.interest_rate_groupBox = QGroupBox("Interest Rate")
        self.interest_rate_groupBox_layout = QHBoxLayout()
        self.interest_rate_groupBox.setLayout(self.interest_rate_groupBox_layout)
        
        self.interest_rate_doubleSpinBox = QDoubleSpinBox()
        self.interest_rate_doubleSpinBox.setMinimum(0.0)
        self.interest_rate_doubleSpinBox.setSuffix(" %")
        self.interest_rate_doubleSpinBox.setFont(QFont("Helvetica", 15))
        self.interest_rate_doubleSpinBox.setSingleStep(0.1)
        self.interest_rate_doubleSpinBox.setMinimumSize(200, 50)
        
        self.interest_rate_groupBox_layout.addWidget(self.interest_rate_doubleSpinBox)
        self.main_layout.addWidget(self.interest_rate_groupBox, 4, 0, 1, 2)
        
        self.calculate_pushBtn = QPushButton("Calculate")
        self.calculate_pushBtn.setMinimumSize(250, 50)
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
        self.monthy_payment_label.setFont(QFont("Helvetica", 20))
        self.monthy_payment_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.output_container_layout.addWidget(self.monthy_payment_label)
        
        self.monthly_payment_output_label = QLabel("N/A")
        self.monthly_payment_output_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.monthly_payment_output_label.setFont(QFont("Helvetica", 20))
        self.output_container_layout.addWidget(self.monthly_payment_output_label)
        
        
        
        
    def set_down_payment_max(self):
        value = self.loan_amount_doubleSpinBox.value()
        self.down_amount_doubleSpinBox.setMaximum(value)
        self.down_amount_doubleSpinBox.setValue(value * 0.05)
        


app = QApplication([])

window = MainWindow()

window.show()

app.exec()
