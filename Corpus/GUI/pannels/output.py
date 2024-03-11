from PySide6.QtWidgets import QHBoxLayout, QPushButton
from ..components import add_input_field


def pannel_output(self, layout):
    output_section_layout = QHBoxLayout()
    add_input_field(self, output_section_layout, 'Result File Name:',
                    'Enter a name for the result file. This name will be used to save the simulation results.', '', 'result_file_name')
    generate_button = QPushButton('Generate')
    # Assuming you have a generate function
    generate_button.clicked.connect(self.generate)
    output_section_layout.addWidget(generate_button)
    layout.addLayout(output_section_layout)
