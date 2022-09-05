from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMenu, QMenuBar, QFileDialog, QMessageBox
import project1 as f

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Creating MenuBar
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        fileMenu = QMenu("File", self)
        self.menuBar.addMenu(fileMenu)
        fileMenu.addAction("Open", self.menu_action_clicked)

        self.setWindowTitle('Areg.zip')
        v_layout = QVBoxLayout()
        self.btn1 = QtWidgets.QPushButton('Compress')
        self.btn1.setStyleSheet("background-color: rgb(150,150,150);")
        self.btn2 = QtWidgets.QPushButton('Decompress')
        self.btn2.setStyleSheet("background-color: rgb(150,150,150);")
        v_layout.addWidget(self.btn1)
        v_layout.addWidget(self.btn2)
        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)
        self.btn1.clicked.connect(self.compressed)
        self.btn2.clicked.connect(self.decompressed)
        

        # Error box
        self.error = QMessageBox()
        self.error.setWindowTitle("Error")
        self.error.setText("File will be ended for .txt: ")
        self.error.setIcon(QMessageBox.Warning)
        
    @QtCore.pyqtSlot()
    def menu_action_clicked(self):
        self.fname = QFileDialog.getOpenFileName(self)[0]
        if ".txt" not in self.fname:
            self.error.exec_()


    def compressed(self):
        f.myFile()
               
    def decompressed(self):
        f.currentFile()





app = QApplication([])
window = Window()
window.show()
app.exec_()





    