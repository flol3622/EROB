from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
import GUI


class GUIApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # Setup groups for different settings
        GUI.pannel_simulation(self, main_layout)
        GUI.pannel_building(self, main_layout)
        GUI.pannel_people(self, main_layout)
        GUI.pannel_heating_occupancy(self, main_layout)
        GUI.pannel_advanced(self, main_layout)
        GUI.pannel_output(self, main_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('Simulation Configuration')
        self.setGeometry(300, 300, 600, 700)

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
    app = QApplication([])
    ex = GUIApp()
    ex.show()
    app.exec()
