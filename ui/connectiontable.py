# ui/connectiontable.py
# OpenSesame

# This file is part of OpenSesame. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.


from PyQt4.QtGui import QTableWidget, QTableWidgetItem

class ConnectionTable(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.configs = {}
        self.map = {}
    
    def getConfigNames(self):
        return self.map.keys()
    
    def setState(self, name, state):
        name=str(name)
        row = self.map[name]
        
        i = self.item(row, 0)
        i.setText(state)
        
    def appendRow(self, ovconfig):
        rc = self.rowCount()
        self.insertRow(rc)
        self.configs[rc] = ovconfig
        
        name = ovconfig.getname()
        self.map[name] = rc
        
        twi = QTableWidgetItem
        self.setItem(rc, 0, twi('Disconnected'))
        self.setItem(rc, 1, twi(name))
        self.setItem(rc, 2, twi(ovconfig.getremote()))
        if ovconfig.getdescription() is not None:
            self.setItem(rc, 3, twi(ovconfig.getdescription()))
        else:
            self.setItem(rc, 3, twi(''))
        
        self.resizeColumnsToContents()
    
    def editRow(self, key, ovconfig):
        self.configs[key] = ovconfig
        
        i = self.item(key, 1)
        i.setText(ovconfig.getname())
        #self.editItem(i)
        
        i = self.item(key, 2)
        i.setText(ovconfig.getremote())
        #self.editItem(i)
        
        i = self.item(key, 3)
        i.setText(ovconfig.getdescription())
        #self.editItem(i)
        
        self.resizeColumnsToContents()
    
    def removeRow(self, key):
        if self.configs.has_key(key):
            name = self.configs[key].getname()
            del self.map[name]
            del self.configs[key]
        
        QTableWidget.removeRow(self, key)
