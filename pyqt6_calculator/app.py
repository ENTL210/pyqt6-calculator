from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QWidget,
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
        
        loan_amount_label = QLabel("Loan Amount")
        loan_amount_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        loan_amount_label.setFont(QFont("Helvetica", 18))
        main_layout.addWidget(loan_amount_label, 1, 0)
        
        loan_amount_doubleSpinBox = QDoubleSpinBox()
        loan_amount_doubleSpinBox.setMinimum(0.0)
        loan_amount_doubleSpinBox.setMaximum(float("inf"))
        loan_amount_doubleSpinBox.setPrefix("$ ")
        loan_amount_doubleSpinBox.setSingleStep(1000.0)
        loan_amount_doubleSpinBox.setMaximumSize(200, 50)
        loan_amount_doubleSpinBox.setFont(QFont("Helvetica", 15))
        
        main_layout.addWidget(loan_amount_doubleSpinBox, 2, 0, 1, 2)
        
        
        
        


app = QApplication([])

window = MainWindow()

window.show()

app.exec()
