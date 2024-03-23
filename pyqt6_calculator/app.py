from PyQt6.QtCore import QSize, Qt
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
    
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mortgage Calculator")

        self.UiComponents()
        
    def UiComponents(self):
        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(40)

        self.main = QWidget()
        self.main.setLayout(self.main_layout)

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
        self.down_percent_spinBox.setMinimum(0)
        self.down_percent_spinBox.setMaximum(100)
        self.down_percent_spinBox.setSuffix(" %")
        self.down_percent_spinBox.setFont(QFont("Helvetica", 15))
        self.down_percent_spinBox.setSingleStep(5)
        self.down_percent_spinBox.setMinimumSize(100,50)
        
        self.down_amount_groupBox_layout.addWidget(self.down_amount_doubleSpinBox)
        self.down_amount_groupBox_layout.addWidget(self.down_percent_spinBox)
        self.main_layout.addWidget(self.down_amount_groupBox, 2, 0, 1, 2)
        
    def set_down_payment_max(self):
        value = self.loan_amount_doubleSpinBox.value()
        self.down_amount_doubleSpinBox.setMaximum(value)
        self.down_amount_doubleSpinBox.setValue(value * 0.05)
        


app = QApplication([])

window = MainWindow()

window.show()

app.exec()
