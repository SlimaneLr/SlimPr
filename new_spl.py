import pandas as pd
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QColor
import sys


class MainWindow(QtWidgets.QMainWindow): 
    
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("./new_spl_ui.ui", self)
        
        self.Open_file = self.findChild(QtWidgets.QPushButton, "Open_file")
        self.Split_data = self.findChild(QtWidgets.QPushButton, "Split_data")
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, "tableWidget")
        
        self.spinBox = self.findChild(QtWidgets.QSpinBox, "spinBox")
        self.Real_data = self.findChild(QtWidgets.QCheckBox, "Real_data")
        self.X_train = self.findChild(QtWidgets.QCheckBox, "X_train")
        self.Y_train = self.findChild(QtWidgets.QCheckBox, "Y_train")
        self.X_test = self.findChild(QtWidgets.QCheckBox, "X_test")
        self.Y_test = self.findChild(QtWidgets.QCheckBox, "Y_test")
        
        
        self.Open_file.clicked.connect(self.load_file)
        self.Split_data.clicked.connect(self.split_data)
        
    def alert_(self, message):
        alert = QMessageBox()
        alert.setWindowTitle("alert")
        alert.setText(message)
        alert.exec()
        
    
    def load_file(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '', 'CSV Files (*.csv)')
        if not filePath:
            return
        if filePath.endswith('.csv'):
            df = pd.read_csv(filePath)
        else:
            raise ValueError("Unsupported file format")

        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(df.iloc[row, col])))
                self.tableWidget.item(row, col).setBackground(QColor(171,255,191))
                
    def split_data(self):
        spl_value = int(self.spinBox.text())
        self.spinBox.setValue(0)
        if(spl_value > 30):
            self.alert_("Testing value must be less than 30%")
        
        
        
        test_rows = spl_value * self.tableWidget.rowCount() / 100
        print(self.tableWidget.item(0,0).background().color().name())
        self.tableWidget.item(0,0).setBackground()
        
        
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())