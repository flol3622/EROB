from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
)
import GUI
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulation Settings")
        self.setGeometry(100, 100, 800, 600)

        self.tab_widget = TabWidget(self)
        self.setCentralWidget(self.tab_widget)


class TabWidget(QTabWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.basic_settings_tab = GUI.BasicSettingsTab()
        self.addTab(self.basic_settings_tab, "Basic Settings")

        self.advanced_settings_tab = GUI.AdvancedSettingsTab()
        self.addTab(self.advanced_settings_tab, "Advanced Settings")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
