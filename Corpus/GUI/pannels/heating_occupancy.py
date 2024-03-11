from PySide6.QtWidgets import QGroupBox, QVBoxLayout
from ..components import add_input_field

def pannel_heating_occupancy(layout, app_instance):
    group = QGroupBox('Heating Profile and Occupancy')
    group_layout = QVBoxLayout()
    add_input_field(group_layout, app_instance, 'Heating Profile:', 'Heating profile indicating temperatures for active, asleep, and absent states. Enter -1 if not predefined.', 'not predefined', 'heating_profile')
    add_input_field(group_layout, app_instance, 'Members:', 'Add household members with their employment types. Leave empty if not predefined.', 'e.g. FTE, FTE, Retired, School', 'members')
    group.setLayout(group_layout)
    layout.addWidget(group)