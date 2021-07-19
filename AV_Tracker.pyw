import sys
from Dialogs.AV_sum import *
from Dialogs.dialog import *
from Dialogs.AV_Summary import *
from PySide6.QtWidgets import *
import PySide6.QtSql as QtSql
from PySide6.QtCore import Qt
from datetime import datetime, date
import csv
import sqlite3


def createConnection():
    """Creates connection to the database."""
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('AV_sum.db')
    if db.open():
        return True
    else:
        print(db.lastError().text())
        return False


class MyForm(QMainWindow):
    """Class for the Main Window GUI."""
    def __init__(self, parent=None):
        """The Initialization of the class."""
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Sets up the Table View for the database
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("AV")
        #Sorts by column then by direction
        self.model.setSort(3, Qt.AscendingOrder)
        #Sets edit strategy to On Field change
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.ui.tableView.setModel(self.model)
        #Calls a function based on the button or menu triggered
        self.ui.Save_Button.clicked.connect(self.dbinput)
        self.ui.pushclearsearch.clicked.connect(self.clearsearch)
        self.ui.Update_Button.clicked.connect(self.updaterow)
        self.ui.pushSearch.clicked.connect(self.dbfilter)
        self.ui.pushRefresh.clicked.connect(self.dbrefresh)
        self.ui.actionBy_Date_4.triggered.connect(self.dbexport)
        self.ui.actionBy_Hostname_4.triggered.connect(self.Hostdbex)
        self.ui.actionBy_Username_4.triggered.connect(self.Userdbex)
        self.ui.actionExport_Entire_Database.triggered.connect(self.dbexall)
        self.ui.actionClear_Form.triggered.connect(self.clearform)
        self.ui.actionExport_AV_Summary.triggered.connect(self.Callprep)
        self.ui.actionDelete_Row.triggered.connect(self.deletrow)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionUpdate_Row.triggered.connect(self.mapindex)
        self.ui.lineEditSearch.returnPressed.connect(self.dbfilter)
        #Syle and look of the application
        app.setStyle("plastique")
        #Maps all the Fields to a column
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.ui.Hostname_Input, 0)
        self.mapper.addMapping(self.ui.lineEditLogs, 10)
        self.mapper.addMapping(self.ui.lineEditdategen, 2)
        self.mapper.addMapping(self.ui.lineEditdaterec, 3)
        self.mapper.addMapping(self.ui.IP_Address_Input, 4)
        self.mapper.addMapping(self.ui.lineEditDAT, 11)
        self.mapper.addMapping(self.ui.Username_input, 5)
        self.mapper.addMapping(self.ui.Location_input, 6)
        self.mapper.addMapping(self.ui.Detection_Type_Input, 9)
        self.mapper.addMapping(self.ui.Org_input, 7)
        self.mapper.addMapping(self.ui.File_Path_input, 12)
        self.mapper.addMapping(self.ui.textEditComments, 13)
        self.mapper.addMapping(self.ui.Device_Type_Drop, 1)
        self.mapper.addMapping(self.ui.Action_selection, 8)
        #Hides The input fields and button for the update view
        self.ui.Update_Button.hide()
        self.ui.lineEditdaterec.hide()
        self.ui.lineEditdategen.hide()
        self.ui.Date_gen_input.setDate(date.today())
        self.ui.Date_rec_input.setDate(date.today())

    def mapindex(self):
        """Function called to pull a row from
            the table back to the line edits
            and drop selections"""
        devices = ['Desktop', 'Laptop', 'Server']
        actions = ['On Access Deleted', 'On Access Cleaned',
                   'Managed Scan Deleted',
                   'Managed Scan Cleaned', 'Script Scan Blocked', 'Other']
        # Promts the user to input the row to update
        i, ok = QInputDialog.getInteger(
            self, "Update Row", "Row:", 1, 1, 1000, 1)
        row = "%d" % i
        row = int(row) - 1
        if ok:
            self.ui.Save_Button.hide()
            self.ui.Update_Button.show()
            self.ui.lineEditdaterec.show()
            self.ui.lineEditdategen.show()
            for device in devices:
                device = self.model.record(row).value("device_type")
                self.ui.Device_Type_Drop.setCurrentIndex(devices.index(device))
            for action in actions:
                action = self.model.record(row).value("action")
                self.ui.Action_selection.setCurrentIndex(actions.index(action))
            self.mapper.setCurrentIndex(row)

    def updaterow(self, row):
        """Function to update the row in the
        database from the updated line edits"""
        row = self.mapper.currentIndex()
        hosttext = str(self.ui.Hostname_Input.text())
        daterec = str(self.ui.lineEditdaterec.text())
        dategen = str(self.ui.lineEditdategen.text())
        device = str(self.ui.Device_Type_Drop.currentText())
        logs = str(self.ui.lineEditLogs.text())
        ipadd = str(self.ui.IP_Address_Input.text())
        dat = str(self.ui.lineEditDAT.text())
        username = str(self.ui.Username_input.text())
        location = str(self.ui.Location_input.text())
        detection = str(self.ui.Detection_Type_Input.text())
        action = str(self.ui.Action_selection.currentText())
        org = str(self.ui.Org_input.text())
        filepath = str(self.ui.File_Path_input.toPlainText())
        comments = str(self.ui.textEditComments.toPlainText())
        # When the update button is triggered
        # this updates the the row if dates aren't blocked
        if dategen and daterec != "":
            self.model.setData(self.model.index(row, 0), hosttext.upper())
            self.model.setData(self.model.index(row, 1), device)
            self.model.setData(self.model.index(row, 4), ipadd)
            self.model.setData(self.model.index(row, 5), username.lower())
            self.model.setData(self.model.index(row, 6), location)
            self.model.setData(self.model.index(row, 7), org)
            self.model.setData(self.model.index(row, 8), action)
            self.model.setData(self.model.index(row, 9), detection)
            self.model.setData(self.model.index(row, 10), logs.upper())
            self.model.setData(self.model.index(row, 11), dat)
            self.model.setData(self.model.index(row, 12), filepath)
            self.model.setData(self.model.index(row, 13), comments)
            self.model.setData(self.model.index(row, 2), dategen)
            self.model.setData(self.model.index(row, 3), daterec)
            self.model.submitAll()
            self.ui.Hostname_Input.clear()
            self.ui.lineEditdaterec.clear()
            self.ui.lineEditdategen.clear()
            self.ui.lineEditLogs.clear()
            self.ui.IP_Address_Input.clear()
            self.ui.lineEditDAT.clear()
            self.ui.Username_input.clear()
            self.ui.Location_input.clear()
            self.ui.Detection_Type_Input.clear()
            self.ui.Org_input.clear()
            self.ui.File_Path_input.clear()
            self.ui.textEditComments.clear()
            self.ui.Save_Button.show()
            self.ui.Update_Button.hide()
            self.ui.lineEditdaterec.hide()
            self.ui.lineEditdategen.hide()
        else:
            w, ok = QMessageBox.warning(
                self, 'Warning', "Dates cannot be left blank",)

    def clearsearch(self):
        """Clears the search from the database view"""
        self.ui.lineEditSearch.clear()
        self.model.setFilter(
            "" + self.ui.comboFilter.currentText()
               + " like '" + self.ui.lineEditSearch.text() + "%'")

    def clearform(self):
        """Function to clear the line edits of text"""
        self.ui.Hostname_Input.clear()
        self.ui.lineEditLogs.clear()
        self.ui.IP_Address_Input.clear()
        self.ui.lineEditDAT.clear()
        self.ui.Username_input.clear()
        self.ui.Location_input.clear()
        self.ui.Detection_Type_Input.clear()
        self.ui.Org_input.clear()
        self.ui.File_Path_input.clear()
        self.ui.textEditComments.clear()
        self.ui.Save_Button.show()
        self.ui.Update_Button.hide()
        self.ui.lineEditdaterec.hide()
        self.ui.lineEditdategen.hide()

    def deletrow(self):
        """Function called to delete a row from the tableview and database"""
        i, ok = QInputDialog.getInteger(
            self, "Delete Row", "Row:", 1, 1, 100, 1)
        rowid = "%d" % i
        row = "%d" % i
        row = int(row) - 1
        if ok:
            yes = QMessageBox.question(
                self, 'Message',
                """You are about to delete row %s from the database.
              Are you sure you want to continue?""" % rowid,
                QMessageBox.Yes, QMessageBox.No)
            if yes == QMessageBox.Yes:
                self.model.removeRow(row)

    def dbinput(self):
        """The Function to Input the User Data to the Database"""
        self.model.insertRow(0)
        hosttext = str(self.ui.Hostname_Input.text())
        device = str(self.ui.Device_Type_Drop.currentText())
        logs = str(self.ui.lineEditLogs.text())
        ipadd = str(self.ui.IP_Address_Input.text())
        dat = str(self.ui.lineEditDAT.text())
        dategen = self.ui.Date_gen_input.dateTime()
        dategen = str(dategen.toPyDateTime().strftime('%m/%d/%y %I:%M:%S %p'))
        username = str(self.ui.Username_input.text())
        location = str(self.ui.Location_input.text())
        daterec = self.ui.Date_rec_input.dateTime()
        daterec = str(daterec.toPyDateTime().strftime('%m/%d/%y %I:%M:%S %p'))
        action = str(self.ui.Action_selection.currentText())
        detection = str(self.ui.Detection_Type_Input.text())
        org = str(self.ui.Org_input.text())
        filepath = str(self.ui.File_Path_input.toPlainText())
        comments = str(self.ui.textEditComments.toPlainText())
        self.model.setData(self.model.index(0, 0), hosttext.upper())
        self.model.setData(self.model.index(0, 1), device)
        self.model.setData(self.model.index(0, 4), ipadd)
        self.model.setData(self.model.index(0, 5), username.lower())
        self.model.setData(self.model.index(0, 6), location)
        self.model.setData(self.model.index(0, 7), org)
        self.model.setData(self.model.index(0, 8), action)
        self.model.setData(self.model.index(0, 9), detection)
        self.model.setData(self.model.index(0, 10), logs.upper())
        self.model.setData(self.model.index(0, 11), dat)
        self.model.setData(self.model.index(0, 12), filepath)
        self.model.setData(self.model.index(0, 13), comments)
        self.model.setData(self.model.index(0, 2), dategen)
        self.model.setData(self.model.index(0, 3), daterec)
        self.model.submitAll()
        self.ui.Hostname_Input.clear()
        self.ui.lineEditLogs.clear()
        self.ui.IP_Address_Input.clear()
        self.ui.lineEditDAT.clear()
        self.ui.Date_gen_input.dateTime()
        self.ui.Username_input.clear()
        self.ui.Location_input.clear()
        self.ui.Date_rec_input.dateTime()
        self.ui.Detection_Type_Input.clear()
        self.ui.Org_input.clear()
        self.ui.File_Path_input.clear()
        self.ui.textEditComments.clear()

    def dbfilter(self):
        """The function to filter the database view based on user input """
        self.model.setFilter(
            "" + self.ui.comboFilter.currentText() +
            " like '" + self.ui.lineEditSearch.text() + "%'")

    def dbrefresh(self):
        """Function to refresh the database view."""
        self.model.select()

    def dbexport(self):
        """Function to call a Dialog box for the
        exporting functions of the database."""
        dialog = Dialog()
        dialog.exec_()

    def Callprep(self):
        """Function that calls the Morning call export"""
        callprepui = Ui_AV_Summary()
        callprepui.exec_()

    def dbexall(self):
        """Function to export the entire database to csv file format."""
        now = datetime.now()
        folder = QFileDialog.getSaveFileName(
            None, str("Save File"), str(
                "AV_OUTPUT_DATABASE_%s.csv" % now.strftime('%m%d%Y')),
            str("CSV(*.csv)"))
        conn = sqlite3.connect("AV_sum.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * from AV ORDER BY date_rec DESC;")
        csv_writer = csv.writer(open(folder, "wb"))
        csv_writer.writerow([i[0] for i in cursor.description])
        #write headers
        csv_writer.writerows(cursor)
        del csv_writer
        # this will close the CSV file

    def Hostdbex(self):
        """Function to export from the database
         based on the hostname to csv file format."""
        now = datetime.now()
        text, ok = QInputDialog.getText(
            self, "Export By Hostname", "Hostname:", QLineEdit.Normal)
        if ok and text != '':
            text = str(text)
            folder = QFileDialog.getSaveFileName(
                None, str("Save File"),
                str("AV_OUTPUT_%s_%s.csv" % (text, now.strftime('%m%d%Y'))),
                str("CSV(*.csv)"))
            conn = sqlite3.connect("AV_sum.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from AV WHERE hostname LIKE '" + text + "%'")
            csv_writer = csv.writer(open(folder, "wb"))
            csv_writer.writerow([i[0] for i in cursor.description])
            # write headers
            csv_writer.writerows(cursor)
            del csv_writer
            # this will close the CSV file

    def Userdbex(self):
        """Function to export from the database
         based on the username to csv file format."""
        text, ok = QInputDialog.getText(
            self, "Export By Username", """Wildcard = %
EXAMPLE %smith.

Username:""", QLineEdit.Normal)
        if ok and text != '':
            text = str(text)
            now = datetime.now()
            folder = QFileDialog.getSaveFileName(
                None, str("Save File"),
                str("AV_OUTPUT_%s_%s.csv" % (text, now.strftime('%m%d%Y'))),
                str("CSV(*.csv)"))
            conn = sqlite3.connect("AV_sum.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * from AV WHERE username LIKE '" + text + "%'")
            csv_writer = csv.writer(open(folder, "wb"))
            csv_writer.writerow([i[0] for i in cursor.description])
            # write headers
            csv_writer.writerows(cursor)
            del csv_writer
            # this will close the CSV file


class Ui_AV_Summary(QDialog, Ui_AV_Summary):
    """Class for the Dialog window for the
    options to export the database based on date given."""
    def __init__(self):
        """The Initialization of the Dialog window."""
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.avsumprep.clicked.connect(self.avsummarydialog)
        self.Startdateedit.setDate(date.today())
        self.Enddateedit.setDate(date.today())

    def avsummarydialog(self):
        """Function to export from the database
         based on dates to produce an AV summary."""
        #Opens a Dialog to save the file
        startdate = self.Startdateedit.date()
        enddate = self.Enddateedit.date()
        startdate1 = str(startdate.toPyDate().strftime('%m/%d/%y'))
        enddate1 = str(enddate.toPyDate().strftime('%m/%d/%y'))
        folder = QFileDialog.getSaveFileName(
            None, str("Save File"), str("AV Summary.txt"), str("TXT(*.txt)"))
        conn = sqlite3.connect("AV_sum.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * from AV WHERE date_rec BETWEEN '" +
            startdate1 + "' and '" + enddate1 + "%'")
        r = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        results = []
        for row in r:
            summary = dict(zip(columns, row))
            results.append(summary)
        with open(folder, 'w') as f:
            for x in results:
                f.write("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

DEVICE: %s   %s
IP (at time of detection): %s
USER (at time of detection): %s
DETECTION: %s
DATE-TIME (CT): Received: %s    Generated: %s
ACTION: %s
LOCATION:
%s
LOGS PULLED: %s
DAT VERSION: %s
COMMENTS:
%s



"""
                        % (x['hostname'], x['device_type'],
                            x['ip_address'], x['username'],
                            x['detection'], x['date_rec'],
                            x['date_gen'], x['action'],
                            x['filepath'], x['logs'],
                            x['dat_version'], x['comments']))
                continue
                f.close()
            self.done(0)


class Dialog(QDialog, Ui_Dialog):
    """Class for the Dialog window for the
    options to export the database based on date given."""
    def __init__(self):
        """The Initialization of the Dialog window."""
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushExport.clicked.connect(self.exportdb)
        self.dateEdit.setDate(date.today())

    def exportdb(self):
        """Function to export from the database
        based on the date to csv file format."""
        datedb = self.dateEdit.date()
        datedb = str(datedb.toPyDate().strftime('%m%d%Y'))
        datedb2 = self.dateEdit.date()
        datedb2 = str(datedb2.toPyDate().strftime('%m/%d/%y'))
        folder = QFileDialog.getSaveFileName(
            None, str("Save File"), str(
                "AV_OUTPUT_DATE_%s.csv" % datedb), str("CSV(*.csv)"))
        conn = sqlite3.connect("AV_sum.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * from AV WHERE date_rec LIKE '" + datedb2 + "%'")
        csv_writer = csv.writer(open(folder, "wb"))
        csv_writer.writerow([i[0] for i in cursor.description])
        # write headers
        csv_writer.writerows(cursor)
        del csv_writer
        # this will close the CSV file
        self.done(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
