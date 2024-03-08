import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create and configure the layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create and configure the input labels and text boxes
        self.num1_label = QLabel("Number 1:")
        self.num1_input = QLineEdit()
        layout.addWidget(self.num1_label)
        layout.addWidget(self.num1_input)

        self.num2_label = QLabel("Number 2:")
        self.num2_input = QLineEdit()
        layout.addWidget(self.num2_label)
        layout.addWidget(self.num2_input)

        # Create and configure the operation dropdown
        self.operation_label = QLabel("Operation:")
        layout.addWidget(self.operation_label)
        operations = ["Add", "Subtract", "Multiply", "Divide"]
        self.operation_input = QComboBox()
        self.operation_input.addItems(operations)
        layout.addWidget(self.operation_input)

        # Create and configure the calculate button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        # Create and configure the output label
        self.result_label = QLabel("Result:")
        layout.addWidget(self.result_label)
        self.result_value = QLabel("")
        layout.addWidget(self.result_value)

        # Set the window title
        self.setWindowTitle("Calculator")

    def calculate(self):
        # Get the user input
        num1 = float(self.num1_input.text())
        num2 = float(self.num2_input.text())
        operation = self.operation_input.currentText()

        # Perform the chosen operation
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                # Handle division by zero
                self.result_value.setText("Error: Division by zero")
                return
            result = num1 / num2

        # Display the result
        self.result_value.setText(str(result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())