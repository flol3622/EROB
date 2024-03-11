from PySide6.QtWidgets import QGroupBox, QVBoxLayout
from ..components import add_input_field

def pannel_heating_occupancy(self, layout):
    group = QGroupBox('Heating Profile and Occupancy')
    group_layout = QVBoxLayout()
    add_input_field(self, group_layout, 'Heating Profile:', 'Heating profile indicating temperatures for active, asleep, and absent states. Enter -1 if not predefined.', 'not predefined', 'heating_profile')
    add_input_field(self, group_layout, 'Members:', 'Add household members with their employment types. Leave empty if not predefined.', 'e.g. FTE, FTE, Retired, School', 'members')
    group.setLayout(group_layout)
    layout.addWidget(group)