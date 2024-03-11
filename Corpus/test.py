import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem, QComboBox
from PySide6.QtCore import Slot

class CounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Input field for the counter
        self.counter_input = QLineEdit()
        self.counter_input.setPlaceholderText('Enter a number...')
        self.counter_input.textChanged.connect(self.updateCounter)
        self.layout.addWidget(self.counter_input)

        # Table to display rows based on counter value
        self.table = QTableWidget()
        self.table.setColumnCount(2) # Now two columns: one for the row label, one for the selection
        self.table.setHorizontalHeaderLabels(['Row', 'Choice'])
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

    @Slot()
    def updateCounter(self):
        counter_value = self.counter_input.text()
        if counter_value.isdigit():
            self.updateTable(int(counter_value))
        else:
            self.updateTable(0)

    def updateTable(self, num_rows):
        self.table.setRowCount(num_rows)
        for i in range(num_rows):
            self.table.setItem(i, 0, QTableWidgetItem(f"Row {i + 1}"))
            self.addComboBox(i)

    def addComboBox(self, row):
        comboBox = QComboBox()
        options = ['A', 'B', 'C']
        comboBox.addItems(options)
        self.table.setCellWidget(row, 1, comboBox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CounterApp()
    ex.show()
    sys.exit(app.exec_())
