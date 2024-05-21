import os
import sys

# from pprint import pprint
from rich.pretty import pprint

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QTimer, QUrl
from PyQt6.QtWidgets import QComboBox, QTableWidgetItem, QSpinBox, QCheckBox, QWidget

base_dir = os.path.dirname(os.path.abspath(__file__))


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


def bedroomSpinBox(bedrooms):
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
        self.employmentBool.stateChanged.connect(
            lambda: self.peopleTable.setColumnHidden(
                1, not self.employmentBool.isChecked()
            )
        )
        self.bedroomBool.stateChanged.connect(
            lambda: self.peopleTable.setColumnHidden(
                2, not self.bedroomBool.isChecked()
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

        # file selection buttons
        self.occProfileFileName = None
        self.actProfileFileName = None
        self.occupFile.clicked.connect(
            lambda: self.selectFile(
                self.occProfileFileDisp, "txt", "Select occupancy profile"
            )
        )
        self.actOnFile.clicked.connect(
            lambda: self.selectFile(
                self.activProfileFileDisp, "txt", "Select activity profile"
            )
        )

        # define output file
        self.outFileName = self.outFileLabel.text()
        self.fileOutNameButton.clicked.connect(self.defineOutputFile)

        # generate output
        self.generateButton.clicked.connect(self.getParams)

    def updatePeopleTable(self):
        rows = self.numPersons.value()
        self.peopleTable.setRowCount(rows)
        for i in range(rows):
            # add label i inside the first column, unchangable (label)
            self.peopleTable.setItem(i, 0, QTableWidgetItem(f"Person {i + 1}"))
            if self.peopleTable.cellWidget(i, 1) is None:
                self.peopleTable.setCellWidget(i, 1, employmentComboBox())
                self.peopleTable.setCellWidget(i, 2, bedroomSpinBox(self.numBedrooms))

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

    def selectFile(self, lineEdit, ext, title="Open file"):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, title, "", f"{ext} files (*.{ext});;All files (*)"
        )
        if file:
            lineEdit.setText(os.path.basename(file))
            if "occup" in title.lower():
                self.occProfileFileName = file
            elif "act" in title.lower():
                self.actProfileFileName = file

    def defineOutputFile(self):
        file, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save file", "", "Parameters files (*.p);;All files (*)"
        )
        if file:
            self.outFileLabel.setText(os.path.relpath(file))
            self.outFileName = file

    def getParams(self):
        params = {}
        params["name"] = self.outFileName
        params["nday"] = self.simLength.value()
        params["year"] = self.simYear.value()
        params["nBui"] = self.numBuildings.value()
        params["npers"] = self.numPersons.value()
        params["members"] = [
            self.peopleTable.cellWidget(i, 2).currentText()
            for i in range(params["npers"])
            if self.employmentBool.isChecked()
        ]
        params["clusters"] = [
            {
                "mon": self.peopleTable2.cellWidget(i, 0).currentIndex() + 1,
                "tue": self.peopleTable2.cellWidget(i, 1).currentIndex() + 1,
                "wed": self.peopleTable2.cellWidget(i, 2).currentIndex() + 1,
                "thu": self.peopleTable2.cellWidget(i, 3).currentIndex() + 1,
                "fri": self.peopleTable2.cellWidget(i, 4).currentIndex() + 1,
                "sat": self.peopleTable2.cellWidget(i, 5).currentIndex() + 1,
                "sun": self.peopleTable2.cellWidget(i, 6).currentIndex() + 1,
            }
            for i in range(params["npers"])
            if self.occupCustom.isChecked()
        ]
        params["nbedr"] = (
            self.numBedrooms.value() if self.bedroomBoolMain.isChecked() else 0
        )
        params["BEDR"] = [
            self.peopleTable.cellWidget(i, 3).value()
            for i in range(params["npers"])
            if self.bedroomBool.isChecked()
        ]
        apps = []
        for widget in self.appGroup.findChildren(QWidget):
            if appliance_name := widget.property("applianceName"):
                if isinstance(widget, QCheckBox) and widget.isChecked():
                    apps.append(appliance_name)
                elif isinstance(widget, QSpinBox) and widget.value() > 0:
                    apps.extend([appliance_name] * widget.value())
        params["apps"] = apps if self.appBool.isChecked() else []
        params["VentS"] = (
            self.ventSystem.currentIndex() if self.ventBool.isChecked() else -1
        )
        params["DW"] = self.dwType.currentIndex() if self.dwBool.isChecked() else -1
        params["YearBuilt"] = (
            self.constrYear.value() if self.constrYearBool.isChecked() else -1
        )
        params["OccONFILE"] = int(self.occupFile.isChecked())
        params["OccFileName"] = self.occProfileFileName
        params["ActONFILE"] = int(self.actOnFile.isChecked())
        params["ActFileName"] = self.actProfileFileName
        params["shtype"] = (
            self.heatSetpoint.currentIndex() + 1
            if self.heatSetpointBool.isChecked()
            else -1
        )
        shrooms = ["dayzone", "bathroom", "nightzone"]
        params["shrooms"] = (
            [
                shrooms[i]
                for i, zone in enumerate(self.shroomsWidget.findChildren(QCheckBox))
                if zone.isChecked()
            ]
            if self.shroomsBool.isChecked()
            else []
        )
        params["habits"] = (
            [i.currentIndex() for i in self.formHabits.findChildren(QComboBox)]
            if self.habitsDetailBool.isChecked() and self.habitsBool.isChecked()
            else []
        )
        habitsGen = self.habitsBool.isChecked() and self.habitsGeneralBool.isChecked()
        params["HHhabit"] = self.hhhabits.currentIndex() + 1 if habitsGen else -1
        params["SeCo"] = self.seasonality.currentIndex() + 1 if habitsGen else -1

        pprint(params)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("EROB gui")
    sys.exit(app.exec())
