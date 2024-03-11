import pandas as pd
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtWidgets import QMessageBox, QButtonGroup
from PyQt6.QtGui import QColor
from random import randrange
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
        self.Split_data.setEnabled(False)

    def alert_(self, message):
        alert = QMessageBox()
        alert.setWindowTitle("Alert")
        alert.setText(message)
        alert.exec()

    def load_file(self):
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
        self.Split_data.setEnabled(True)

    def split_data(self):
        spl_value = int(self.spinBox.text())
        self.spinBox.setValue(0)
        self.Split_data.setEnabled(False)
        if spl_value > 30:
            self.alert_("Testing value must be less than 30%")
        else:
            test_rows = spl_value * self.tableWidget.rowCount() / 100
            print(int(test_rows))
            for i in range(int(test_rows)):
                rn = randrange(self.tableWidget.rowCount())
                col = self.tableWidget.columnCount()-1
                for c in range(int(col)):
                    if self.tableWidget.item(rn, c).background().color().name() == "#abffbf":
                        self.tableWidget.item(rn, c).setBackground(QColor(242, 255, 171))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
