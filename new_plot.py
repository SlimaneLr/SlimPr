import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from qtpy import QtWidgets
import matplotlib.pyplot as plt
from plot_file_ui import Ui_mainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Plot Viewer")  # Set your window title here
        self.setFixedSize(800, 600)
        # Connect buttons to their respective functions
        self.ui.pushButton.clicked.connect(self.openFile)
        self.ui.pushButton_2.clicked.connect(self.designPlot)



    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        if fileName:
            df = pd.read_csv(fileName)
            self.ui.tableWidget.setRowCount(df.shape[0])
            self.ui.tableWidget.setColumnCount(df.shape[1])
            self.ui.tableWidget.setHorizontalHeaderLabels(df.columns)
            for row in range(df.shape[0]):
                for col in range(df.shape[1]):
                    self.ui.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(df.iloc[row, col])))

            # Populate comboboxes with column names
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(df.columns)
            self.ui.comboBox_2.clear()
            self.ui.comboBox_2.addItems(df.columns)

    def designPlot(self):
        x_label = self.ui.comboBox.currentText()
        y_label = self.ui.comboBox_2.currentText()

        if x_label and y_label:
            # Extract data from tableWidget
            table = self.ui.tableWidget
            headers = [table.horizontalHeaderItem(col).text() for col in range(table.columnCount())]
            x_index = headers.index(x_label)
            y_index = headers.index(y_label)

            x_data = []
            y_data = []
            for row in range(table.rowCount()):
                x_value = table.item(row, x_index).text()
                y_value = table.item(row, y_index).text()

                # Check if the data in the selected columns are numerical
                if self.isNumeric(x_value) and self.isNumeric(y_value):
                    x_data.append(float(x_value))
                    y_data.append(float(y_value))
                else:
                    # Convert string values to categories
                    x_data.append(x_value)
                    y_data.append(y_value)

            # Plot the data
            plt.figure()
            if all(isinstance(val, str) for val in x_data) and all(isinstance(val, str) for val in y_data):
                plt.scatter(x_data, y_data)  # Scatter plot for string data
            else:
                plt.plot(x_data, y_data, 'o')  # Scatter plot for numerical data
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(f"Plot of {y_label} against {x_label}")
            plt.show()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select X and Y labels.")

    def isNumeric(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
