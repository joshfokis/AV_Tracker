# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AV_Summary.ui'
#
# Created: Wed Aug  7 14:51:40 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AV_Summary(object):
    def setupUi(self, AV_Summary):
        AV_Summary.setObjectName(_fromUtf8("AV_Summary"))
        AV_Summary.resize(194, 107)
        self.gridLayout = QtGui.QGridLayout(AV_Summary)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(AV_Summary)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.Startdateedit = QtGui.QDateEdit(AV_Summary)
        self.Startdateedit.setDate(QtCore.QDate(2013, 1, 1))
        self.Startdateedit.setCalendarPopup(True)
        self.Startdateedit.setObjectName(_fromUtf8("Startdateedit"))
        self.gridLayout.addWidget(self.Startdateedit, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(AV_Summary)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.Enddateedit = QtGui.QDateEdit(AV_Summary)
        self.Enddateedit.setDate(QtCore.QDate(2013, 1, 1))
        self.Enddateedit.setCalendarPopup(True)
        self.Enddateedit.setObjectName(_fromUtf8("Enddateedit"))
        self.gridLayout.addWidget(self.Enddateedit, 2, 1, 1, 1)
        self.avsumprep = QtGui.QPushButton(AV_Summary)
        self.avsumprep.setObjectName(_fromUtf8("avsumprep"))
        self.gridLayout.addWidget(self.avsumprep, 3, 1, 1, 1)

        self.retranslateUi(AV_Summary)
        QtCore.QMetaObject.connectSlotsByName(AV_Summary)

    def retranslateUi(self, AV_Summary):
        AV_Summary.setWindowTitle(_translate("AV_Summary", "AV Summary Export", None))
        self.label.setText(_translate("AV_Summary", "Start Date", None))
        self.Startdateedit.setDisplayFormat(_translate("AV_Summary", "MM/dd/yy", None))
        self.label_2.setText(_translate("AV_Summary", "End Date", None))
        self.Enddateedit.setDisplayFormat(_translate("AV_Summary", "MM/dd/yy", None))
        self.avsumprep.setText(_translate("AV_Summary", "Export", None))

