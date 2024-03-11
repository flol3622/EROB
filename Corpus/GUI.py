import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QSpinBox, QMessageBox, QGroupBox, QComboBox)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class GUIApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Simulation Parameters
        simulation_parameters_group = QGroupBox('Simulation Parameters')
        simulation_parameters_layout = QVBoxLayout()
        self.add_spinbox_with_info(simulation_parameters_layout, 'Simulation Length (days):', 'Define the number of days for the simulation duration. Typically set to 365 for a full year.', 1, 365, 365, 'simulation_length')
        self.add_spinbox_with_info(simulation_parameters_layout, 'Year:', 'Specify the year for the simulation. This affects the starting day of the year for the simulation.', 1900, 2100, 2021, 'year')
        simulation_parameters_group.setLayout(simulation_parameters_layout)
        layout.addWidget(simulation_parameters_group)

        # Building and Household Configuration
        building_configuration_group = QGroupBox('Building and Household Configuration')
        building_configuration_layout = QVBoxLayout()
        self.add_spinbox_with_info(building_configuration_layout, 'Number of Buildings:', 'Define the number of buildings to simulate. Enter a positive integer value.', 1, 100, 1, 'number_of_buildings')
        self.add_spinbox_with_info(building_configuration_layout, 'Number of Persons:', 'Define the number of persons in the household. If not predefined, enter 0.', 0, 20, 0, 'number_of_persons')
        self.add_spinbox_with_info(building_configuration_layout, 'Number of Bedrooms:', 'Define the number of bedrooms. Maximum allowed is 8. If not predefined, enter 0.', 0, 8, 0, 'number_of_bedrooms')
        self.add_combobox_with_info(building_configuration_layout, 'Ventilation System:', 'Type of ventilation system: 0 for no system, 1 for exhaust, 2 for balanced. Leave as "not predefined" if unknown.', ['0: no system', '1: exhaust', '2: balanced'], 'no system', 'ventilation_system')
        self.add_combobox_with_info(building_configuration_layout, 'Dwelling Type:', 'Type of dwelling: 1 for apartment, 2 for house. Leave as "not predefined" if unknown.', ['1: apartment', '2: house'], 'not predefined', 'dwelling_type')
        self.add_input_field_with_info(building_configuration_layout, 'Year Built:', 'Enter the year the building was constructed or last renovated. ', 'unknown', 'year_built')
        building_configuration_group.setLayout(building_configuration_layout)
        layout.addWidget(building_configuration_group)

        # Heating Profile and Occupancy
        heating_profile_group = QGroupBox('Heating Profile and Occupancy')
        heating_profile_layout = QVBoxLayout()
        self.add_input_field_with_info(heating_profile_layout, 'Heating Profile:', 'Heating profile indicating temperatures for active, asleep, and absent states. Enter -1 if not predefined.', 'not predefined', 'heating_profile')
        self.add_input_field_with_info(heating_profile_layout, 'Members:', 'Add household members with their employment types. Leave empty if not predefined.', 'e.g. FTE, FTE, Retired, School', 'members')
        heating_profile_group.setLayout(heating_profile_layout)
        layout.addWidget(heating_profile_group)

        # Advanced Settings for Simulation
        advanced_group = QGroupBox('Advanced Settings')
        advanced_layout = QVBoxLayout()
        advanced_group.setLayout(advanced_layout)

        # Occupancy and Activity Profiles
        self.add_input_field_with_info(advanced_layout, 'Occupancy Profiles:', 'Define CLUSTERS (occupancy profiles) for each weekday. Leave empty if not predefined.', 'e.g. mon:4, tue:4, wed:4', 'occupancy_profiles')
        self.add_input_field_with_info(advanced_layout, 'Activity Profiles:', 'Indicate if the occupancy and activity profiles are predefined on files. Enter 0 for no, 1 for yes.', '0', 'activity_profiles')

        # Appliance Configuration
        self.add_input_field_with_info(advanced_layout, 'Appliances:', 'Define appliances used. Leave empty if not predefined.', 'e.g., Fridge, TV, Heater', 'appliances')

        # Window Use Habits
        self.add_input_field_with_info(advanced_layout, 'Window Use Habits:', 'Define window use habits for different seasons and rooms. Leave empty if not predefined.', 'e.g., living room winter: 1', 'window_use_habits')

        layout.addWidget(advanced_group)

        # add horizontal separator
        line = QLabel()
        line.setFrameStyle(QLabel.HLine | QLabel.Sunken)
        layout.addWidget(line)

        # Save Output
        save_output_group = QHBoxLayout()
        self.add_input_field_with_info(save_output_group, 'Result File Name:', 'Enter a name for the result file. This name will be used to save the simulation results.', '', 'result_file_name')
        
        generate_button = QPushButton('Generate')
        generate_button.clicked.connect(self.generate)
        save_output_group.addWidget(generate_button)
        layout.addLayout(save_output_group)

        self.setLayout(layout)
        self.setWindowTitle('Simulation Configuration')
        self.setGeometry(300, 300, 600, 700)

    def add_input_field_with_info(self, layout, label_text, tooltip, placeholder, attribute_name=None, input_mask=None):
        row_layout = QHBoxLayout()
        label = QLabel(label_text)
        input_field = QLineEdit()
        if attribute_name:
            setattr(self, attribute_name, input_field)
        if input_mask:
            input_field.setInputMask(input_mask)
        input_field.setPlaceholderText(placeholder)
        # Set a maximum width for QLineEdit to control its size
        input_field.setMaximumWidth(300)  # Adjust the width as needed
        info_button = QPushButton('?')
        info_button.setFixedWidth(20)
        info_button.clicked.connect(lambda: self.show_message(tooltip))
        row_layout.addWidget(label)
        row_layout.addWidget(input_field)
        row_layout.addWidget(info_button)
        layout.addLayout(row_layout)
        setattr(self, label_text.replace(' ', '_').lower(), input_field)

    def add_spinbox_with_info(self, layout, label_text, tooltip, min_val, max_val, default_val, attribute_name=None):
        row_layout = QHBoxLayout()
        label = QLabel(label_text)
        spinbox = QSpinBox()
        if attribute_name:
            setattr(self, attribute_name, spinbox)
        spinbox.setMinimum(min_val)
        spinbox.setMaximum(max_val)
        spinbox.setValue(default_val)
        spinbox.setMaximumWidth(300)
        info_button = QPushButton('?')
        info_button.setFixedWidth(20)
        info_button.clicked.connect(lambda: self.show_message(tooltip))
        row_layout.addWidget(label)
        row_layout.addWidget(spinbox)
        row_layout.addWidget(info_button)
        layout.addLayout(row_layout)
        setattr(self, label_text.replace(' ', '_').lower(), spinbox)
    
    def add_combobox_with_info(self, layout, label_text, tooltip, options, default_val, attribute_name=None):
        row_layout = QHBoxLayout()
        label = QLabel(label_text)
        combobox = QComboBox()
        if attribute_name:
            setattr(self, attribute_name, combobox)
        for option in options:
            combobox.addItem(option)
        combobox.setCurrentText(default_val)
        combobox.setMaximumWidth(300)
        info_button = QPushButton('?')
        info_button.setFixedWidth(20)
        info_button.clicked.connect(lambda: self.show_message(tooltip))
        row_layout.addWidget(label)
        row_layout.addWidget(combobox)
        row_layout.addWidget(info_button)
        layout.addLayout(row_layout)
        setattr(self, label_text.replace(' ', '_').lower(), combobox)

    def show_message(self, message):
        QMessageBox.information(self, 'Information', message)

    def generate(self):
        # folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        # if folder_path:
        # Initialize a dictionary to store all parameters
        parameters = {}

        # Retrieve values from spin boxes
        parameters['simulation_length'] = self.simulation_length.value()
        parameters['year'] = self.year.value()
        parameters['number_of_buildings'] = self.number_of_buildings.value()
        parameters['number_of_persons'] = self.number_of_persons.value()
        parameters['number_of_bedrooms'] = self.number_of_bedrooms.value()

        # Retrieve values from input fields
        parameters['ventilation_system'] = self.ventilation_system.currentText()
        parameters['dwelling_type'] = self.dwelling_type.currentText()
        parameters['year_built'] = self.year_built.text()
        parameters['heating_profile'] = self.heating_profile.text()
        parameters['members'] = self.members.text()
        parameters['occupancy_profiles'] = self.occupancy_profiles.text()
        parameters['activity_profiles'] = self.activity_profiles.text()
        parameters['appliances'] = self.appliances.text()
        parameters['window_use_habits'] = self.window_use_habits.text()
        parameters['result_file_name'] = self.result_file_name.text()

        # print(f"Saving output to: {folder_path}")
        print("Parameters:", parameters)
        # Here, you can further process the collected parameters as needed.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUIApp()
    ex.show()
    sys.exit(app.exec())
