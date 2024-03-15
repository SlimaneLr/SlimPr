import pandas as pd
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtWidgets import QMessageBox, QButtonGroup
from PyQt6.QtGui import QColor
from random import randrange
import sys
# hehehehe

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("./new_spl_ui.ui", self)

        self.Open_file = self.findChild(QtWidgets.QPushButton, "Open_file")
        self.Split_data = self.findChild(QtWidgets.QPushButton, "Split_data")
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, "tableWidget")

        self.spinBox = self.findChild(QtWidgets.QSpinBox, "spinBox")
        self.Real_data = self.findChild(QtWidgets.QRadioButton, "Real_data")
        self.X_train = self.findChild(QtWidgets.QRadioButton, "X_train")
        self.Y_train = self.findChild(QtWidgets.QRadioButton, "Y_train")
        self.X_test = self.findChild(QtWidgets.QRadioButton, "X_test")
        self.Y_test = self.findChild(QtWidgets.QRadioButton, "Y_test")

        self.Open_file.clicked.connect(self.load_file)
        self.Split_data.clicked.connect(self.split_data)

        self.Real_data.setEnabled(False)
        self.X_train.setEnabled(False)
        self.Y_train.setEnabled(False)
        self.X_test.setEnabled(False)
        self.Y_test.setEnabled(False)

        self.Real_data.toggled.connect(self.update_table_real_data)
        self.X_test.toggled.connect(self.update_table_x_test)
        self.X_train.toggled.connect(self.update_table_x_train)
        self.Y_test.toggled.connect(self.update_table_y_test)
        self.Y_train.toggled.connect(self.update_table_y_train)

    def alert_(self, message):
        alert = QMessageBox()
        alert.setWindowTitle("Alert")
        alert.setText(message)
        alert.exec()

    def load_file(self):
        self.Real_data.setChecked(False)
        self.X_train.setChecked(False)
        self.Y_train.setChecked(False)
        self.X_test.setChecked(False)
        self.Y_test.setChecked(False)
        
        
        self.Real_data.setEnabled(False)
        self.X_train.setEnabled(False)
        self.Y_train.setEnabled(False)
        self.X_test.setEnabled(False)
        self.Y_test.setEnabled(False)
        
        
        
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '', 'CSV Files (*.csv)')
        if not filePath:
            return
        if filePath.endswith('.csv'):
            self.df = pd.read_csv(filePath)
        else:
            raise ValueError("Unsupported file format")
        self.tableWidget.setRowCount(self.df.shape[0])
        self.tableWidget.setColumnCount(self.df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(self.df.columns)

        for row in range(self.df.shape[0]):
            for col in range(self.df.shape[1]):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(self.df.iloc[row, col])))
                self.tableWidget.item(row, col).setBackground(QColor(171, 255, 191))
                
        self.tableWidget.setColumnWidth(0, 140)
        self.tableWidget.setColumnWidth(1, 140)
        self.tableWidget.setColumnWidth(2, 140)
        self.tableWidget.setColumnWidth(3, 140)
        self.tableWidget.setColumnWidth(4, 140)
        self.tableWidget.setColumnWidth(5, 140)
        self.tableWidget.setColumnWidth(6, 140)
        self.tableWidget.setColumnWidth(7, 140)
        self.tableWidget.setColumnWidth(8, 140)
        self.tableWidget.setColumnWidth(9, 80)
        
        
        

    def split_data(self):
        
        spl_value = int(self.spinBox.text())
        self.spinBox.setValue(0)
        for row in range(self.df.shape[0]):
            for col in range(self.df.shape[1]):
                self.tableWidget.item(row, col).setBackground(QColor(171, 255, 191))
                
        if spl_value > 30 or spl_value == 0:
            self.alert_("Testing value must be less than 30% " + "and greater than 0%")
        else:
            self.Real_data.setChecked(True)
            self.Real_data.setEnabled(True)
            self.X_train.setEnabled(True)
            self.Y_train.setEnabled(True)
            self.X_test.setEnabled(True)
            self.Y_test.setEnabled(True)
            test_rows = spl_value * self.tableWidget.rowCount() / 100
            print(int(test_rows))
            for i in range(int(test_rows)):
                rn = randrange(self.tableWidget.rowCount())
                col = self.tableWidget.columnCount()-1
                while self.tableWidget.item(rn, 0).background().color().name() == "#f2ffab" :
                    print(rn)
                    rn = randrange(self.tableWidget.rowCount())
                    print("false random.........................")
                for c in range(int(col)):
                    if self.tableWidget.item(rn, c).background().color().name() == "#abffbf":
                        self.tableWidget.item(rn, c).setBackground(QColor(242, 255, 171))
                    
            self.alert_("data splited")
                        
                        
    def update_table_real_data(self):
        rb = self.sender()
        if rb.isChecked():
            print("real data checked")

    def update_table_x_test(self):
        rb = self.sender()
        if rb.isChecked():
            print("x_test checked")

    def update_table_y_test(self):
        rb = self.sender()
        if rb.isChecked():
            print("y_test checked")

    def update_table_x_train(self):
        rb = self.sender()
        if rb.isChecked():
            print("x_train checked")
    
    def update_table_y_train(self):
        rb = self.sender()
        if rb.isChecked():
            print("y_train checked")

                        
                

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
