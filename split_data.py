import pandas as pd
from PyQt6 import QtWidgets, QtGui
from split_data_ui import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.Open_file.clicked.connect(self.load_file)
        self.Split_data.clicked.connect(self.split_data)

    def load_image_widget_to_tab2(self):
        pixmap = QtGui.QPixmap('images/plot.png')
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)

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

    def split_data(self):
        # Get the selected percentage from the spin box
        global split_data
        percentage = self.spinBox.value() / 100

        # Get the selected split type (radio button)
        split_type = ""
        for radio_button in (self.Real_data, self.X_test, self.X_train, self.Y_test, self.Y_train):
            if radio_button.isChecked():
                split_type = radio_button.text()
                break

        if split_type == "Real data":
            # Handle the case of displaying the whole data
            print("Displaying the whole data")
            return

        # Split the data based on the selected percentage and split type
        if split_type in ["X_test", "X_train"]:
            # Get the index to split the data
            split_index = int(len(df) * percentage)
            # Get X_test or X_train data
            if split_type == "X_test":
                split_data = df[:split_index]
            else:
                split_data = df[split_index:]

        elif split_type in ["Y_test", "Y_train"]:
            # Get the index to split the data
            split_index = int(len(df) * percentage)
            # Get Y_test or Y_train data
            if split_type == "Y_test":
                split_data = df[:split_index]
            else:
                split_data = df[split_index:]

        # Update the tableWidget with the split data
        self.tableWidget.setRowCount(split_data.shape[0])
        self.tableWidget.setColumnCount(split_data.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(split_data.columns)

        for row in range(split_data.shape[0]):
            for col in range(split_data.shape[1]):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(split_data.iloc[row, col])))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
