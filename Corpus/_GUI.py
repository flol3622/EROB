import os
import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QTimer, QUrl
from PyQt6.QtWidgets import QComboBox, QTableWidgetItem, QSpinBox

base_dir = os.path.dirname(os.path.abspath(__file__))


def genderComboBox():
    comboBox = QComboBox()
    comboBox.addItems(["M", "F"])
    return comboBox


def employmentComboBox():
    comboBox = QComboBox()
    comboBox.addItems(["FTE", "PTE", "Retired", "School", "Student", "Unemployed"])
    return comboBox


def occupancyComboBox():
    comboBox = QComboBox()
    comboBox.addItems(
        [
            "Nightshift",
            "Early shift",
            "Short absence",
            "Dayshift",
            "Half day absence",
            "Long absence",
            "Always present",
        ]
    )
    return comboBox


def bedroomComboBox(bedrooms):
    spinBox = QSpinBox()
    spinBox.setMaximum(bedrooms.value())
    spinBox.setMinimum(1)

    def updateSpinBoxMax(bedrooms, spinBox):
        try:
            spinBox.setMaximum(bedrooms.value())
        except Exception:
            pass

    bedrooms.valueChanged.connect(lambda: updateSpinBoxMax(bedrooms, spinBox))
    return spinBox


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(os.path.join(base_dir, "GUI/layout.ui"), self)
        self.show()

        # accord person table to number of persons
        self.numPersons.valueChanged.connect(self.updatePeopleTable)

        # disable all columns
        for i in range(1, 4):
            self.peopleTable.setColumnHidden(i, True)

        # if the checkbox is checked, show the column
        self.genderBool.stateChanged.connect(
            lambda: self.peopleTable.setColumnHidden(1, not self.genderBool.isChecked())
        )
        self.employmentBool.stateChanged.connect(
            lambda: self.peopleTable.setColumnHidden(
                2, not self.employmentBool.isChecked()
            )
        )
        self.bedroomBool.stateChanged.connect(
            lambda: self.peopleTable.setColumnHidden(
                3, not self.bedroomBool.isChecked()
            )
        )

        # connect the button to highlight the numPersons spinbox
        self.goToNumPersons.clicked.connect(self.highlightNumPersons)

        # help documentation
        self.actionHelp.triggered.connect(self.helpDock.show)
        self.helpText.setOpenExternalLinks(True)
        self.helpText.setSource(
            QUrl.fromLocalFile(os.path.join(base_dir, "GUI/help.html"))
        )

    def updatePeopleTable(self):
        rows = self.numPersons.value()
        self.peopleTable.setRowCount(rows)
        for i in range(rows):
            # add label i inside the first column, unchangable (label)
            self.peopleTable.setItem(i, 0, QTableWidgetItem(f"Person {i + 1}"))
            if self.peopleTable.cellWidget(i, 0) is None:
                self.peopleTable.setCellWidget(i, 1, genderComboBox())
                self.peopleTable.setCellWidget(i, 2, employmentComboBox())
                self.peopleTable.setCellWidget(i, 3, bedroomComboBox(self.numBedrooms))

        self.peopleTable2.setRowCount(rows)
        for i in range(rows):
            if self.peopleTable2.cellWidget(i, 0) is None:
                for j in range(7):
                    self.peopleTable2.setCellWidget(i, j, occupancyComboBox())

    def highlightNumPersons(self):
        self.tabWidget.setCurrentIndex(0)
        self.label_14.setStyleSheet("border: 2px solid blue;")
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.label_14.setStyleSheet("border: none;"))
        self.timer.start(500)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec())
