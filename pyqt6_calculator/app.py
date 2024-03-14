from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mortgage Calculator")
        self.setMinimumSize(QSize(450,500 ))

        main_layout = QVBoxLayout()

        main = QWidget()
        main.setLayout(main_layout)

        self.setCentralWidget(main)

        header = QLabel("Mortgage Calculator")
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        header.setFont(QFont("Helvetica", 25))
        main_layout.addWidget(header)

        calculator_container = QWidget()
        calculator_layout = QHBoxLayout()
        calculator_container.setLayout(calculator_layout)

        main_layout.addWidget(calculator_container)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()
