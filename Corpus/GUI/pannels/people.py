from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QTableWidget, QComboBox, QLineEdit, QTableWidgetItem


def pannel_people(self, layout):
    group = QGroupBox('People')
    self.dynamic_table = DynamicTable() 
    group_layout = self.dynamic_table.layout
    group.setLayout(group_layout)
    layout.addWidget(group)


class DynamicTable:
    def __init__(self):
        self.layout = QVBoxLayout()

        # Input field for the counter
        self.counter_input = QLineEdit()
        self.counter_input.setPlaceholderText('Enter a number...')

        # Table to display rows based on counter value
        self.table = QTableWidget()
        # Now two columns: one for the row label, one for the selection
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Row', 'Choice'])

        self.layout.addWidget(self.counter_input)
        self.layout.addWidget(self.table)

        self.counter_input.textChanged.connect(self.updateCounter)

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
