from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow 
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mortgage Calculator")

app = QApplication([])

window = MainWindow()

window.show()

app.exec()
