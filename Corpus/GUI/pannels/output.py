from PySide6.QtWidgets import QHBoxLayout, QPushButton
from ..components import add_input_field

def pannel_output(layout,app_instance):
    output_section_layout = QHBoxLayout()
    add_input_field(output_section_layout, app_instance, 'Result File Name:', 'Enter a name for the result file. This name will be used to save the simulation results.', '', 'result_file_name')
    generate_button = QPushButton('Generate')
    generate_button.clicked.connect(app_instance.generate)  # Assuming you have a generate function
    output_section_layout.addWidget(generate_button)
    layout.addLayout(output_section_layout)