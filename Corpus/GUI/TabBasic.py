from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGroupBox,
)
from PySide6.QtCore import Qt

import GUI.components.inputs as inputs


class BasicSettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        # display content at top
        layout.setAlignment(Qt.AlignTop)

        # *** Simulation Group ***
        simulation_group = QGroupBox("Simulation")
        simulation_layout = QVBoxLayout()
        simulation_group.setLayout(simulation_layout)

        inputs.input_field(
            self,
            simulation_layout,
            label_text="Simulation length (in days)",
            tooltip="The length of the simulation in days",
            placeholder="number",
            attribute_name="sim_length",
        )

        inputs.input_field(
            self,
            simulation_layout,
            label_text="Year",
            tooltip="The year of the simulation",
            placeholder="YYYY",
        )

        # *** Building Group ***
        building_group = QGroupBox("Building")
        building_layout = QVBoxLayout()
        building_group.setLayout(building_layout)

        inputs.input_field(
            self,
            building_layout,
            label_text="Number of buildings",
            tooltip="The number of buildings in the simulation",
            placeholder="number",
        )

        inputs.input_field_with_checkbox(
            self,
            building_layout,
            label_text="Building name",
            tooltip="The name of the building",
            placeholder="name",
            attribute_name="building_name",
        )

        layout.addWidget(simulation_group)
        layout.addWidget(building_group)

        self.setLayout(layout)
