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
    QDoubleSpinBox,
    QLabel,
    
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mortgage Calculator")
        self.setMinimumSize(QSize(600,200 ))

        main_layout = QGridLayout()

        main = QWidget()
        main.setLayout(main_layout)

        self.setCentralWidget(main)
        
        # Header...
        header = QLabel("Mortgage Calculator")
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        header.setFont(QFont("Helvetica", 25))
        main_layout.addWidget(header, 0, 0, 1, 5)
        
        loan_amount_groupBox = QGroupBox("Loan Amount")
        loan_amount_groupBox_layout = QVBoxLayout()
        loan_amount_groupBox.setLayout(loan_amount_groupBox_layout)
     
        loan_amount_doubleSpinBox = QDoubleSpinBox()
        loan_amount_doubleSpinBox.setMinimum(0.0)
        loan_amount_doubleSpinBox.setMaximum(float("inf"))
        loan_amount_doubleSpinBox.setPrefix("$ ")
        loan_amount_doubleSpinBox.setSingleStep(1000.0)
        loan_amount_doubleSpinBox.setMaximumSize(200, 50)
        
        loan_amount_groupBox_layout.addWidget(loan_amount_doubleSpinBox)
        main_layout.addWidget(loan_amount_groupBox, 1, 0, 1, 2)
        
        down_amount_groupBox = QGroupBox("Down Amount")
        down_amount_groupBox_layout = QHBoxLayout()
        down_amount_groupBox.setLayout(down_amount_groupBox_layout)
        
        down_amount_doubleSpinBox = QDoubleSpinBox()
        down_amount_doubleSpinBox.setMinimum(0,0)
        down_amount_doubleSpinBox.setMaximum()
        
        
        
        


app = QApplication([])

window = MainWindow()

window.show()

app.exec()
