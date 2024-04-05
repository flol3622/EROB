from PySide6.QtWidgets import QWidget, QVBoxLayout


class AdvancedSettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        # Implementeer de elementen voor 'Advanced settings' tabblad
        self.setLayout(layout)
