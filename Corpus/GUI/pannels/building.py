from PySide6.QtWidgets import QGroupBox, QVBoxLayout
from ..components import add_input_field, add_combobox, add_spinbox

def pannel_building(layout, app_instance):
    group = QGroupBox('Building and Household Configuration')
    group_layout = QVBoxLayout()
    add_spinbox(group_layout, app_instance, 'Number of Buildings:', 'Define the number of buildings to simulate. Enter a positive integer value.', 1, 100, 1, 'number_of_buildings')
    add_spinbox(group_layout, app_instance, 'Number of Persons:', 'Define the number of persons in the household. If not predefined, enter 0.', 0, 20, 0, 'number_of_persons')
    add_spinbox(group_layout, app_instance, 'Number of Bedrooms:', 'Define the number of bedrooms. Maximum allowed is 8. If not predefined, enter 0.', 0, 8, 0, 'number_of_bedrooms')
    add_combobox(group_layout, app_instance, 'Ventilation System:', 'Type of ventilation system: 0 for no system, 1 for exhaust, 2 for balanced. Leave as "not predefined" if unknown.', ['0: no system', '1: exhaust', '2: balanced'], '0: no system', 'ventilation_system')
    add_combobox(group_layout, app_instance, 'Dwelling Type:', 'Type of dwelling: 1 for apartment, 2 for house. Leave as "not predefined" if unknown.', ['1: apartment', '2: house'], '1: apartment', 'dwelling_type')
    add_input_field(group_layout, app_instance, 'Year Built:', 'Enter the year the building was constructed or last renovated.', 'unknown', 'year_built')
    group.setLayout(group_layout)
    layout.addWidget(group)