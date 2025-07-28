
from curses import window
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.show()
    app.exec()
