import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem, QComboBox


def genderComboBox():
    comboBox = QComboBox()
    comboBox.addItems(["M", "F"])
    return comboBox


def employmentComboBox():
    comboBox = QComboBox()
    comboBox.addItems(["FTE", "PTE", "Retired", "School", "Student", "Unemployed"])
    return comboBox


def bedroomComboBox(bedrooms):
    max = bedrooms.value()
    comboBox = QComboBox()
    comboBox.addItems([str(i) for i in range(1, max + 1)])

    # listen to changes in the number of bedrooms
    bedrooms.valueChanged.connect(
        lambda: comboBox.clear()
        or comboBox.addItems([str(i) for i in range(1, bedrooms.value() + 1)])
    )

    return comboBox


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("./Corpus/GUI/layout.ui", self)
        self.show()

        # accord person table to number of persons
        self.numPersons.valueChanged.connect(self.updatePeopleTable)
        self.updatePeopleTableColumns()


    def updatePeopleTable(self):
        rows = self.numPersons.value()
        self.peopleTable.setRowCount(rows)
        for i in range(rows):
            if self.peopleTable.cellWidget(i, 0) is None:
                self.peopleTable.setCellWidget(i, 0, genderComboBox())
                self.peopleTable.setCellWidget(i, 1, employmentComboBox())
                self.peopleTable.setCellWidget(i, 2, bedroomComboBox(self.numBedrooms))

    def updatePeopleTableColumns(self):
        # disable all columns
        for i in range(3):
            self.peopleTable.setColumnHidden(i, True)
        
        # if genderBool is checked, unhide first column, keep listening to changes
        self.genderBool.stateChanged.connect(
            lambda: self.peopleTable.setColumnHidden(0, not self.genderBool.isChecked())
        )
        self.employmentBool.stateChanged.connect(
            lambda: self.peopleTable.setColumnHidden(1, not self.employmentBool.isChecked())
        )
        self.bedroomBool.stateChanged.connect(
            lambda: self.peopleTable.setColumnHidden(2, not self.bedroomBool.isChecked())
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec())
