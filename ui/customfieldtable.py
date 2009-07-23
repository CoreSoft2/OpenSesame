# ui/customfieldtable.py
# JFX OpenVPN Client

# This file is part of the JFX OpenVPN Client GUI. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

from PyQt4.QtGui import QTableWidget, QTableWidgetItem

class CustomFieldTable(QTableWidget):
    def addCustomField(self, key=None, value=None):
        rc=self.rowCount()
        self.insertRow(rc)
        
        if key is not None:
            twi = QTableWidgetItem
            if value is None:
                value = ''
            self.setItem(rc, 0, twi(key))
            self.setItem(rc, 1, twi(value))
    
    def removeCustomField(self):
        row = self.currentRow()
        
        if row > 0:
            self.removeRow(row)
    
    def getCustomFields(self):
        rc = self.rowCount()
        for i in range(0,rc):
            field = self.getItem(i, 0).text()
            value = self.getItem(i, 1).text()
            yield (field, value)
    
