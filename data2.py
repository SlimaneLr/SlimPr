import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.loadButton.clicked.connect(self.load_file)

    def load_file(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '', 'CSV Files (*.csv);;Excel Files (*.xlsx)')
        if not filePath:
            return
        if filePath.endswith('.csv'):
            df = pd.read_csv(filePath)
        elif filePath.endswith('.xlsx'):
            df = pd.read_excel(filePath)
        else:
            raise ValueError("Unsupported file format")

        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(df.iloc[row, col])))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
