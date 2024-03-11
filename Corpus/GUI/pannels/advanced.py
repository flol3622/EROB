from PySide6.QtWidgets import QGroupBox, QVBoxLayout
from ..components import add_input_field

def pannel_advanced(self, layout):
    group = QGroupBox('Advanced Settings')
    group_layout = QVBoxLayout()
    add_input_field(self, layout, 'Occupancy Profiles:', 'Define CLUSTERS (occupancy profiles) for each weekday. Leave empty if not predefined.', 'e.g. mon:4, tue:4, wed:4', 'occupancy_profiles')
    add_input_field(self, layout, 'Activity Profiles:', 'Indicate if the occupancy and activity profiles are predefined on files. Enter 0 for no, 1 for yes.', '0', 'activity_profiles')
    add_input_field(self, layout, 'Appliances:', 'Define appliances used. Leave empty if not predefined.', 'e.g., Fridge, TV, Heater', 'appliances')
    add_input_field(self, layout, 'Window Use Habits:', 'Define window use habits for different seasons and rooms. Leave empty if not predefined.', 'e.g., living room winter: 1', 'window_use_habits')
    group.setLayout(group_layout)
    layout.addWidget(group)

  