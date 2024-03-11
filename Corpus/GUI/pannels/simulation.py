from PySide6.QtWidgets import QGroupBox, QVBoxLayout
from ..components import add_spinbox

def pannel_simulation(self, layout):

    group = QGroupBox('Simulation Parameters')
    group_layout = QVBoxLayout()
    add_spinbox(self, layout, 'Simulation Length (days):', 'Define the number of days for the simulation duration. Typically set to 365 for a full year.', 1, 365, 365, 'simulation_length')
    add_spinbox(self, layout, 'Year:', 'Specify the year for the simulation. This affects the starting day of the year for the simulation.', 1900, 2100, 2021, 'year')
    group.setLayout(group_layout)
    layout.addWidget(group)
