from PySide6.QtWidgets import QMainWindow, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 300, 400)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.show()
