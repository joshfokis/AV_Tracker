AV_Tracker
==========

Manually track and store in a Database of AV detections on your network.
----------

1.AV Summary Entry
----------
Fill out the form with the correct information to the corresponding entry fields. The device type field is a drop down menu that contains the following device types: Desktop, Laptop, and Server.  Also the action menu contains: On Access Deleted, On Access Cleaned, Managed Scan Deleted, Managed Scan Cleaned, and Script Scan Blocked
After Entering the information and check that it is correct, click the save button to submit the information to the database. Once it has saved to the database the form will clear out and you will see a new row appended to the database with the information you have entered.

2.	Update Row
----------
If any information was left out or needed to be added at a later time, there are two options to updating a row.  The first option is by double clicking in a cell, which is only ideal if you need to append little information to one cell. 
The next option is ideal if multiple fields need to be updated or corrected.  Select the database menu from the menu bar and the option Update Row. Once the option has been selected a window will open asking for the row number. Enter the correct row number indicated on the vertical numbers to the left of the database. After typing the correct row number and clicking ok, the fields in the form will populate with the information from the row. The save button now turns into the update button to update the row and clear out the fields when finished. 

3.	Delete Row
----------
The delete row option will delete the row that is either a duplicate or a blank row. Select the delete row option from the database menu and a window similar to the update row will open up. Type the number of the row you wish to delete and click ok. READ THE NEXT POPUPAS IT WILL INFORM YOU OF THE ROW THAT IS ABOUT TO BE DELETED AND IF YOU WISH TO CONTINUE. MAKE SURE THAT IS THE CORRECT ROW.  Once you confirmed the row and are ready to continue with the deletion click yes and the row will be permanently deleted from the database.

4.	Filter Search
----------
If a need arises to search the database without exporting to a csv, there is a search field at the bottom of the application. You can search by hostname or username.  Once you have chosen and entered the search criteria continue by clicking search. The database view above will change and filter out everything but your search results. To return to the original view there is a clear button next to search button click the clear button and the view should return to the original view.

5.	Export AV Summary Text
----------
To get the data for the AV Summary Text email select the Export Morning Call option from the database menu.  A window will open to input the start date that must be entered MANUALLY. Once ok is clicked on the first window another window will open to input the end date that must also be input MANUALLY. Once ok is clicked for the end date selection you will be prompt to save a text document to a location. Select the location and save the file. 

6.	Export By Date Received
----------
Select the Date Received option from the database menu and export by submenu to export to a csv file for the selected date. Once export is clicked after the date is selected you will be prompt to save the csv file to a location.

7.	Export By Hostname
----------
Select the export by Hostname option from the database menu and export by submenu to export to a csv file for the selected hostname. Once export is clicked after the date is selected you will be prompt to save the csv file to a location.

8.	Export By Username
----------
Select the export by Username option from the database menu and export by submenu to export to a csv file for the selected Username. You have the option of using a wildcard ‘%’ to search by part of a username. Once export is clicked after the date is selected you will be prompt to save the csv file to a location.

9.	Export Entire Database
----------
Select the export entire database option from the database menu. The Export Entire Database will export the entire database to a csv file.
