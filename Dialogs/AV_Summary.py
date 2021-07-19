# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AV_Summary.ui'
#
# Created: Wed Aug  7 14:51:40 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PySide6.QtWidgets import *

class Ui_AV_Summary(object):
    def setupUi(self, AV_Summary):
        AV_Summary.setObjectName("AV_Summary")
        AV_Summary.resize(194, 107)
        self.gridLayout = QGridLayout(AV_Summary)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QLabel(AV_Summary)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.Startdateedit = QDateEdit(AV_Summary)
        # self.Startdateedit.setDate(QtCore.QDate(2013, 1, 1))
        self.Startdateedit.setCalendarPopup(True)
        self.Startdateedit.setObjectName("Startdateedit")
        self.gridLayout.addWidget(self.Startdateedit, 1, 1, 1, 1)
        self.label_2 = QLabel(AV_Summary)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.Enddateedit = QDateEdit(AV_Summary)
        # self.Enddateedit.setDate(QtCore.QDate(2013, 1, 1))
        self.Enddateedit.setCalendarPopup(True)
        self.Enddateedit.setObjectName("Enddateedit")
        self.gridLayout.addWidget(self.Enddateedit, 2, 1, 1, 1)
        self.avsumprep = QPushButton(AV_Summary)
        self.avsumprep.setObjectName("avsumprep")
        self.gridLayout.addWidget(self.avsumprep, 3, 1, 1, 1)

        self.retranslateUi(AV_Summary)
        # QtCore.QMetaObject.connectSlotsByName(AV_Summary)

    def retranslateUi(self, AV_Summary):
        AV_Summary.setWindowTitle(QApplication.translate("AV_Summary", "AV Summary Export", None))
        self.label.setText(QApplication.translate("AV_Summary", "Start Date", None))
        self.Startdateedit.setDisplayFormat(QApplication.translate("AV_Summary", "MM/dd/yy", None))
        self.label_2.setText(QApplication.translate("AV_Summary", "End Date", None))
        self.Enddateedit.setDisplayFormat(QApplication.translate("AV_Summary", "MM/dd/yy", None))
        self.avsumprep.setText(QApplication.translate("AV_Summary", "Export", None))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_AV_Summary()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())