import sys
import pandas as pd
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QTabWidget,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Analyzer")

        # Create tabs
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        # Create table widget
        self.table = QTableWidget()

        # Create button
        self.open_button = QPushButton("Open File")
        self.open_button.clicked.connect(self.open_file)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.open_button)
        layout.addWidget(self.tabs)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.Option.ShowDirsOnly
        path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "CSV Files (*.csv);;Excel Files (*.xls *.xlsx)", options=options
        )
        if path:
            if path.endswith(".csv"):
                self.read_csv(path)
            else:
                self.read_excel(path)

    def read_csv(self, path):
        data = pd.read_csv(path)
        self.show_data(data)

    def read_excel(self, path):
        data = pd.read_excel(path)
        self.show_data(data)

    def show_data(self, data):
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data.columns))
        self.table.setHorizontalHeaderLabels(data.columns)

        for row, (index, row_data) in enumerate(data.iterrows()):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, col, item)

        # Clear existing layout from tabs
        self.tab1.layout().clear()
        self.tab2.layout().clear()

        # Add table to tabs
        layout1 = QHBoxLayout()
        layout1.addWidget(self.table)
        self.tab1.setLayout(layout1)

        # You can add additional widgets to other tabs here (optional)

        self.tabs.setCurrentIndex(0)  # Show the first tab


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
