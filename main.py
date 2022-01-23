import sys
from UI.creator.ui_opener import MainWindow
from PyQt5.QtWidgets import QApplication

def run():
    qt = QApplication(sys.argv)
    app = MainWindow
    app.show()
    qt.exec_()

if __name__ == '__main__':
    run()