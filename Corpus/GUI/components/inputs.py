from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QSpinBox,
    QComboBox,
    QPushButton,
    QMessageBox,
    QHBoxLayout,
    QCheckBox,
)


def input_field(self, layout, label_text, tooltip, placeholder, attribute_name=None):
    row_layout = QHBoxLayout()
    label = QLabel(label_text)
    input_field = QLineEdit()

    if attribute_name is not None:
        setattr(self, attribute_name, input_field)

    input_field.setPlaceholderText(placeholder)
    input_field.setMaximumWidth(300)  # Adjust the width as needed
    info_button = QPushButton("?")
    info_button.setFixedWidth(20)
    info_button.clicked.connect(
        lambda: QMessageBox.information(layout.parentWidget(), "Information", tooltip)
    )
    row_layout.addWidget(label)
    row_layout.addWidget(input_field)
    row_layout.addWidget(info_button)
    layout.addLayout(row_layout)


def input_field_with_checkbox(self, layout, label_text, tooltip, placeholder, attribute_name=None):
    row_layout = QHBoxLayout()
    checkbox = QCheckBox()
    label = QLabel(label_text)
    input_field = QLineEdit()
    
    # Define a method to update the state based on the checkbox
    def update_input_field_state():
        if checkbox.isChecked():
            input_field.setEnabled(True)
            if attribute_name is not None:
                setattr(self, attribute_name, input_field)
        else:
            input_field.setEnabled(False)
            input_field.setText("")  # Clear the text when disabled
            if attribute_name is not None:
                setattr(self, attribute_name, None)

    # Connect the checkbox state change to the update method
    checkbox.stateChanged.connect(lambda _: update_input_field_state())
    
    # Initially call the update method to set the initial state
    update_input_field_state()
    
    input_field.setPlaceholderText(placeholder)
    input_field.setMaximumWidth(300)
    
    info_button = QPushButton('?')
    info_button.setFixedWidth(20)
    info_button.clicked.connect(lambda: QMessageBox.information(layout.parentWidget(), 'Information', tooltip))


    row_layout.addWidget(label)
    # expand the space to move the checkbox to the left
    row_layout.addStretch()
    row_layout.addWidget(checkbox)
    row_layout.addWidget(input_field)
    row_layout.addWidget(info_button)
    layout.addLayout(row_layout)


def spinbox(
    self,
    layout,
    label_text,
    tooltip,
    min_val,
    max_val,
    default_val,
    attribute_name=None,
):
    row_layout = QHBoxLayout()
    label = QLabel(label_text)
    spinbox = QSpinBox()
    spinbox.setMinimum(min_val)
    spinbox.setMaximum(max_val)
    spinbox.setValue(default_val)
    spinbox.setMaximumWidth(300)
    if attribute_name is not None:
        setattr(self, attribute_name, spinbox)
    info_button = QPushButton("?")
    info_button.setFixedWidth(20)
    info_button.clicked.connect(
        lambda: QMessageBox.information(layout.parentWidget(), "Information", tooltip)
    )
    row_layout.addWidget(label)
    row_layout.addWidget(spinbox)
    row_layout.addWidget(info_button)
    layout.addLayout(row_layout)


def combobox(
    self, layout, label_text, tooltip, options, default_val, attribute_name=None
):
    row_layout = QHBoxLayout()
    label = QLabel(label_text)
    combobox = QComboBox()
    combobox.addItems(options)
    combobox.setCurrentText(default_val)
    combobox.setMaximumWidth(300)
    if attribute_name is not None:
        setattr(self, attribute_name, combobox)
    info_button = QPushButton("?")
    info_button.setFixedWidth(20)
    info_button.clicked.connect(
        lambda: QMessageBox.information(layout.parentWidget(), "Information", tooltip)
    )
    row_layout.addWidget(label)
    row_layout.addWidget(combobox)
    row_layout.addWidget(info_button)
    layout.addLayout(row_layout)
